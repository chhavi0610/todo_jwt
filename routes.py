from fastapi import APIRouter, HTTPException
from database import connection
from auth import hash_password, check_password, create_token
from schema import ReisterUser, LoginUser, AddTask
router = APIRouter()


@router.post("/register")
async def register(reg_usr: ReisterUser):
    conn = connection()
    if conn is None:
        print("db connection error")
    cur = conn.cursor()

    cur.execute( "INSERT INTO users (name, email,password) VALUES (%s,%s, %s)",
                (reg_usr.name,reg_usr.email, hash_password(reg_usr.password)))
    conn.commit()
    cur.close()
    conn.close()

    return {"message": "user registered"}

@router.post("/login")
async def login(user: LoginUser):
    conn = connection()
    if conn is None:
        print("db connection error")
    cur = conn.cursor()
    cur.execute( "SELECT id, hashed_password FROM users WHERE email=%s",(user.email,))
    u = cur.fetchone()

    if not u:
        raise HTTPException(401, "user not found")
    
    if not check_password(user.password, u[1]):
        raise HTTPException(401, "wrong password")
    
    token = create_token(user.email)

    cur.close()
    conn.close()

    return {"token": token}


@router.post("/todo")
async def add_task(todo: AddTask):
    conn = connection()
    if conn is None:
        print("db connection error")
    cur = conn.cursor()

    cur.execute("INSERT INTO tasks(title) VALUES (%s)",(todo.title,))
    conn.commit()
    cur.close()
    conn.close()

    return {"message": "todo added"}


@router.get("/todo")
def get_tasks():

    conn = connection()
    if conn is None:
        print("db connection error")
    cur = conn.cursor()

    cur.execute("SELECT id, title FROM tasks")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    result = []
    for r in rows:
        result.append({
            "id": r[0],
            "title": r[1]
        })

    return result


@router.put("/todo/{id}")
async def update_task(id: int, todo:AddTask):

    conn = connection()
    if conn is None:
        print("db connection error")
    cur = conn.cursor()

    cur.execute(
        "UPDATE tasks SET title=%s WHERE id=%s",
        (todo.title, id)
    )

    conn.commit()
    cur.close()
    conn.close()

    return {"message": "task updated"}


@router.delete("/todo/{id}")
def delete_todo(id: int):

    conn = connection()
    if conn is None:
        print("db connection error")    
        
    cur = conn.cursor()

    cur.execute("DELETE FROM tasks WHERE id=%s", (id,))
    conn.commit()

    cur.close()
    conn.close()

    return {"message": "task deleted"}
