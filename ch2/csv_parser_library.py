from enum import Enum


class CSVParserLibrary:
    class Mode(Enum):
        IGNORE_ERRORS = "ignore_errors"

    def __init__(self):
        self.mode = None
        self.object_type = None

    def set_mode(self, mode):
        self.mode = mode

    def set_object_type(self, object_type):
        self.object_type = object_type

    def parse(self, csv):
        return csv
