from ch4.message import Message
from ch4.message_bot import MessageBot
from ch4.email_sender import EmailSender
from ch4.repository.message_repository import MessageRepository


class MessageSender:
    def __init__(
        self,
        message_bot: MessageBot,
        repository: MessageRepository,
        email_sender: EmailSender,
    ):
        self.message_bot = message_bot
        self.repository = repository
        self.email_sender = email_sender

    def send_messages(self) -> None:
        messages_to_be_sent = self.repository.get_messages_to_be_sent()
        message_to_be_sent: Message
        # 송신해야 하는 모든 메시지에 대해
        for message_to_be_sent in messages_to_be_sent:
            self.message_bot.send(message_to_be_sent)
            if self.email_sender.is_user_prefer_to_send_via_email(
                message_to_be_sent.get_email()
            ):
                self.email_sender.send_message(message_to_be_sent)

            # 메시지를 전송 완료로 표시한다.
            message_to_be_sent.mark_as_sent()
