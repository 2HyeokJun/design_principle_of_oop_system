from ch4.bot.bot import Bot
from ch4.message import Message
from ch4.user_directory import UserDirectory
from ch4.email_sender import EmailSender
from ch4.user_preferences import UserPreferences
from ch4.repository.message_repository import MessageRepository


class MessageSender:
    def __init__(
        self,
        bot: Bot,
        user_directory: UserDirectory,
        repository: MessageRepository,
        email_sender: EmailSender,
        user_prefs: UserPreferences,
    ):
        self.bot = bot
        self.user_directory = user_directory
        self.repository = repository
        # 새로운 의존성을 추가한다.
        self.email_sender = email_sender
        self.user_prefs = user_prefs

    def send_messages(self) -> None:
        messages_to_be_sent = self.repository.get_messages_to_be_sent()
        message_to_be_sent: Message
        # 송신해야 하는 모든 메시지에 대해
        for message_to_be_sent in messages_to_be_sent:
            # 이메일에서 사용자의 id를 가져온다.
            user_id = self.user_directory.get_account(message_to_be_sent.get_email())
            # 봇을 통해 메시지를 전송한다.
            self.bot.send_private_message(
                id=user_id,
                message=message_to_be_sent.get_body_in_markdown(),
            )
            # 두가지 새 의존성을 사용해 메시지 복사본을 사용자에게 이메일로 보낼지 결정한다.
            if self.user_prefs.send_via_email(message_to_be_sent.get_email()):
                self.email_sender.send_message(message_to_be_sent)

            # 메시지를 전송 완료로 표시한다.
            message_to_be_sent.mark_as_sent()
