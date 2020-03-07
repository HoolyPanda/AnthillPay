import vk_api
from vk_api import bot_longpoll
import threading
import assets.View.mainView as mainView

token = open('./token.cred').read()


views = []
userIds = []

def parseStuff(userId, event):
    for view in views:
        if view.userId == userId:
            if view.ParseEvent(event) == True:
                views.remove(view)
                userIds.remove(view.userId)
    

def main():
    try:
        session = vk_api.VkApi(token= token)
        lps = bot_longpoll.VkBotLongPoll(session, 192654141)
        for event in bot_longpoll.VkBotLongPoll.listen(lps):
            for view in views:
                if view.userId not in userIds:
                    userIds.append(view.userId)
            rawEvent = event.raw
            userId = rawEvent['object']['from_id']
            #
            mV = mainView.mainView(session, userId, event= event)
            if mV.userId not in userIds:
                views.append(mV)
                userIds.append(mV.userId)
                # mV.ParseEvent(event)
            a = threading.Thread(target= parseStuff, args= {event, userId,})
            a.start()
            # for view in views:
            #     if view.userId == userId:
            #         if view.ParseEvent(event) == True:
            #             views.remove(view)
            #             userIds.remove(view.userId)
            #     break

            pass
    except Exception as e:
        print(str(e))
        main()

main()