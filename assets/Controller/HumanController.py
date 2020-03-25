import assets.Model.HumanModel as HM
# import assets.Controller.MoneyController as MC
from assets.Controller.MoneyController import MoneyController as MC
import assets.View.keyboards as keyboards
# import assets.Model.HumanModel
import os
import json
import random

class HumanController:
    def __init__(self, session):
        self.loadedAccounts = []
        self.targetAccaunt = 0
        self.isTransferingMoney = False
        self.MController = MC()
        # self.session = sessiosn
        self.userId = 0
        pass

    def CheckIfIdIsLoaded(self, vkID: int):
        for user in self.loadedAccounts:
            if user.vkId == vkID:
                return True
        return False    
    
    def GetUserById(self, vkID: int):
        for user in self.loadedAccounts:
            if user.vkId == vkID:
                return user
        pass

    def LoadHumanFromVkID(self, vkID:int):
        path = './DB/'
        for f in os.listdir(path):
            if f == f'{str(vkID)}.json':
                hm = HM.Human()
                self.loadedAccounts.append(hm.LoadFromJson(path= f'{path}{f}'))
                return hm.LoadFromJson(path= f'{path}{f}')
        return None

    def LoadHumanFromAPayID(self, aPayID: int):
        path = './DB/'
        for f in os.listdir(path):
                if not os.path.isdir(f'{path}{f}'):
                    hm = HM.Human()
                    hm.LoadFromJson(path= f'{path}{f}')
                    if hm.id == aPayID:
                        self.loadedAccounts.append(hm.LoadFromJson(path= f'{path}{f}'))
                        return hm.LoadFromJson(path= f'{path}{f}')
        return None 

    def ParseEvent(self, event, account, session):
        rawEvent = event.raw['object']
        if 'payload' in rawEvent:
            payload = json.loads(rawEvent['payload'])
            if 'mainMenu' in payload.keys():
                
                if 'finances' in payload.values():
                    session.method('messages.send', {
                        'message': f'У вас на счету {str(account.money)} ньюйен',
                        'peer_id': account.vkId,
                        'random_id': random.randint(1, 10000000000000),
                        'keyboard': keyboards.mainKB
                    })
                
                if 'profile' in payload.values():
                    name = account.name
                    id = account.id
                    session.method('messages.send', {
                        'message': f"Имя: {str(name)}\nЛичный номер: {str(id)}",
                        'peer_id': account.vkId,
                        'random_id': random.randint(1, 10000000000000),
                        'keyboard': keyboards.mainKB
                    })
                    pass

                if 'history' in payload.values():
                    msg = ''
                    for transaction in account.transactions:
                        msg += f'{transaction}\n'
                    session.method('messages.send', {
                        'message': f"История транзакций:\n{msg}",
                        'peer_id': account.vkId,
                        'random_id': random.randint(1, 10000000000000),
                        'keyboard': keyboards.mainKB
                    })

                if 'QR' in payload.values():
                    session.method('messages.send', {
                        'message': f"",
                        'peer_id': account.vkId,
                        'random_id': random.randint(1, 10000000000000),
                        'attachment': account.QRcodeURL,
                        'keyboard': keyboards.mainKB
                    })
            elif 'additionalFunction' in payload.keys():
                if self.targetAccaunt != 0:

                    if 'Валидация' in payload.values():
                        targetUser = self.LoadHumanFromAPayID(self.targetAccaunt)
                        currentUser = self.GetUserById(self.userId)
                        if targetUser.work == currentUser.work:
                            session.method('messages.send', {
                                'message': 'Валидация успешно пройдена',
                                'peer_id': self.userId,
                                'random_id': random.randint(1, 10000000000000),
                                'keyboard': keyboards.mainKB
                            })
                        else:
                            session.method('messages.send', {
                                'message': 'Валидация провалена',
                                'peer_id': self.userId,
                                'random_id': random.randint(1, 10000000000000),
                                'keyboard': keyboards.mainKB
                            })
                        return True

                    elif 'Перевести деньги' in payload.values():
                        self.isTransferingMoney = True
                        self.MController.tansactionInProgress = True
                        self.MController.TransferMoney(to= self.LoadHumanFromAPayID(self.targetAccaunt), fromUser= self.LoadHumanFromVkID(self.userId))
                        session.method('messages.send', {
                            'message': 'Введите сумму для перевода',
                            'peer_id': self.userId,
                            'random_id': random.randint(1, 10000000000000)
                        })
                        # self.moneyController.FixedMoneyTransaction()
                        a = 0
                        return False
            
        elif self.MController.tansactionInProgress:
            if self.MController.ParseEvent(self, event.raw['object']):
                a = 0
                session.method('messages.send', {
                    'message': 'Сумма успешно переведена',
                    'peer_id': self.userId,
                    'random_id': random.randint(1, 10000000000000),
                    'keyboard': keyboards.mainKB
                })
                pass
            else:
                session.method('messages.send', {
                    'message': 'Во время транзакции что-то пошло не так. Проверьте плетежные реквезиты и свой счет, если там недостаточно денег',
                    'peer_id': self.userId,
                    'random_id': random.randint(1, 10000000000000),
                    'keyboard': keyboards.mainKB
                })
                pass
            pass
            return True
        else:
            session.method('messages.send', {
                'message': 'Main Menu',
                'peer_id': self.userId,
                'random_id': random.randint(1, 10000000000000),
                'keyboard': keyboards.mainKB
            })

        return True
