from vk_api import bot_longpoll
import threading
import random
import json
import assets.View.keyboards
from assets.Model.HumanModel import Human

class HumanCreator():
    def __init__(self, id: int, lps, session):
        self.currentParametr = ''
        self.humanModel = Human(vkId= id)
        for event in bot_longpoll.VkBotLongPoll.listen(lps):
            value = event.raw['object']['text']
            if 'payload' in event.raw['object']:

                if 'button' in json.loads(event.raw['object']['payload']):
                    payload = json.loads(event.raw['object']['payload'])['button'] 
                elif 'eyeColor' in json.loads(event.raw['object']['payload']):
                    payload = 'eyeColor'

                if payload == 'name':
                    session.method('messages.send', {
                        'message': 'Введите свое имя:',
                        'peer_id': id,
                        'random_id': random.randint(1, 10000000000000)
                    })
                    self.currentParametr = payload
                elif payload == 'eyes':                    
                    session.method('messages.send', {
                        'message': 'Выберите цвет глаз',
                        'peer_id': id,
                        'random_id': random.randint(1, 10000000000000),
                        'keyboard': assets.View.keyboards.eyeColorKB
                    })
                    self.currentParametr = payload
                elif payload == 'password':
                    session.method('messages.send', {
                        'message': "Задайте пароль для вашего аккаунта AnthillPay.\nВ целях безопасности, не сообщайте его никому и удалите сообщение с ним",
                        'peer_id': id,
                        'random_id': random.randint(1, 10000000000000),
                    })
                    self.currentParametr = payload
                elif payload == 'hair':
                    session.method('messages.send', {
                        'message': "Введите цвет волос",
                        'peer_id': id,
                        'random_id': random.randint(1, 10000000000000),
                    })
                    self.currentParametr = payload                    
                    

                elif payload == 'eyeColor':
                    self.SaveCurrentParametr(json.loads(event.raw['object']['payload'])[payload])
                    session.method('messages.send', {
                        'message': f"Параметр {self.currentParametr} успешно задан.",
                        'peer_id': id,
                        'random_id': random.randint(1, 10000000000000),
                        'keyboard': assets.View.keyboards.humanCreatorKB
                    })
                elif payload == 'confirm':
                    self.currentParametr = 'vkId'
                    self.SaveCurrentParametr(int(id))
                    self.humanModel.GenerateaUserHash()
                    self.humanModel.SaveToJsonFile()

                    

            else:
                self.SaveCurrentParametr(value)
                session.method('messages.send', {
                    'message': f"Параметр {self.currentParametr} успешно задан.",
                    'peer_id': id,
                    'random_id': random.randint(1, 10000000000000),
                    'keyboard': assets.View.keyboards.humanCreatorKB
                })
                self.currentParametr = ''
            pass
        pass

    def SaveCurrentParametr(self, value):
        humanDump = self.humanModel.getJson()
        humanDump[self.currentParametr] = value
        self.humanModel.LoadFromJsonObject(modelDump= humanDump)