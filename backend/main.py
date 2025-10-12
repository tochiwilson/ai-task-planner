from pydantic import BaseModel
from fastapi import FastAPI

from db import tasks_collection

class Task(BaseModel):
    title: str
    description: str
    priority: str | None = None # optioneel
    
app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World"}

@app.post("/task")
def create_task(task: Task):
    task_dict = task.model_dump()
    result = tasks_collection.insert_one(task_dict)
    return {"inserted_id": str(result.inserted_id)}

@app.get("/task")
def get_all_tasks():
    tasks_cursor = tasks_collection.find()
    
    tasks = []
    for task in tasks_cursor:
        task["_id"] = str(task["_id"])
        tasks.append(task)
        
    return tasks
    