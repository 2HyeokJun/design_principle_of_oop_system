from ch4.bot.sdk.chatbot_v1 import ChatBotV1
from ch4.bot.sdk.bot_message import BotMessage
from ch4.bot.bot import Bot


class SDKBot(Bot):
    def __init__(self):
        super().__init__()

    def send_private_message(self, id, message):
        try:
            chatbot = ChatBotV1()
            message = BotMessage(user_id=id, msg=message)
            chatbot.write_message(message=message)
        except IOError as e:    # 도메인에 초점을 맞춘 예외를 던지고 저수준 세부 사항을 로그에 남긴다.
            print("ERROR:", e)
            raise BotException(id, message)
            

class BotException(ValueError): # BotException은 도메인에 초점을 맞춘 예외이다.
    pass