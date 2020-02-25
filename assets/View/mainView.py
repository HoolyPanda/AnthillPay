import vk_api
from vk_api import bot_longpoll
import os
from assets.Controller.registrationController import RegistrationController as rC

from assets.Model.HumanModel import Human
import assets.View.HumanCreator as HumanCreator
import threading
import random
import assets.View.keyboards as keyboards


token = open('./token.cred').read()
class mainView():
    def __init__(self, session, userId: int, event):
        
        self.session = session
        self.userId = userId
        self.event = event
        self.hC = None
        pass
    def ParseEvent(self, event):

        # self.session.met        
        if rC.CheckRegistration(None, id= self.userId):
            user = Human().LoadFromJson('./DB/' + str(self.userId) + '.json')
            self.session.method('messages.send', {
                'message': 'Main Menu',
                'peer_id': self.userId,
                'random_id': random.randint(1, 10000000000000),
                'keyboard': None
            })
        else:
            if not self.hC:
                self.hC = HumanCreator.HumanCreator(id=str(self.userId), session= self.session)
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



