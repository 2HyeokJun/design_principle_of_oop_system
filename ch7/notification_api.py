from abc import ABC, abstractmethod
from ch7.notification import Notification
from ch7.types import Medium, DispatchTime

class NotificationAPI(ABC):
    @abstractmethod
    def create_notification(self, message: str, supported_medium: list[Medium], times: list[DispatchTime]) -> Notification:
        pass

    def add_participant(self, notification_id: int, participant_email: str) -> None:
        pass

    def remove_participant(self, notification_id: int, participant_email: str) -> None:
        pass