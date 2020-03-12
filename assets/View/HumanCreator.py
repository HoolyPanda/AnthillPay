from vk_api import bot_longpoll
import threading
import random
import json
import assets.View.keyboards
from assets.Model.HumanModel import Human

class HumanCreator():
    def __init__(self, id: int, session):
        self.currentParametr = ''
        self.humanModel = Human(vkId= int(id))
        self.humanDump = {}
        self.session = session
        self.id = id
    def ParseEvent(self, event):
        payload = ''
        value = event.raw['object']['text']
        if 'payload' in event.raw['object']:

            if 'button' in json.loads(event.raw['object']['payload']):
                payload = json.loads(event.raw['object']['payload'])['button'] 
            elif 'eyeColor' in json.loads(event.raw['object']['payload']):
                payload = 'eyeColor'                
            elif 'hairColor' in json.loads(event.raw['object']['payload']):
                payload = "hairColor"

            elif 'workPlace' in json.loads(event.raw['object']['payload']):
                self.currentParametr = 'work'
                self.SaveCurrentParametr(value)
                self.session.method('messages.send', {
                    'message': f"Параметр успешно задан.",
                    'peer_id': self.id,
                    'random_id': random.randint(1, 10000000000000),
                    'keyboard': assets.View.keyboards.humanCreatorKB
                })
            elif 'height' in json.loads(event.raw['object']['payload']):
                self.currentParametr = 'height'
                self.SaveCurrentParametr(value)
                self.session.method('messages.send', {
                    'message': f"Параметр успешно задан.",
                    'peer_id': self.id,
                    'random_id': random.randint(1, 10000000000000),
                    'keyboard': assets.View.keyboards.humanCreatorKB
                })

            elif 'homeDistrict' in json.loads(event.raw['object']['payload']):
                self.currentParametr = 'district'
                self.SaveCurrentParametr(value)
                self.session.method('messages.send', {
                    'message': f"Параметр успешно задан.",
                    'peer_id': self.id,
                    'random_id': random.randint(1, 10000000000000),
                    'keyboard': assets.View.keyboards.humanCreatorKB
                })
 

            if payload == 'name':
                self.session.method('messages.send', {
                    'message': 'Введите свое имя:',
                    'peer_id': self.id,
                    'random_id': random.randint(1, 10000000000000),
                    'keyboard': assets.View.keyboards.nullKB
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
                    'message': "Задайте пароль для Вашего чипа безопасности.\nНе сообщайте его никому и удалите сообщение с ним",
                    'peer_id': self.id,
                    'random_id': random.randint(1, 10000000000000)
                })
                self.currentParametr = payload
            elif payload == 'hair':
                self.session.method('messages.send', {
                    'message': "Введите цвет волос",
                    'peer_id': self.id,
                    'random_id': random.randint(1, 10000000000000),
                    'keyboard': assets.View.keyboards.hairKB
                })
            elif payload == 'height':
                self.session.method('messages.send', {
                    'message': "Выберите параметр роста",
                    'peer_id': self.id,
                    'random_id': random.randint(1, 10000000000000),
                    'keyboard': assets.View.keyboards.heightKB
                })

            elif payload == 'hairColor':
                self.currentParametr = payload  
                self.SaveCurrentParametr(value)                  
                self.session.method('messages.send', {
                    'message': f"Параметр успешно задан.",
                    'peer_id': self.id,
                    'random_id': random.randint(1, 10000000000000),
                    'keyboard': assets.View.keyboards.humanCreatorKB
                })
                pass

            elif payload == 'work':                
                self.session.method('messages.send', {
                    'message': "Выберите место работы",
                    'peer_id': self.id,
                    'random_id': random.randint(1, 10000000000000),
                    'keyboard': assets.View.keyboards.worksKB
                })
                pass

            elif payload == 'eyeColor':
                self.SaveCurrentParametr(json.loads(event.raw['object']['payload'])[payload])
                self.session.method('messages.send', {
                    'message': f"Параметр успешно задан.",
                    'peer_id': self.id,
                    'random_id': random.randint(1, 10000000000000),
                    'keyboard': assets.View.keyboards.humanCreatorKB
                })

            elif payload == 'district':
                self.session.method('messages.send', {
                    'message': "Укажите район, в котором вы родились",
                    'peer_id': self.id,
                    'random_id': random.randint(1, 10000000000000),
                    'keyboard': assets.View.keyboards.districtKB
                })

            elif payload == 'confirm':
                self.session.method('messages.send', {
                    'message': f"Обработка...",
                    'peer_id': self.id,
                    'random_id': random.randint(1, 10000000000000)
                })
                self.currentParametr = 'vkId'
                self.SaveCurrentParametr(int(self.id))
                self.humanModel.money = 200
                self.humanModel.GenerateaUserHash()
                self.humanModel.GenerateQR()
                self.humanModel.SaveToJsonFile()
                self.session.method('messages.send', {
                    'message': f"Добро пожаловать в AnthillPay!",
                    'peer_id': self.id,
                    'random_id': random.randint(1, 10000000000000),
                    'keyboard': assets.View.keyboards.mainKB
                })
                return True
            # TODO: payload eq 'false'
                

        else:
            if self.currentParametr:
                self.SaveCurrentParametr(value)
                self.session.method('messages.send', {
                    'message': f"Параметр успешно задан.",
                    'peer_id': self.id,
                    'random_id': random.randint(1, 10000000000000),
                    'keyboard': assets.View.keyboards.humanCreatorKB
                })
                self.currentParametr = ''
        pass
        # pass

    def SaveCurrentParametr(self, value):
        humanDump = self.humanModel.getJson()
        try:
            value = value.lower()
        except Exception as e:
            pass
        self.humanDump.update({self.currentParametr: value})
        self.humanModel.LoadFromJsonObject(self.humanDump)
        # humanDump[self.currentParametr] = value