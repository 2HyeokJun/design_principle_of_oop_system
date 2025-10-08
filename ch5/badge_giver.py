from ch5.employee import Employee
from ch5.trainings_taken import TrainingsTaken
from ch5.badge_rule import BadgeRule


class BadgeGiver:
    def __init__(self, rules: list[BadgeRule]):
        self.rules = rules

    def give(self, employee: Employee):
        for rule in self.rules:
            if rule.give(employee):
                employee.win_badge(rule.badge_to_give())
