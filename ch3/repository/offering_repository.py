from typing import Optional
from ch3.offering import Offering
from ch3.enrollment import Enrollment

class OfferingRepository:
    def __init__(self):
        self.repository = []

    def find_by_id(self, id: int) -> Optional[Offering]:
        offering: Offering
        for offering in self.repository:
            if offering.id == id:
                return offering
        return None
    
    def add_employee(self, employee):
        self.repository.append(employee)

    def get_enrollment(self, employee_id: int) -> Optional[Enrollment]:
        offering: Offering
        for offering in self.repository:
            enrollments = offering.enrollments
            for enrollment in enrollments:
                if enrollment.employee.id == employee_id:
                    return enrollment
        return None

    
