import vk_api
from vk_api import bot_longpoll
import assets.View.mainView as mainView

token = open('./token.cred').read()

def main():
    try:
        session = vk_api.VkApi(token= token)
        lps = bot_longpoll.VkBotLongPoll(session, 192654141)
        views = []
        userIds = []
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
                # mV.ParseEvent(event)
            for view in views:
                if view.userId == userId:
                    if view.ParseEvent(event) == True:
                        views.remove(view)
                        userIds.remove(view.userId)
                break

            pass
    except Exception as e:
        print(str(e))
        quit

main()