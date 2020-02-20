import json

class Human:
    def __init__(self,name: str = None, hair: str = None, eyes: str = None, vkId: int= None, password: str = None):
        self.hair = hair
        self.eyes = eyes
        self.name = name
        self.vkId = vkId
        self.password = password
        try:
            self.id = hash(str([str.encode(hair, encoding= 'utf-8'), str.encode(hair, encoding= 'utf-8'), str.encode(vkId, encoding= 'utf-8'), name, str.encode(password, encoding= 'utf-8')]))
        except Exception:
            self.id = 0
        self.money = 0
    pass

    def AddMoney(self, amount: int):
        self.money = self.money + amount
        return True

    def RemoveMoney(self, amount: int):
        if self.money - amount >= 0:
            self.money = self.money - amount
            return True
        else:
            return False

    def SaveToJson(self):
        profile = open('./DB/' + self.name + '.json', 'w+')
        dump = json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        profile.write(dump)
        profile.close()
        pass

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
        # pass


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