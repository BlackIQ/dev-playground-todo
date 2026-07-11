# FastAPI & SQLAlchemy
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

# Dependencies
from dependencies import get_db

# Task Model & Task Schema
from models.task import TaskModel
from schemas.task import Task, TaskRead

# Router
router = APIRouter(
    prefix="/tasks",
    tags=["Task"]
)


@router.get("", response_model=list[TaskRead])
async def all_tasks(db: Session = Depends(get_db)):
    return db.query(TaskModel).all()


@router.get("/{task_id}", response_model=TaskRead)
async def get_task(task_id: int, db: Session = Depends(get_db)):
    item = db.get(TaskModel, task_id)

    if not item:
        raise HTTPException(status_code=404, detail="Task not found")

    return item


@router.post("", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
async def create_task(task: Task, db: Session = Depends(get_db)):
    db_item = TaskModel(**task.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item


@router.put("/{task_id}", response_model=TaskRead)
async def update_task(task_id: int, task: Task, db: Session = Depends(get_db)):
    item = db.get(TaskModel, task_id)

    if not item:
        raise HTTPException(status_code=404, detail="Task not found")

    for key, value in task.model_dump().items():
        setattr(item, key, value)

    db.commit()
    db.refresh(item)

    return item


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    item = db.get(TaskModel, task_id)

    if not item:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(item)
    db.commit()

    return None
