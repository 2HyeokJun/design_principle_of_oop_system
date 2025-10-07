from ch3.repository.training_repository import TrainingRepository
from ch3.offering import Offering
from ch3.employee import Employee

class AddEmployeeToOfferingValidator:
    def __init__(self, trainings: TrainingRepository):
        self.validation_result = []
        self.trainings = trainings

    def validate(self, offering: Offering, employee: Employee):
        # 오퍼링에 빈 자리가 있어야 한다.
        if not offering.has_available_spots():
            self.validation_result.add("Offering has no available spots")

        # 참가자가 이 과정을 3번 이상 수강했으면 안 된다.
        times_participant_took_the_training = self.trainings.count_participations(employee, offering.get_training())
        if times_participant_took_the_training >= 3:
            self.validation_result.add("Participant can't ttake the training again")

        # 참가자가 이 오퍼링에 이미 등록되어 있으면 안 된다.
        if offering.is_employee_registered():
            self.validation_result.add("Participant already in this offering")

        return self.validation_result