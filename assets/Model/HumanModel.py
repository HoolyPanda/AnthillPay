import json
import vk_api
from vk_api import VkUpload 
import requests
from typing import overload

import pyqrcode
from pyqrcode import QRCode
import base64


class Human(object):
    def __init__(self, name: str = None, hair: str = None, eyes: str = None, vkId: int= None, password: str = None):
        self.hairColor = hair
        self.eyeColor = eyes
        self.name = name
        self.vkId = vkId
        self.password = password
        self.id = 0
        self.money = 0
        self.district = ''
        self.work = ''
        self.transactions = []
        self.QRcodeURL = ''
        self.evidences = []
        # TODO: weapons 
    pass

    def GenerateaUserHash(self):
        try: #stangebug
            self.id = hash(str([str.encode(self.hairColor, encoding= 'utf-8'), str.encode(self.eyes, encoding= 'utf-8'), str.encode(str(self.vkId), encoding= 'utf-8'), self.name, str.encode(self.password, encoding= 'utf-8')]))
        except Exception:
            self.id = 0
        
        pass

    def GenerateQR(self):
        payload = str(base64.b64encode(bytes(f'TransferMoneyTo {str(self.id)}', 'utf-8')), 'utf-8')
        a = pyqrcode.create(payload)
        QRfile = f'./DB/QRs/{str(self.vkId)}.png'
        a.png(QRfile, scale=8, module_color= [0, 0, 0, 255], background=[0xff, 0xff, 0xff])

        login = open('./login.cred', 'r').readline()
        password = open("./password.cred", 'r').readline()
        groupID = 192654141
        albumID = 271112751

        client = vk_api.VkApi(login, password)
        client.auth()
        u = VkUpload(client)
        a = u.photo(photos= QRfile, album_id= albumID, group_id= groupID, caption= f'QrCode')
        a = a[0]
        ownerId = a['owner_id']
        mediaId = a['id']
        self.QRcodeURL = f'photo{ownerId}_{mediaId}'
        pass

    def getMoney(self):
        return self.money

    def getPassword(self):
        return self.password
    
    def setPassword(self, newPassword: str):
        self.password = newPassword

    def AddMoney(self, amount: int):
        self.money = self.money + amount
        self.transactions.append(f'+{str(amount)}')
        self.SaveToJsonFile()
        return True

    def RemoveMoney(self, amount: int):
        if self.money - amount >= 0:
            self.money = self.money - amount
            self.transactions.append(f'-{str(amount)}')
            self.SaveToJsonFile()
            return True
        else:
            return False

    def SaveToJsonFile(self):
        profile = open('./DB/' + str(self.vkId) + '.json', 'w+')
        dump = json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        profile.write(dump)
        profile.close()
        return dump

    def getJson(self):
        dump = json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        return json.loads(dump)

    def LoadFromJson(self, path: str):
        profile = open(path, 'r').read()
        profile = json.loads(profile)
        self.__dict__.update(profile)
        return self

    # @LoadFromJson.overload()
    def LoadFromJsonObject(self, profile:{}):
        self.__dict__.update(profile)
        return self        

# a = Human(eyes= 'a', hair= 'b', name= "пробное имя")
# a = Human()
# a.SaveToJson()
# a.LoadFromJson('./DB/160500068.json')
# a.GenerateQR()
# a.RemoveMoney(100)
# a.AddMoney(100)
# a = Human().LoadFromJson('./DB/160500068.json')
# a.AddMoney(100)
# a.SaveToJsonFile()
# print('')