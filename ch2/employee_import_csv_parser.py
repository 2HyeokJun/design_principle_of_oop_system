from csv_parser_library import CSVParserLibrary
from ch1.types import EmployeeParsedData


class EmployeeImportCSVParser:
    def parse(self, csv):
        csv_parser = CSVParserLibrary()
        csv_parser.set_mode(csv_parser.Mode.IGNORE_ERRORS)
        csv_parser.set_object_type(EmployeeParsedData)
        return csv_parser.parse(csv)
