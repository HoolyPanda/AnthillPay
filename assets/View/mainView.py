import vk_api
from vk_api import bot_longpoll
import os
import threading
import random

from assets.Model.HumanModel import Human

from assets.Controller.registrationController import RegistrationController as rC
from assets.Controller.HumanController import *

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



