from fastapi import FastAPI

from routes.task import router as task_router
from db import tasks_collection

app = FastAPI()
app.include_router(task_router)

@app.get("/")
def root():
    return {"Hello": "World"}
