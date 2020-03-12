import assets.Controller.HumanController as HumanController
import assets.Model.HumanModel as HM

class MoneyController:
# TODO: transactions notifications
    def __init__(self):
        self.tansactionInProgress = False
        self.seed: HM.Human
        self.peer: HM.Human
        self.peerAPay: int
        pass

    def TransferMoney(self, to: int, fromVkID: int):
        hC = HumanController.HumanController()
        self.seed = hC.LoadHumanFromVkID(fromVkID)
        self.peerAPay = to
        self.tansactionInProgress = True

    def FixedMoneyTransaction(self, to: HM.Human, frm: HM.Human, amount: int):
        if frm.getMoney() >= amount:
            frm.RemoveMoney(amount)
            to.AddMoney(amount)
            frm.SaveToJsonFile()
            to.SaveToJsonFile()
            return True
        else:
            return False

    def ParseEvent(self, fromVkID, event):
        a = ''
        
        if event['text'].isdigit():
            transferAmount = int(event['text'])
            if transferAmount > 0:
                if self.seed.RemoveMoney(transferAmount):
                    self.peer = HumanController.HumanController().LoadHumanFromAPayID(self.peerAPay)
                    self.peer.AddMoney(transferAmount)
                    self.tansactionInProgress = False
                    return True
            else:
                self.tansactionInProgress = False
                return False
            
        else:
            self.tansactionInProgress = False
            return False
    