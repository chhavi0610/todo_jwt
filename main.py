from fastapi import FastAPI
from database import create_table_task, create_table_user
from routes import router

app = FastAPI()
app.include_router(router)

try:
        create_table_user()
        create_table_task()
except Exception as e:
        print("DB not ready:", e)


@app.get("/")
def home():
    return {"status": "working"}
