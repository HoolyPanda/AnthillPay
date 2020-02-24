import os
import assets.Model.HumanModel


class RegistrationController:
    def CheckRegistration(self, id: int):
        if os.path.exists('./DB/' + str(id) + '.json'):
            return True
        else:
            return False
    
    
