"""
누군가 등록을 취소했을 때 대기자 명단에 있는 모든 직원에게 이메일을 보내는 기능 구현
"""


class UnenrollEmployeeFromOfferingService:
    def __init__(self, emailer, offerings):
        self.emailer = emailer
        self.offerings = offerings

    def unenroll(self, enrollment_id):
        offering = self.offerings.get_offering_from(enrollment_id)
        # 전체 워크플로우에서 등록 취소 프로세스의 끝에 대기자 명단 알림 단계를 추가한다.
        self.notify_waiting_list(offering)

    # 알림 로직을 구현한다.
    def notify_waiting_list(self, offering):
        employees = offering.get_waiting_list()
        for employee in employees:
            self.emailer.send_waiting_list_email(offering, employee)
