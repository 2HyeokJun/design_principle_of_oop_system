from ch4.bot.bot import Bot
from ch4.user_directory import UserDirectory
from ch4.message import Message


class MessageBot:
    def __init__(self, bot: Bot, user_directory: UserDirectory):
        self.bot = bot
        self.user_directory = user_directory

    def send(self, msg: Message):
        user_id = self.user_directory.get_account(msg.get_email())
        self.bot.send_private_message(user_id, msg.get_body_in_markdown())
