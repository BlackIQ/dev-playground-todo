# BaseSchema
from database.base import BaseSchema


# Task Schema
class Task(BaseSchema):
    title: str
    details: str
    priority: int
    is_completed: bool


class TaskRead(Task):
    id: int
