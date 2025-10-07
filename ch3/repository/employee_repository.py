class EmployeeRepository:
    def __init__(self):
        self.repository = []

    def find_by_id(self, id: int):
        for offering in self.repository:
            if offering == id:
                return offering
        return None