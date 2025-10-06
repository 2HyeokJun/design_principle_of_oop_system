from csv_parser_library import CSVParserLibrary
from employee import Employee
from import_result import ImportResult
from ch1.types import EmployeeParsedData
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
            if maybe_an_employee.is_empty():
                new_employee = Employee()
                new_employee.set_name(employee["name"])
                new_employee.set_email(employee["email"])
                new_employee.set_starting_date(employee["starting_date"])
                new_employee.set_role(employee["role"])

                self.employees.save(new_employee)
                result.added_new_employee(new_employee)
            # 직원이 존재할 경우 직원 정보를 갱신한다
            else:
                current_employee = Employee()
                current_employee.set_name(employee["name"])
                current_employee.set_starting_date(employee["starting_date"])
                current_employee.set_role(employee["role"])

                self.employees.update(current_employee)
                result.updated_employee(current_employee)

        return result
