
import assets.Model.HumanModel as HM
# from assets.Controller.HumanController import HumanController as HC
# import assets.Controller.HumanController as HC
# from assets.Controller.HumanController import HumanController


class MoneyController:
# TODO: transactions notifications
    def __init__(self):
        self.tansactionInProgress = False
        self.seed: HM.Human
        self.peer: HM.Human
        self.peerAPay: int
        pass

    def TransferMoney(self, to: HM.Human, fromUser: HM.Human):
        # TODO: transaction host name
        # hC = HC(None)
        self.seed = fromUser
        self.peer = to
        self.tansactionInProgress = True

    def FixedMoneyTransaction(self, to: HM.Human, frm: HM.Human, amount: int):
        if frm.getMoney() >= amount:
            if frm.id != to.id:
                frm.RemoveMoney(amount)
                frm.SaveToJsonFile()
                to.AddMoney(amount)
                to.SaveToJsonFile()
                return True
            else:
                return False
        else:
            return False

    def ParseEvent(self, fromVkID, event):
        a = ''
        
        if event['text'].isdigit():
            transferAmount = int(event['text'])
            if transferAmount > 0:

                if self.seed.id != self.peer.id and self.seed.RemoveMoney(transferAmount):
                    # self.peer = HC(None).LoadHumanFromAPayID(self.peerAPay)
                    self.peer.AddMoney(transferAmount)
                    self.tansactionInProgress = False
                    return True
            else:
                self.tansactionInProgress = False
                return False
            
        else:
            self.tansactionInProgress = False
            return False
    