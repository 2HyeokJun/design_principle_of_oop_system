class Message:
    def __init__(self, email, body):
        self.email = email
        self.body = body
        self.sent = False

    def get_email(self):
        return self.email

    def get_body_in_markdown(self):
        return self.body

    def mark_as_sent(self):
        self.sent = True
