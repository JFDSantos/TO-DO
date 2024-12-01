from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime, timezone
from app.models import Task
from app.schemas import TaskCreate, TaskUpdate, TaskResponse
from app.routes.auth import get_current_user  # Função para autenticação
from app.database import SessionLocal

router = APIRouter(prefix="/tasks", tags=["Tasks"])

def my_dependency():
    session = SessionLocal()
    return session

# Criar uma tarefa
@router.post("/", response_model=TaskResponse, status_code=201)
async def create_task(
    task: TaskCreate,
    db: AsyncSession = Depends(my_dependency),
    current_user: dict = Depends(get_current_user)
):
    try:
        new_task = Task(**task.model_dump(), user_id=current_user.id, created_at=datetime.now(timezone.utc))
        db.add(new_task)
        await db.commit()
        await db.refresh(new_task)
        return new_task
    except SQLAlchemyError as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail="Error creating task.")

# Listar todas as tarefas do usuário logado
@router.get("/", response_model=list[TaskResponse])
async def get_tasks(
    db: AsyncSession = Depends(my_dependency),
    current_user: dict = Depends(get_current_user)
):
    try:
        query = select(Task).where(Task.user_id == current_user.id)
        result = await db.execute(query)
        tasks = result.scalars().all()
        return tasks
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Error fetching tasks.")

# Atualizar uma tarefa pelo ID
@router.put("/{task_id}", response_model=TaskResponse)
async def update_task(
    task_id: int,
    task: TaskUpdate,
    db: AsyncSession = Depends(my_dependency),
    current_user: dict = Depends(get_current_user)
):
    try:
        query = select(Task).where(Task.id == task_id, Task.user_id == current_user.id)
        result = await db.execute(query)
        task_db = result.scalar_one_or_none()

        if not task_db:
            raise HTTPException(status_code=404, detail="Task not found.")

        for key, value in task.dict(exclude_unset=True).items():
            setattr(task_db, key, value)
        task_db.updated_at = datetime.now(timezone.utc)

        await db.commit()
        await db.refresh(task_db)
        return task_db
    except SQLAlchemyError as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail="Error updating task.")

# Deletar uma tarefa pelo ID
@router.delete("/{task_id}", status_code=204)
async def delete_task(
    task_id: int,
    db: AsyncSession = Depends(my_dependency),
    current_user: dict = Depends(get_current_user)
):
    try:
        query = select(Task).where(Task.id == task_id, Task.user_id == current_user.id)
        result = await db.execute(query)
        task_db = result.scalar_one_or_none()

        if not task_db:
            raise HTTPException(status_code=404, detail="Task not found.")

        await db.delete(task_db)
        await db.commit()
        return {"detail": "Task deleted successfully."}
    except SQLAlchemyError:
        await db.rollback()
        raise HTTPException(status_code=500, detail="Error deleting task.")
