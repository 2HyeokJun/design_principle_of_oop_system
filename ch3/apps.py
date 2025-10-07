from ch3.offering import Offering
from ch3.employee import Employee
from ch3.training import Training

def get_offering_from_database() -> Offering:
    offering = Offering(
        id=1,
        training=Training(),
        date="2025-10-07 21:37:00",
        employees=[],
        max_number_of_attendees=10,
        available_spots=3
    )
    return offering

def use_offering_entity():
    offering: Offering = get_offering_from_database()
    employee_that_wants_to_participate = Employee()

    # 현재 오퍼링에 빈 자리가 있는가?
    if offering.get_available_spots() > 0:
        offering.add_employee(employee_that_wants_to_participate)

if __name__ == "__main__":
    use_offering_entity()