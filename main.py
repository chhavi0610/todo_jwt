import os
from fastapi import FastAPI
from database import create_table_user, create_table_task
from routes import router

app = FastAPI()
app.include_router(router)



@app.get("/")
def home():
    return {"status": "working"}
