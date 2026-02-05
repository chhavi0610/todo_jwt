from fastapi import FastAPI
from database import create_table_task, create_table_user
from routes import router

app = FastAPI()
app.include_router(router)

@app.on_event("startup")
def startup_event():
    create_table_user()
    create_table_task()


@app.get("/")
def home():
    return {"status": "working"}
