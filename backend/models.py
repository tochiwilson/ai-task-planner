from pydantic import BaseModel, Field
from typing import Optional, Literal

PriorityType = Literal['low', 'medium', 'high']

class Task(BaseModel):
    title: str = Field(..., description="Title of the task")
    description: str = Field(..., description="Description of the task")
    priority: Optional[PriorityType] = None

class UpdateTask(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[PriorityType] = None
