from ch2.employee import Employee
from ch2.updated_offering import UpdatedOffering


class Offering:

    def __init__(self, employee: Employee, updated_offering: UpdatedOffering):
        self.employee = employee
        self.updated_offering = updated_offering

    def is_date_updated(self):
        return True

    def is_description_updated(self):
        return False

    def is_import_info_updated(self):
        return self.is_date_updated() or self.is_description_updated()

    def should_receive_an_email(self):
        """
        직원들은 이메일을 받도록 동의한 경우나
        중요한 변경된 경우 이메일을 받아야 한다
        """
        is_import_info_was_updated = self.is_import_info_updated()
        is_employee_wantes_updates = self.employee.wants_any_email_updates()

        return is_import_info_was_updated or is_employee_wantes_updates

    def update(self):
        if self.should_receive_an_email():
            return False
        else:
            return True
