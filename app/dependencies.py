from config import get_app_settings
from connections.db import db_connection
from services.employee import EmployeeService

from repositories.product_employees import ProductEmployeesRepository


def get_employee_service():
    db = db_connection(get_app_settings())
    repo = ProductEmployeesRepository(db)
    employee_service = EmployeeService(repo)
    return employee_service
