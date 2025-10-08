class UserDirectory:
    def __init__(self):
        self.directory = []

    def get_account(self, email):
        for dir in self.directory:
            if dir.email == email:
                return dir.id
        return None
