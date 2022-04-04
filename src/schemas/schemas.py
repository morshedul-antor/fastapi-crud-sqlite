from pydantic import BaseModel

class TodoCreate(BaseModel):
       task: str
