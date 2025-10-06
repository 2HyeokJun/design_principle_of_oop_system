"""
누군가 등록을 취소했을 때 대기자 명단에 있는 모든 직원에게 이메일을 보내는 기능 구현
"""

from ch2.waiting_list_notifier import WaitingListNotifier


class UnenrollEmployeeFromOfferingService:
    # 서비스는 이제 새로운 WaitingListNotifier에 의존한다.
    def __init__(self, offerings, notifier: WaitingListNotifier):
        self.offerings = offerings
        self.notifier = notifier

    def unenroll(self, enrollment_id):
        offering = self.offerings.get_offering_from(enrollment_id)
        # notifier 클래스를 호출한다.
        self.notifier.notify(offering)
