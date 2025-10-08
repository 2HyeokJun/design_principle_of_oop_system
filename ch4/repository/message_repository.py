class MessageRepository:
    def __init__(self):
        self.messages_to_be_sent = []

    def get_messages_to_be_sent(self) -> list:
        return self.messages_to_be_sent
