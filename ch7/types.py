from enum import Enum


class Medium(Enum):
    EMAIL = "EMAIL"
    CHAT = "CHAT"
    WHATSAPP = "WHATSAPP"


class DispatchTime(Enum):
    RIGHT_NOW = "RIGHT_NOW"
    ONE_WEEK_BEFORE = "ONE_WEEK_BEFORE"
    DAY_BEFORE = "DAY_BEFORE"
    ONE_HOUR_BEFORE = "ONE_HOUR_BEFORE"