from ch4.bot.bot import Bot
from ch4.message import Message
from ch4.user_directory import UserDirectory
from ch4.repository.message_repository import MessageRepository


class MessageSender:
    def __init__(
        self, bot: Bot, user_directory: UserDirectory, repository: MessageRepository
    ):
        self.bot = bot
        self.user_directory = user_directory
        self.repository = repository

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
            # 메시지를 전송 완료로 표시한다.
            message_to_be_sent.mark_as_sent()
