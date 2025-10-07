import random
from ch3.employee import Employee
from ch3.training import Training

class TrainingRepository:
    def __init__(self):
        self.repository = []

    def count_participations(self, employee: Employee, training: Training) -> int:
        return random.randint(0, 5)