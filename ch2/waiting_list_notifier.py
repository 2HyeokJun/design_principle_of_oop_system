class WaitingListNotifier:
    def __init__(self, emailer):
        self.emailer = emailer  # 새 클래스는 Emailer에 의존한다.

    def notify(self, offering):  # 알림 로직은 이제 새로운 클래스 안에 위치한다.
        employees = offering.get_waiting_list()
        for employee in employees:
            self.emailer.send_waiting_list_email(offering, employee)
