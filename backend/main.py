from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.task import router as task_router

app = FastAPI()
app.include_router(task_router)

origins = ["http://localhost:3000", "http://127.0.0.1:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"Hello": "World"}
