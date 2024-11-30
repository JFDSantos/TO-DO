from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    username: str
    password: str

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: bool = False  
    user_id: int 

    class Config:
        orm_mode = True 

class TaskCreate(TaskBase):
    pass 

class TaskUpdate(TaskBase):
    title: str
    description: Optional[str] = None
    status: bool = False
    
    class Config:
        orm_mode = True 

class TaskResponse(TaskBase):
    id: int  
    created_at: str  
    updated_at: str 

    class Config:
        orm_mode = True  
