from sqlalchemy import Table, Column, Integer, String
from .database import meta, engine

tasks = Table(
    "tasks",
    meta,
    Column("id", Integer, primary_key=True),
    Column("title", String(255)),
    Column("status", String(50), default="todo"),
)

meta.create_all(engine)
