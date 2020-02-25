from vk_api import bot_longpoll
import threading
import random
import json
import assets.View.keyboards
from assets.Model.HumanModel import Human

class HumanCreator():
    def __init__(self, id: int, session):
        self.currentParametr = ''
        self.humanModel = Human(vkId= id)
        self.session = session
        self.id = id

    def ParseEvent(self, event):
        value = event.raw['object']['text']
        if 'payload' in event.raw['object']:

            if 'button' in json.loads(event.raw['object']['payload']):
                payload = json.loads(event.raw['object']['payload'])['button'] 
            elif 'eyeColor' in json.loads(event.raw['object']['payload']):
                payload = 'eyeColor'

            if payload == 'name':
                self.session.method('messages.send', {
                    'message': 'Введите свое имя:',
                    'peer_id': self.id,
                    'random_id': random.randint(1, 10000000000000)
                })
                self.currentParametr = payload
            elif payload == 'eyes':                    
                self.session.method('messages.send', {
                    'message': 'Выберите цвет глаз',
                    'peer_id': self.id,
                    'random_id': random.randint(1, 10000000000000),
                    'keyboard': assets.View.keyboards.eyeColorKB
                })
                self.currentParametr = payload
            elif payload == 'password':
                self.session.method('messages.send', {
                    'message': "Задайте пароль для вашего аккаунта AnthillPay.\nВ целях безопасности, не сообщайте его никому и удалите сообщение с ним",
                    'peer_id': self.id,
                    'random_id': random.randint(1, 10000000000000),
                })
                self.currentParametr = payload
            elif payload == 'hair':
                self.session.method('messages.send', {
                    'message': "Введите цвет волос",
                    'peer_id': self.id,
                    'random_id': random.randint(1, 10000000000000),
                })
                self.currentParametr = payload                    
                

            elif payload == 'eyeColor':
                self.SaveCurrentParametr(json.loads(event.raw['object']['payload'])[payload])
                self.session.method('messages.send', {
                    'message': f"Параметр {self.currentParametr} успешно задан.",
                    'peer_id': self.id,
                    'random_id': random.randint(1, 10000000000000),
                    'keyboard': assets.View.keyboards.humanCreatorKB
                })
            elif payload == 'confirm':
                self.currentParametr = 'vkId'
                self.SaveCurrentParametr(int(self.id))
                self.humanModel.GenerateaUserHash()
                self.humanModel.SaveToJsonFile()
                return True
            # TODO: payload eq 'false'
                

        else:
            if self.currentParametr:
                self.SaveCurrentParametr(value)
                self.session.method('messages.send', {
                    'message': f"Параметр {self.currentParametr} успешно задан.",
                    'peer_id': self.id,
                    'random_id': random.randint(1, 10000000000000),
                    'keyboard': assets.View.keyboards.humanCreatorKB
                })
                self.currentParametr = ''
        pass
        # pass

    def SaveCurrentParametr(self, value):
        humanDump = self.humanModel.getJson()
        humanDump[self.currentParametr] = value
        self.humanModel.LoadFromJsonObject(modelDump= humanDump)