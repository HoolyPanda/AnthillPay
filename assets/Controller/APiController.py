import json
import random
import assets.Controller.HumanController as HumanController
import assets.Controller.MoneyController as MoneyController

class APIController:
    def __init__(self, session):
        self.session = session
        self.MoneyController = MoneyController.MoneyController()
        self.HumanController = HumanController.HumanController()
        pass

    def GenerateEvidences(self, hackingPoints: int, victim, hacker):
        evidences = {}
        if hackingPoints <= 40:
            evidences.update({'name': hacker.name, 'work': hacker.work})
            pass
        elif hackingPoints > 50:
            evidences.update({'work': hacker.work})
            pass
        elif hackingPoints > 70:
            evidences.update({'eyes': hacker.eyes})
            pass
        return evidences

    def ParseEvent(self, event):
        request = json.loads(event.raw['object']['text'])
        a =0
        if request['action'] == 'hack':
            victimApayID = request['victimID']
            hackerVkID = request['hackerVkID']
            hackingPoints = request['hackingPoints']
            if request['type'] == 'money':
                stolenMoney = request['amount']
                victim = self.HumanController.LoadHumanFromAPayID(victimApayID)
                hacker = self.HumanController.LoadHumanFromVkID(hackerVkID)
                evidenceNumber = random.randint(1,4)
                evidences = self.GenerateEvidences(hackingPoints= hackingPoints, victim= victim, hacker= hacker)
                victim.evidences.append(evidences)

                if self.MoneyController.FixedMoneyTransaction(frm= victim, to= hacker, amount= stolenMoney):
                    self.session.method('messages.send', {
                        'message': f'ERROR ERROR\nС000000вершен4 прод4ж4 н4 сумму {str(stolenMoney)}',
                        'peer_id': hackerVkID,
                        'random_id': 0
                    }) 
                    self.session.method('messages.send', {
                        'message': f'ERROR ERROR\nС000000вершен4 покупк4 н4 сумму {str(stolenMoney)}\nТовар: NULL',
                        'peer_id': victim.vkId,
                        'random_id': 0
                    }) 
                    
                    return True
                else:
                    pass
            elif request['type'] == 'profile':
                victim = self.HumanController.LoadHumanFromAPayID(victimApayID)
                hacker = self.HumanController.LoadHumanFromVkID(hackerVkID)
                evidences = {
                    'name': hacker.name,
                    'work': hacker.work,
                    'hair': hacker.hairColor,
                    'eyes': hacker.eyeColor,
                    'id': hacker.id
                }
                victim.evidences.append(evidences)
                victim.SaveToJsonFile()
                if hackingPoints > 0:
                    payload = f"""Имя: {victim.name}
                                Цвет Глаз: {victim.eyeColor}
                                Цвет Волос: {victim.hairColor}
                                Место Работы: {victim.work}
                                Родился в: {victim.district}
                                Пароль Безопасности: {victim.password}
                                """         
                    self.session.method('messages.send', {
                            'message': payload,
                            'peer_id': hackerVkID,
                            'random_id': 0,
                            'attachment': victim.QRcodeURL 
                        }) 
                    self.session.method('messages.send', {
                            'message': "Выполнен вход с другого устройства",
                            'peer_id': victim.vkId,
                            'random_id': 0
                        }) 
                return True
