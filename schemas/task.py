# Enum
from enum import IntEnum

# BaseSchema
from database.base import BaseSchema


# Enum of Task priority
class TaskPriority(IntEnum):
    VERY_LOW = 1
    LOW = 2
    MEDIUM = 3
    HIGH = 4
    VERY_HIGH = 5


# Task Schema
class Task(BaseSchema):
    title: str
    details: str
    priority: TaskPriority
    is_completed: bool


class TaskRead(Task):
    id: int
