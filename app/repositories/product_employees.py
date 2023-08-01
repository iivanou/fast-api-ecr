from botocore.exceptions import ClientError
from boto3.resources.base import ServiceResource


class ProductEmployeesRepository:

    TABLE_NAME = 'product-employees'

    def __init__(self, db: ServiceResource) -> None:
        self._db = db

    def create(self, employee: dict):
        table = self._db.Table(self.TABLE_NAME)
        return table.put_item(Item=employee)

    def delete(self, employee_id: str):
        table = self._db.Table(self.TABLE_NAME)
        return table.delete_item(Key={'employeeId': employee_id})

    def get_all(self):
        table = self._db.Table(self.TABLE_NAME)
        return table.scan().get('Items', [])

    def get(self, employee_id: str):
        try:
            table = self._db.Table(self.TABLE_NAME)
            return table.get_item(Key={'employeeId': employee_id}).get('Item')
        except ClientError as err:
            raise ValueError(err.response['Error']['Message'])

    def update(self, employee: dict):
        table = self._db.Table(self.TABLE_NAME)
        response = table.update_item(
            Key={'employeeId': employee.get('employeeId')},
            UpdateExpression="""
                set
                    #nm=:name,
                    salary=:salary
            """,
            ExpressionAttributeValues={
                ':name': employee.get('name'),
                ':salary': employee.get('salary')
            },
            ExpressionAttributeNames={
                "#nm": "name"  # because "name" is a reserved word
            }
        )
        return response
