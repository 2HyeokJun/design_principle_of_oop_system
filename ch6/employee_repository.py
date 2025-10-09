from abc import ABC, abstractmethod
from ch6.employee import Employee
from ch6.cache import Cache

class EmployeeRepository(ABC):
    @abstractmethod
    def find_by_id(self, id: int) -> Employee:
        pass
    @abstractmethod
    def find_by_last_name(self, last_name: str) -> Employee:
        pass
    @abstractmethod
    def save(self, employee: Employee) -> None:
        pass

class PostgresEmployeeEmployee(EmployeeRepository):
    def __init__(self, cache: Cache):
        self.cache = cache
        self.session = ""
    def find_by_last_name(self, last_name):
        if not self.cache.contains(last_name):
            self.cache.add(last_name, self.session.create_query().set_parameter().to_set())
        return self.cache.get(last_name)