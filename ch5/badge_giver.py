from ch5.employee import Employee
from ch5.trainings_taken import TrainingsTaken
from ch5.badge import Badge


class BadgeGiver:
    def __init__(self):
        pass

    def give(self, employee: Employee):
        BadgesForTrainings().give(employee)
        BadgesForQuantity().give(employee)


class BadgesForTrainings:
    def __init__(self):
        pass

    def give(self, employee: Employee):
        trainings_taken: TrainingsTaken = employee.get_trainings_taken()
        # 품질 관련 교육을 받은 경우 배지를 받는다.
        if trainings_taken.has("TESTING") and trainings_taken.has("CODE_QUALITY"):
            self.assign(employee, Badge.QUALITY_HERO)
        # 보안 관련 교육을 모두 들으면 배지를 받는다.
        if trainings_taken.has("SECURITY_101") and trainings_taken.has(
            "SECUITY_FOR_MOBILE_DEVS"
        ):
            self.assign(employee, Badge.SECURITY_COP)
        # ...다른 배지 수여 규칙들...

    def assign(self, employee: Employee, badge: Badge):
        employee.win_badge(badge)


class BadgesForQuantity:
    def __init__(self):
        pass

    def give(self, employee: Employee) -> None:
        trainings_taken: TrainingsTaken = employee.get_trainings_taken()
        if trainings_taken.total_trainings() >= 5:
            self.assign(employee, Badge.FIVE_TRAININGS)
        if trainings_taken.total_trainings() >= 10:
            self.assign(employee, Badge.TEN_TRAININGS)
        if trainings_taken.trainings_in_past_3months() >= 3:
            self.assign(employee, Badge.ON_FIRE)

    def assign(self, employee: Employee, badge: Badge):
        employee.win_badge(badge)
