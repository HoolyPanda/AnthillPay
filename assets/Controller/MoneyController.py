import assets.Controller.HumanController as HumanController
import assets.Model.HumanModel as HM

class MoneyController:

    def __init__(self):
        self.tansactionInProgress = False
        self.seed: HM.Human
        self.peer: HM.Human
        self.peerVkId: int
        pass

    def TransferMoney(self, to: int, fromVkID: int):
        hC = HumanController.HumanController()
        self.seed = hC.LoadHumanFromVkID(fromVkID)
        self.peerVkId = fromVkID
        self.tansactionInProgress = True

    def ParseEvent(self, fromVkID, event):
        a = ''
        
        if event['text'].isdigit():
            transferAmount = int(event['text'])
            if transferAmount > 0:
                if self.seed.RemoveMoney(transferAmount):
                    self.peer = HumanController.HumanController().LoadHumanFromVkID(self.peerVkId)
                    self.peer.AddMoney(transferAmount)
                    self.tansactionInProgress = False
                    return True
            else:
                self.tansactionInProgress = False
                return False
            
        else:
            self.tansactionInProgress = False
            return False
    