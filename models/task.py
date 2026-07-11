# SQLAlchemy DataTypes
from sqlalchemy import Column, Integer, Boolean, String

# BaseModel
from database.base import Base


# Task Model
class TaskModel(Base):
    __tablename__ = "tasks"  # Table name

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    details = Column(String, nullable=False)
    priority = Column(Integer, nullable=False)
    is_completed = Column(Boolean, nullable=False)
