from ch4.message import Message
from ch4.user_preferences import UserPreferences


class EmailSender:
    def __init__(self, user_pref: UserPreferences):
        self.user_pref = user_pref

    def is_user_prefer_to_send_via_email(self, email):
        return self.user_pref.send_via_email(email)

    def send_message(self, message: Message):
        return message
