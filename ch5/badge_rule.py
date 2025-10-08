"""
구현을 개선하기 위한 첫 번째 단계느 추상화하려는 공통 동작을 식별하는 것이다.
여기서는 직원에게 배지를 수여해야 하는지를 결정하는 동작을 추상화할 것이다.
이를 위해 배지를 수여해야 하는지를 결정하는 모든 규칙을 일반적으로 표현하는 BadgeRule 인터페이스를 만들 수 있다.
"""

from abc import ABC, abstractmethod
from ch5.employee import Employee
from ch5.badge import Badge
from ch5.trainings_taken import TrainingsTaken


class BadgeRule(ABC):
    def __init__(self):
        pass

    # 직원이 배지를 받을 자격이 있는지를 결정한다.
    @abstractmethod
    def give(self, employee: Employee) -> None:
        pass

    # 수여할 배지를 반환한다.
    @abstractmethod
    def badge_to_give(self) -> Badge:
        pass


class QualityHero(BadgeRule):
    def __init__(self):
        super().__init__()

    def give(self, employee: Employee) -> bool:
        trainings_taken: TrainingsTaken = employee.get_trainings_taken()
        return trainings_taken.has("TESTING") and trainings_taken.has("CODE_QUALITY")

    def badge_to_give(self) -> Badge:
        return Badge.QUALITY_HERO


class SecurityCop(BadgeRule):
    def __init__(self):
        super().__init__()

    def give(self, employee: Employee) -> bool:
        trainings_taken: TrainingsTaken = employee.get_trainings_taken()
        return trainings_taken.has("SECURITY_101") and trainings_taken.has(
            "SECURITY_FOR_MOBILE_DEVS"
        )

    def badge_to_give(self) -> Badge:
        return Badge.SECURITY_COP


class FiveTrainings(BadgeRule):
    def __init__(self):
        super().__init__()

    def give(self, employee: Employee) -> bool:
        trainings_taken: TrainingsTaken = employee.get_trainings_taken()
        return trainings_taken.total_trainings() >= 5

    def badge_to_give(self) -> Badge:
        return Badge.SECURITY_COP
