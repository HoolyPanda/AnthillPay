import vk_api
from vk_api import bot_longpoll
import assets.View.mainView as mainView

token = open('./token.cred').read()

def main():
    try:
        session = vk_api.VkApi(token= token)
        lps = bot_longpoll.VkBotLongPoll(session, 172301854)
        threads = []
        userIds = []
        for event in bot_longpoll.VkBotLongPoll.listen(lps):
            rawEvent = event.raw
            userId = rawEvent['object']['from_id']
            if userId not in userIds:
                # TODO rewrite mainView in single thread
                mV = mainView.mainView(session, userId, event= event)
                # mv = mainView.mainView()
                mV.start()
                mV.join()
                threads.append(mV)
                userIds.append(userId)
            # mainView.main()
            pass
    except Exception as e:
        print(str(e))
        quit

main()