from fastapi import FastAPI
from database import create_table_task, create_table_user
from routes import router

app = FastAPI()
app.include_router(router)

@app.on_event("startup")
def startup_event():
    try:
        create_table_user()
    except Exception as e:
        print("DB not ready:", e)


@app.get("/")
def home():
    return {"status": "working"}
