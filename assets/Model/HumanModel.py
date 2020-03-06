import json
from typing import overload

import pyqrcode
from pyqrcode import QRCode
import base64
# import pypng


class Human(object):
    def __init__(self,name: str = None, hair: str = None, eyes: str = None, vkId: int= None, password: str = None):
        self.hair = hair
        self.eyes = eyes
        self.name = name
        self.vkId = vkId
        self.password = password
        self.id = 0
        self.money = 0
        self.transactions = []
        # TODO: weapons 
    pass

    def GenerateaUserHash(self):
        try:
            self.id = hash(str([str.encode(self.hair, encoding= 'utf-8'), str.encode(self.eyes, encoding= 'utf-8'), str.encode(str(self.vkId), encoding= 'utf-8'), self.name, str.encode(self.password, encoding= 'utf-8')]))
        except Exception:
            self.id = 0
        
        pass

    def GenerateQR(self):
        payload = str(base64.b64encode(bytes(f'TransferMoneyTo {str(self.id)}', 'utf-8')), 'utf-8')
        a = pyqrcode.create(payload)
        a.png(f'./DB/QRs/{str(self.vkId)}.png', scale=6, module_color=[0, 0, 0, 255], background=[0xff, 0xff, 0xff])
        # TODO: upload qr code to vk
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
        self.name = profile['name'] 
        self.eyes = profile['eyes']
        self.hair = profile['hair']
        self.id = profile['id']
        self.money = profile['money']
        self.vkId = profile['vkId']
        self.password = profile['password']
        self.transactions = profile['transactions']
        return self

    # @LoadFromJson.overload()
    def LoadFromJsonObject(self, modelDump:{}):
        self.name = modelDump['name'] 
        self.eyes = modelDump['eyes']
        self.hair = modelDump['hair']
        if 'id' in modelDump:
            self.id = modelDump['id']
        else:
            self.id = None

        if 'money' in modelDump:
            self.money = modelDump['money']
        else:
            self.money = None
        self.vkId = modelDump['vkId']
        self.password = modelDump['password']
        self.transactions = modelDump['transactions']
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