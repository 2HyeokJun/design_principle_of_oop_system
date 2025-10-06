from employee import Employee
from import_result import ImportResult
from employee_import_csv_parser import EmployeeImportCSVParser


class ImportEmployeesService:
    def __init__(self, employees, parser: EmployeeImportCSVParser):
        self.employees = employees
        self.parser = parser

    def import_csv(self, csv):
        result = ImportResult()
        imported_list = self.parser.parse(csv)

        for employee in imported_list:
            maybe_an_employee = self.employees.find_by_email(employee["email"])
            # 직원이 존재하지 않는 경우 새로 생성한다
            if not maybe_an_employee:
                self.create_new_employee(employee, result)
            # 직원이 존재할 경우 직원 정보를 갱신한다
            else:
                self.update_employee(employee, result)

        return result

    def create_new_employee(self, employee, result):
        new_employee = Employee(
            employee["name"],
            employee["email"],
            employee["starting_date"],
            employee["role"],
        )
        self.employees.save(new_employee)
        result.added_new_employee(new_employee)

    def update_employee(self, employee, result):
        current_employee = Employee(
            employee["name"],
            employee["email"],
            employee["starting_date"],
            employee["role"],
        )

        self.employees.update(current_employee)
        result.updated_employee(current_employee)
