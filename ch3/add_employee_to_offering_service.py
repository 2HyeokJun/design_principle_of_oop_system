from ch3.repository.offering_repository import OfferingRepository
from ch3.repository.employee_repository import EmployeeRepository
from ch3. validator import AddEmployeeToOfferingValidator

class AddEmployeeToOfferingService:
    def __init__(self, offering_repo: OfferingRepository, employee_repo: EmployeeRepository, validator: AddEmployeeToOfferingValidator):
        self.offerings = offering_repo
        self.employees = employee_repo
        self.validator = validator

    def add_employee(self, offering_id: int, employee_id: int):
        offering = self.offerings.find_by_id(offering_id)
        employee = self.employees.find_by_id(employee_id)

        # 오퍼링과 직원의 id가 유효한지 검사한다.
        if not offering or not employee:
            raise ValueError("offering and employee ids should be valid")
        
        # validator를 호출해 비즈니스 측면에서 요청이 유효한지 확인한다.
        validation = self.validator.validate(offering, employee)
        # 검증에 실패하면 예외를 던져 클라이언트가 처리하게 한다.
        if not validation:
            raise ValueError()
        
        # 직원을 오퍼링에 추가한다.
        offering.enroll(employee)

