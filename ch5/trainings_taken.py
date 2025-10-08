class TrainingsTaken:
    def __init__(self):
        self.trainings = []

    def has(self, training):
        for taken in self.trainings:
            if taken == training:
                return True
        return False

    def total_trainings(self):
        return len(self.trainings)

    def trainings_in_past_3months(self):
        result = 0
        for training in self.trainings:
            if training["date"] <= 7:
                result += 1

        return result
