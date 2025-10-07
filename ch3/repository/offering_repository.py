from typing import Optional
from ch3.offering import Offering

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
