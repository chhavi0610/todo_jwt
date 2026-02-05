from fastapi import FastAPI
from database import create_table_task, create_table_user
from routes import router

app = FastAPI()

create_table_user()
create_table_task()

app.include_router(router)

@app.get("/")
def home():
    return {"status": "ok"}
