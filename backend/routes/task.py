from fastapi import APIRouter, HTTPException
from bson import ObjectId
from models import Task, UpdateTask

from db import tasks_collection

router = APIRouter()

# POST /task
@router.post("/task")
def create_task(task: Task):
    if task.title.strip() == "":
        raise HTTPException(status_code=400, detail="Title Cannot Be Empty")
    
    if task.description.strip() == "":
        raise HTTPException(status_code=400, detail="Description Cannot Be Empty")
    
    task_dict = task.model_dump()
    result = tasks_collection.insert_one(task_dict)
    return {"inserted_id": str(result.inserted_id)}

# GET /taks
@router.get("/task")
def get_all_tasks():
    tasks_cursor = tasks_collection.find()

    tasks = []
    for task in tasks_cursor:
        task["_id"] = str(task["_id"])
        tasks.append(task)

    return tasks

# GET /task/id
@router.get("/task/{task_id}")
def get_task(task_id: str):
    try:
        obj_id = ObjectId(task_id)
    except:
        raise HTTPException(status_code=400, detail="Invalid Task ID")

    task = tasks_collection.find_one({"_id": obj_id})

    if not task:
        raise HTTPException(status_code=404, detail="Task Not Found")

    task["_id"] = str(task["_id"])

    return task

# PUT /task/id
@router.put("/task/{task_id}")
def update_task(task_id: str, task_update: UpdateTask):
    try:
        obj_id = ObjectId(task_id)
    except:
        raise HTTPException(status_code=400, detail="Invalid Task ID")

    update_data = {k: v for k, v in task_update.model_dump().items() if v is not None}

    if not update_data:
        raise HTTPException(status_code=400, detail="No Fields To Update")

    result = tasks_collection.update_one({"_id": obj_id}, {"$set": update_data})

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Task Not Found")

    return {"status": "succes", "updated_count": result.modified_count}

# DELETE /task/id
@router.delete("/task/{task_id}")
def delete_task(task_id: str):
    try:
        obj_id = ObjectId(task_id)
    except:
        raise HTTPException(status_code=400, detail="Invalid Task ID")

    result = tasks_collection.delete_one({"_id": obj_id})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Task Not Found")

    return {"status": "success", "deleted_count": result.deleted_count}
