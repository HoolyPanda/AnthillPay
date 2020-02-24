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
class mainView(threading.Thread):
    def __init__(self, session, userId: int, event):
        threading.Thread.__init__(self)
        self.session = session
        self.userId = userId
        self.event = event
        pass
    def run(self):

        # self.session.met        
        lps = bot_longpoll.VkBotLongPoll(self.session, 172301854)
        if rC.CheckRegistration(None, id= self.userId):
            user = Human().LoadFromJson('./DB/' + str(self.userId) + '.json')
            self.session.method('messages.send', {
                'message': 'Main Menu',
                'peer_id': self.userId,
                'random_id': random.randint(1, 10000000000000),
                'keyboard': None
            })
            try:
                for event in bot_longpoll.VkBotLongPoll.listen(lps):
                    # if event
                    if event['raw']['object']['from_id'] == self.userId:
                            pass
                    pass
            except Exception as e:
                print(str(e))
                quit
        else:
            self.session.method('messages.send', {
                'message': 'HumanCreator Menu',
                'peer_id': self.userId,
                'random_id': random.randint(1, 10000000000000),
                'keyboard': keyboards.humanCreatorKB
            })
            hC =  HumanCreator.HumanCreator(lps= lps, id= str(self.userId), session= self.session)



