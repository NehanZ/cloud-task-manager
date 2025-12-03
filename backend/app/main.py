import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import conn
from .models import tasks
from sqlalchemy import insert, select
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Cloud Task Manager API",
    description="A production-ready task management API",
    version="1.0.0"
)

# CORS configuration
allowed_origins = os.getenv("CORS_ORIGINS", "http://localhost:3000").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin.strip() for origin in allowed_origins],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/tasks")
def get_tasks():
    try:
        result = conn.execute(select(tasks)).fetchall()
        return [dict(row._mapping) for row in result]
    except Exception as e:
        return {"error": "Failed to fetch tasks"}, 500

@app.get("/health")
def health_check():
    """Health check endpoint for AWS load balancer"""
    return {"status": "healthy", "environment": os.getenv("NODE_ENV", "development")}

@app.get("/")
def root():
    """Root endpoint"""
    return {"message": "Cloud Task Manager API", "status": "running"}

@app.post("/api/tasks")
def add_task(title: str):
    if not title or not title.strip():
        return {"error": "Title is required"}, 400
    
    try:
        result = conn.execute(insert(tasks).values(title=title.strip(), status="todo").returning(tasks))
        conn.commit()
        return dict(result.fetchone()._mapping)
    except Exception as e:
        conn.rollback()
        return {"error": "Failed to create task"}, 500
