import assets.Controller.APiController as APiController
import vk_api
from vk_api import bot_longpoll
import threading
import assets.View.mainView as mainView
import json

token = open('./token.cred').read()


views = []
userIds = []
apiController: APiController.APIController


def parseStuff(session, userId, event):
    print(json.dumps(event.raw['object']))
    if userId > 0:
        for view in views:
            if view.userId == userId:
                if view.ParseEvent(event) == True:
                    views.remove(view)
                    userIds.remove(view.userId)
                break    
            else:
                pass
    else:
        apiController = APiController.APIController(session)
        apiController.ParseEvent(event)
        pass

def main():
    try:
        session = vk_api.VkApi(token= token)
        lps = bot_longpoll.VkBotLongPoll(session, 192654141)
        # apiController = APiController.APIController(session) 
        
        apiController = APiController.APIController(session) 
        for event in bot_longpoll.VkBotLongPoll.listen(lps):
            for view in views:
                if view.userId not in userIds:
                    userIds.append(view.userId)
            rawEvent = event.raw
            userId = rawEvent['object']['from_id']
            #
            if userId > 0:
                mV = mainView.mainView(session, userId, event= event)
                if mV.userId not in userIds:
                    views.append(mV)
                    userIds.append(mV.userId)
            a = threading.Thread(target= parseStuff, kwargs= {'event':event, "userId":userId, 'session': session})
            a.start()
            pass
    except Exception as e:
        print(str(e))
        main()

main()