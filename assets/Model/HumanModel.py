import json
from typing import overload


class Human(object):
    def __init__(self,name: str = None, hair: str = None, eyes: str = None, vkId: int= None, password: str = None):
        self.hair = hair
        self.eyes = eyes
        self.name = name
        self.vkId = vkId
        self.password = password
        self.id = 0
        self.money = 0
    pass

    def GenerateaUserHash(self):
        try:
            self.id = hash(str([str.encode(self.hair, encoding= 'utf-8'), str.encode(self.eyes, encoding= 'utf-8'), str.encode(str(self.vkId), encoding= 'utf-8'), self.name, str.encode(self.password, encoding= 'utf-8')]))
        except Exception:
            self.id = 0
        
        pass

    def getMoney(self):
        return self.money

    def getPassword(self):
        return self.password
    
    def setPassword(self, newPassword: str):
        self.password = newPassword

    def AddMoney(self, amount: int):
        self.money = self.money + amount
        return True

    def RemoveMoney(self, amount: int):
        if self.money - amount >= 0:
            self.money = self.money - amount
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
        return self        

# a = Human(eyes= 'a', hair= 'b', name= "пробное имя")
# a = Human()
# a.SaveToJson()
# a.LoadFromJson('./DB/пробное имя.json')
# a.RemoveMoney(100)
# a.AddMoney(100)
# a.SaveToJson()
# a = Human().LoadFromJson('./DB/пробное имя.json')
# a.AddMoney(100)
# print('')