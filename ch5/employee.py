from ch5.trainings_taken import TrainingsTaken
from ch5.badge import Badge


class Employee:
    def __init__(self, trainings_taken: TrainingsTaken):
        self.trainings_taken = trainings_taken

    def get_trainings_taken(self):
        return self.trainings_taken

    def win_badge(self, badge: Badge):
        pass
