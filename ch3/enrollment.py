"""
Enrollment 엔터티는 직원, 등록 날짜, 등록 상태, 등록 취소를 한 경우 취소 날짜를 포함한다.
Enrollment 클래스는 등록에 대한 모든 정보를 저장한다. 또 등록을 취소하고 취소 날짜를 설정하는 cancel 메소드를 제공한다.
"""
from typing import Optional
from ch3.employee import Employee

class Enrollment:
    def __init__(self, employee: Employee, date_of_enrollment: str):
        self.employee = employee
        self.date_of_enrollment = date_of_enrollment
        self.status = True
        self.date_of_cancellation = None

    def cancel(self, date_of_cancellation: str):
        self.status = False
        self.date_of_cancellation = date_of_cancellation