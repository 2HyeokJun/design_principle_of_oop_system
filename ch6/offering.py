"""
Offering 클래스에는 날짜, 교육 과정에 참석하는 직원 목록, 최대 참석자 수, 
텍스트 필드(관리자가 강의실 위치, 줌 링크 등의 정보를 입력할 수 있음)가 있다.
"""
from typing import Optional
from datetime import datetime
from ch3.employee import Employee
from ch3.training import Training
from ch3.enrollment import Enrollment


class Offering:
    def __init__(self, id, training: Training, date: str, enrollments: list[Enrollment], max_number_of_attendees: int, available_spots: int):
        self.id = id
        self.training = training
        self.date = date
        self.enrollments = enrollments # 직원 리스트를 등록의 리스트로 변경한다.
        self.max_number_of_attendees = max_number_of_attendees
        self.available_spots = available_spots

    # 등록을 생성하고 오퍼링의 상태와 등록의 상태가 일관성 있게 한다.
    def enroll(self, employee: Employee):
        if self.available_spots == 0:
            raise ValueError
        # 직원을 오퍼링에 추가한다
        now = datetime.now()
        self.enrollments.append(Enrollment(employee, now))
        # 잔여 허용 인원을 하나 줄인다
        self.available_spots -= 1

    # 등록을 취소하고 전체 애그리게이트의 일관성을 보장한다.
    def cancel(self, employee: Employee):
        enrollment_to_cancel = self.find_enrollment_of(employee)
        if not enrollment_to_cancel:
            raise ValueError()
        
        now = datetime.now()
        enrollment_to_cancel.cancel(now)
        self.available_spots += 1

    def find_enrollment_of(self, employee: Employee) -> Optional[Enrollment]:
        for enrollment in self.enrollments:
            if enrollment == employee:
                return enrollment
        return None

    def get_available_spots(self) -> int:
        return self.available_spots
    
    def has_available_spots(self):
        return self.get_available_spots() > 0
    
    def get_training(self):
        return self.training
    
    def is_employee_registered(self, employee: Employee):
        for e in self.employees:
            if e == employee:
                return True
        return False

    

        