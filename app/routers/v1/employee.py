from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated

from app.dependencies import get_employee_service
from app.schemas.employee import Employee, EmployeeOut
from app.services.employee import EmployeeService


employee_router = APIRouter(prefix='/employee', tags=['employee'])


@employee_router.post('/')
def create_employee(model: Employee,
                    employee_service: Annotated[EmployeeService, Depends(get_employee_service)]):
    """
    Create a new item in the DynamoDB database with the information below:

    - **name**: each item must have a name
    - **salary**: each item must have a salary
    """
    return employee_service.create_employee(model)


@employee_router.delete('/{employee_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_employee(employee_id: str,
                    employee_service: Annotated[EmployeeService, Depends(get_employee_service)]):
    """
    Delete an item with the given ID from the DynamoDB database.
    """
    return employee_service.delete_employee(employee_id)


@employee_router.get('/', response_model=list[EmployeeOut])
def get_all(employee_service: Annotated[EmployeeService, Depends(get_employee_service)]) \
        -> list[EmployeeOut]:
    """
    List all items in the DynamoDB database.
    """
    return employee_service.get_all()


@employee_router.get('/{employee_id}', response_model=EmployeeOut)
def get_employee(employee_id: str,
                 employee_service: Annotated[EmployeeService, Depends(get_employee_service)])\
        -> EmployeeOut:
    """
    Return item data with the given ID if it exists in the database.
    """
    try:
        return employee_service.get_employee(employee_id)
    except KeyError:
        raise HTTPException(status_code=400, detail='No employee found')


@employee_router.put('/')
def update_employee(model: Employee,
                    employee_service: Annotated[EmployeeService, Depends(get_employee_service)]):
    """
    Update existing item in the database.
    """
    return employee_service.update_employee(model)
