from ch3.repository.offering_repository import OfferingRepository
from ch3.enrollment import Enrollment
from datetime import datetime

class CancelEnrollmentService:
    def __init__(self, offerings: OfferingRepository):
        self.offerings = offerings

    def cancel(self, offering_id: int, employee_id: int):
        if not offering_id or not employee_id:
            raise ValueError()
        offering = self.offerings.find_by_id(offering_id)
        enrollment = self.offerings.get_enrollment(employee_id)
        if not enrollment:
            raise ValueError()
        
        now = datetime.now()
        enrollment.cancel(now)
        offering.increase_available_spots()