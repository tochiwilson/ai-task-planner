from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["ai_task_db"]
tasks_collection = db["tasks"]
