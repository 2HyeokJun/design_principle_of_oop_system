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


class BadgeRuleFactory(ABC):
    @abstractmethod
    def create_rules(self) -> list[BadgeRule]:
        pass


class BadgeForTrainings(BadgeRule):
    def __init__(self, trainings: list[str], badge_to_give: Badge):
        self.trainings = trainings
        self._badge_to_give = badge_to_give

    def give(self, employee: Employee) -> bool:
        trainings_taken = employee.get_trainings_taken()
        # 모든 교육 과정을 이수했으면 True, 그렇지 않으면 False를 반환한다.
        for training in self.trainings:
            if not trainings_taken.has(training):
                return False
        return True

    # 수여할 배지를 반환한다.
    def badge_to_give(self) -> Badge:
        return self._badge_to_give


quality_hero = BadgeForTrainings(
    trainings=["TESTING", "CODE_QUALITY"], badge_to_give=Badge.QUALITY_HERO
)

security_cop = BadgeForTrainings(
    trainings=["SECURITY_101", "SECURITY_FOR_MOBILE_DEVS"],
    badge_to_give=Badge.SECURITY_COP,
)


class BadgeForTrainingsFactory(BadgeRuleFactory):
    def __init__(self):
        pass

    def create_rules(self) -> list[BadgeRule]:
        return [quality_hero, security_cop]


class BadgeForQuantity(BadgeRule):
    def __init__(self, quantity: int, badge_to_give: Badge):
        self.quantity = quantity
        self._badge_to_give = badge_to_give

    def give(self, employee: Employee) -> bool:
        trainings_taken: TrainingsTaken = employee.get_trainings_taken()
        return trainings_taken.total_trainings() >= self.quantity

    def badge_to_give(self) -> Badge:
        return self._badge_to_give


five_trainings = BadgeForQuantity(5, Badge.FIVE_TRAININGS)
ten_trainings = BadgeForQuantity(10, Badge.TEN_TRAININGS)


class BadgeForQuantitysFactory(BadgeRuleFactory):
    def __init__(self):
        pass

    def create_rules(self) -> list[BadgeRule]:
        return [five_trainings, ten_trainings]
