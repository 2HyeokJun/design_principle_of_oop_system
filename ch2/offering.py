from ch2.employee import Employee
from ch2.updated_offering import UpdatedOffering


class Offering:

    def __init__(self, employee: Employee, updated_offering: UpdatedOffering):
        self.employee = employee
        self.updated_offering = updated_offering

    def update(self):
        if (
            self.employee.wants_any_email_updates()
            or self.updated_offering.is_date_updated()
            or self.updated_offering.is_description_updated()
        ):
            return False
        else:
            return True
