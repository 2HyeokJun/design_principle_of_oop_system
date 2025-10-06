class Employee:
    def __init__(self):
        self.name = None
        self.email = None
        self.starting_date = None
        self.role = None

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_starting_date(self):
        return self.starting_date

    def get_role(self):
        return self.role

    def set_name(self, name):
        self.name = name

    def set_email(self, email):
        self.email = email

    def set_starting_date(self, starting_date):
        self.starting_date = starting_date

    def set_role(self, role):
        self.role = role
