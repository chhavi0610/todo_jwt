from database import create_table, get_connection

from fastapi import FastAPI

from pydantic import BaseModel
app = FastAPI()

class Todo(BaseModel):
    title:str

create_table()
@app.get("/")
async def home():
    return {"status":"ok"}      

@app.post("/todo")
async def add_todo(todo: Todo):
    conn = get_connection()
    c = conn.cursor()
    c.execute("INSERT INTO jar (title) VALUES (?)", (todo.title,))
    conn.commit()
    conn.close()
    return{"message":"todo added"}

@app.get("/todo")
async def get_todos():
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM demo")
    rows = c.fetchall()
    conn.close()

    return[
        {"id": r[0], "title": r[1]}
        for r in rows
    ]


@app.get("/task")
async def get_task():
    conn=get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM demo")
    result = c.fetchall()
    conn.close()
    return[
        {"id": r[0], "title":r[1]}
        for r in result
    ]

@app.delete("/delete/{id}")
async def delete_entry(id: str):
    
    conn = get_connection()
    c = conn.cursor()
    c.execute("DELETE FROM task WHERE id = ?",(id,))
    if c.rowcount == 0:
        conn.commit()
        conn.close()
        return{"message":"deleted"}

@app.put("/update/{id}")
async def update_entry(id: str, todo: Todo):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE demo SET title = ? WHERE id = ?", (todo.title, id))
        conn.commit()
        conn.close()
        return {"message":"updated"}