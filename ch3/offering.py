"""
Offering 클래스에는 날짜, 교육 과정에 참석하는 직원 목록, 최대 참석자 수, 
텍스트 필드(관리자가 강의실 위치, 줌 링크 등의 정보를 입력할 수 있음)가 있다.
"""
from ch3.employee import Employee
from ch3.training import Training


class Offering:
    def __init__(self, id, training: Training, date: str, employees: list, max_number_of_attendees: int, available_spots: int):
        self.id = id
        self.training = training
        self.date = date
        self.employees = employees
        self.max_number_of_attendees = max_number_of_attendees
        self.available_spots = available_spots

    def get_employees(self) -> list:
        return self.employees
    
    def get_available_spots(self) -> int:
        return self.available_spots
    
    def set_available_spots(self, available_spots: int) -> None:
        self.available_spots = available_spots
    

        