from ch4.bot.sdk.chatbot_v1 import ChatBotV1
from ch4.bot.sdk.bot_message import BotMessage
from ch4.bot.bot import Bot


class SDKBot(Bot):
    def __init__(self):
        super().__init__()

    def send_private_message(self, id, message):
        chatbot = ChatBotV1()
        message = BotMessage(user_id=id, msg=message)
        chatbot.write_message(message=message)
