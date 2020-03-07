import assets.Model.HumanModel as HM
# import assets.Model.HumanModel
import os
import json
import random

class HumanController:
    def __init__(self):
        self.loadedAccounts = []
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
                        'random_id': random.randint(1, 10000000000000)
                    })
                
                if 'profile' in payload.values():
                    name = account.name
                    id = account.id
                    session.method('messages.send', {
                        'message': f"Имя: {str(name)}\nЛичный номер: {str(id)}",
                        'peer_id': account.vkId,
                        'random_id': random.randint(1, 10000000000000)
                    })
                    pass

                if 'history' in payload.values():
                    msg = ''
                    for transaction in account.transactions:
                        msg += f'{transaction}\n'
                    session.method('messages.send', {
                        'message': f"История транзакций:\n{msg}",
                        'peer_id': account.vkId,
                        'random_id': random.randint(1, 10000000000000)
                    })

                if 'QR' in payload.values():
                    session.method('messages.send', {
                        'message': f"",
                        'peer_id': account.vkId,
                        'random_id': random.randint(1, 10000000000000),
                        'attachment': account.QRcodeURL
                    })

            pass
        return True
