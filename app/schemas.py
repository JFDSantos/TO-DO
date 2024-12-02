from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    password: str

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: bool = False  

    class Config:
        orm_mode = True 

class TaskCreate(TaskBase):
    pass 

class TaskUpdate(BaseModel):
    status: bool = False
    
    class Config:
        orm_mode = True 

class TaskResponse(TaskBase):
    id: int  
    created_at: datetime  
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
