from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException

app = FastAPI()

users_db=[]
current_user_id = 1

class User(BaseModel):
    id: int
    name: str
    email: str
    age: int

class UserCreate(BaseModel):
    name: str
    email: str
    age: int

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    age: int

@app.post("/users", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate):
    global current_user_id

    new_user = User(
        id=current_user_id,
        name=user.name,
        email=user.email,
        age=user.age
    )

    users_db.append(new_user)
    current_user_id += 1

    return new_user

from typing import List

@app.get("/users", response_model=List[UserResponse])
def get_all_users():
    return users_db


@app.get("/users/{user_id}", response_model=UserResponse)
def get_user_by_id(user_id: int):
    for user in users_db:
        if user.id == user_id:
            return user

    raise HTTPException(status_code=404, detail="User not found")


@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, updated_user: UserCreate):
    for index, user in enumerate(users_db):
        if user.id == user_id:
            new_user = User(
                id=user_id,
                name=updated_user.name,
                email=updated_user.email,
                age=updated_user.age
            )
            users_db[index] = new_user
            return new_user

    raise HTTPException(status_code=404, detail="User not found")


@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int):
    for index, user in enumerate(users_db):
        if user.id == user_id:
            users_db.pop(index)
            return

    raise HTTPException(status_code=404, detail="User not found")
