from pydantic import BaseModel, Field


class Employee(BaseModel):
    employeeId: str = Field(str, example='e899ac6b-d0eb-4ec9-a48b-0f17cc769426')
    name: str = Field(str, example='HardSkill')
    salary: int = Field(int, example=[100, 100000])


class EmployeeOut(BaseModel):
    employeeId: str
    name: str
    salary: int
