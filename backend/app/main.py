from fastapi import FastAPI
from .database import conn
from .models import tasks
from sqlalchemy import insert, select

app = FastAPI()

@app.get("/api/tasks")
def get_tasks():
    result = conn.execute(select(tasks)).fetchall()
    return [dict(row._mapping) for row in result]

@app.post("/api/tasks")
def add_task(title: str):
    result = conn.execute(insert(tasks).values(title=title, status="todo").returning(tasks))
    conn.commit()
    return dict(result.fetchone()._mapping)
