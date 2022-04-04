from lib2to3.pytree import Base
from fastapi import FastAPI, status
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import uvicorn

engine = create_engine("sqlite:///todo.db")
Base = declarative_base()
Base.metadata.create_all(engine)

app = FastAPI()

@app.get("/")
async def root():
       return {"message": "Hello World!"}

@app.post("/todo", status_code=status.HTTP_201_CREATED)
def create_todo():
       return "create todo"

@app.get("/todo/{id}")
def read_todo(id: int):
       return "get todo with id"

@app.put("/todo/{id}")
def update_todo(id: int):
       return "update todo with id"

@app.delete("/todo/{id}")
def delete_todo(id: int):
       return "delete todo with id"

@app.get("/todo")
def read_todo_list():
       return "read todo list"


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.2", port=8000, reload=True, log_level="info")