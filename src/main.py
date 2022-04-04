from fastapi import FastAPI, status, HTTPException
from db.database import Base, engine
from sqlalchemy.orm import Session
import uvicorn

import models.models as models
import schemas.schemas as schemas

app = FastAPI()

#create database
Base.metadata.create_all(engine)

@app.get("/")
async def root():
       return {"message": "CRUD Application"}


@app.post("/todo", status_code=status.HTTP_201_CREATED)
def create_todo(todo: schemas.TodoCreate):
    # create a new database session
    session = Session(bind=engine, expire_on_commit=False)

    # create an instance of the ToDo database model
    todo_create = models.ToDo(task = todo.task)

    # add it to the session and commit it
    session.add(todo_create)
    session.commit()

    # close the session
    session.close()

    # return the id
    return {todo_create.task}


@app.get("/todo/{id}")
def read_todo(id: int):
       session = Session(bind=engine, expire_on_commit=False)
       todo_id = session.query(models.ToDo).get(id)
       session.close()
       if not todo_id:
              raise HTTPException(status_code=404, detail="Not Found by ID!")
       return {todo_id.task}


@app.put("/todo/{id}")
def update_todo(id: int, task: str):
       session = Session(bind=engine, expire_on_commit=False)
       todo_update = session.query(models.ToDo).get(id)
       if todo_update:
              todo_update.task = task
              session.commit()
       session.close()
       if not todo_update:
              raise HTTPException(status_code=404, detail="Not Found for Update!")
       return todo_update


@app.delete("/todo/{id}")
def delete_todo(id: int):
       session = Session(bind=engine, expire_on_commit=False)
       todo_delete = session.query(models.ToDo).get(id)
       if todo_delete:
              session.delete(todo_delete)
              session.commit()
              session.close()
       else:
              raise HTTPException(status_code=404, detail="Not Found for Detele!")
       return todo_delete


@app.get("/todo")
def read_todo_list():
       session = Session(bind=engine, expire_on_commit=False)
       todo_list = session.query(models.ToDo).all()
       return todo_list


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.2", port=8000, reload=True, log_level="info")

