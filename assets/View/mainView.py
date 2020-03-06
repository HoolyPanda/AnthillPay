import vk_api
from vk_api import bot_longpoll
import os
import threading
import random
import base64

from assets.Model.HumanModel import Human

from assets.Controller.registrationController import RegistrationController as rC
from assets.Controller.HumanController import *
from assets.Controller.MoneyController import MoneyController

import assets.View.HumanCreator as HumanCreator
import assets.View.keyboards as keyboards
# import assets.View.MainMenu as MainMenu


token = open('./token.cred').read()
class mainView():
    def __init__(self, session, userId: int, event):
        
        self.session = session
        self.userId = userId
        self.event = event
        self.hC = None
        self.HController = HumanController()
        self.MController = MoneyController()
        pass
    def ParseEvent(self, event):

        # self.session.met        
        if rC.CheckRegistration(None, id= self.userId):
            # user = Human().LoadFromJson('./DB/' + str(self.userId) + '.json').
            if not self.HController.CheckIfIdIsLoaded(vkID= self.userId):
                user = self.HController.LoadHumanFromVkID(vkID= self.userId)
            else:
                user = self.HController.GetUserById(vkID= self.userId)
            if user:
                try:
                    b64 = str(base64.b64decode(event.raw['object']['text']), 'utf-8')
                    a = b64[:len('TransferMoneyTo ')] 
                    if b64[:len('TransferMoneyTo ')] == 'TransferMoneyTo ':
                        self.MController.TransferMoney(to= int(b64[len('TransferMoneyTo '):]), fromVkID= user.vkId)
                        self.session.method('messages.send', {
                            'message': 'Введите сумму перевода',
                            'peer_id': self.userId,
                            'random_id': random.randint(1, 10000000000000)
                        })       
                        return False                 
                except Exception as e:
                    pass
                if self.MController.tansactionInProgress:
                    if self.MController.ParseEvent(self, event.raw['object']):
                        a = 0
                        self.session.method('messages.send', {
                            'message': 'Сумма успешно переведена',
                            'peer_id': self.userId,
                            'random_id': random.randint(1, 10000000000000),
                            'keyboard': keyboards.mainKB
                        })
                        pass
                    else:
                        self.session.method('messages.send', {
                            'message': 'Во время транзакции что-то пошло не так. Проверьте плетежные реквезиты и свой счет, если там недостаточно денег',
                            'peer_id': self.userId,
                            'random_id': random.randint(1, 10000000000000),
                            'keyboard': keyboards.mainKB
                        })
                        pass
                    pass
                    return True
                else:
                    self.session.method('messages.send', {
                        'message': 'Main Menu',
                        'peer_id': self.userId,
                        'random_id': random.randint(1, 10000000000000),
                        'keyboard': keyboards.mainKB
                    })
                    if self.HController.ParseEvent(event, user, self.session):
                        return True
            else:
                # TODO: error
                pass
        else:
            if not self.hC:
                self.hC = HumanCreator.HumanCreator(id= str(self.userId), session= self.session)
                self.session.method('messages.send', {
                    'message': 'HumanCreator Menu',
                    'peer_id': self.userId,
                    'random_id': random.randint(1, 10000000000000),
                    'keyboard': keyboards.humanCreatorKB
                })
            else:
                if self.hC.ParseEvent(event) == True:
                    return True
                else:
                    pass



