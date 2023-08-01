from uuid import uuid4

from app.repositories.product_employees import ProductEmployeesRepository
from app.schemas.employee import Employee


class EmployeeService:

    def __init__(self, table: ProductEmployeesRepository):
        self._table = table

    def create_employee(self, model: Employee):
        model.employeeId = str(uuid4())
        return self._table.create(model.dict())

    def delete_employee(self, employee_id: str):
        return self._table.delete(employee_id)

    def get_all(self):
        return self._table.get_all()

    def get_employee(self, uid: str):
        return self._table.get(uid)

    def update_employee(self, model: Employee):
        return self._table.update(model.dict())
