
from pydantic import BaseModel, UUID4

class UserCreate(BaseModel):
    name: str
    email: str

class UserOut(BaseModel):
    id: UUID4
    name: str
    email: str

    class Config:
        orm_mode = True
