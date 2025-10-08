class BotMessage:
    def __init__(self, user_id: int, msg: str):
        self.user_id = user_id
        self.msg = msg
