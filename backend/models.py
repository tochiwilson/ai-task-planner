from pydantic import BaseModel
from typing import Optional

class Task(BaseModel):
    title: str
    description: str
    priority: str | None = None

class UpdateTask(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
