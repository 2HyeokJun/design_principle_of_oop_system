class ImportResult:
    def __init__(self):
        self.result = []

    def added_new_employee(self, employee):
        self.result.append(employee)

    def updated_employee(self, employee):
        self.result.append(employee)
