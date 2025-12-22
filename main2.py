from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException


app = FastAPI()

users_db=[]

class User(BaseModel):
    id: int
    name: str
    email: str
    age: int

@app.post("/users")
def create_user(user: User):
    users_db.append(user)
    return {
        "message": "User added successfully",
        "data": user
    }

@app.get("/users")
def get_all_users():
    return {
        "total_users": len(users_db),
        "users": users_db
    }

@app.get("/users/{user_id}")
def get_user_by_id(user_id: int):
    for user in users_db:
        if user.id == user_id:
            return user

    return {"error": "User not found"}

@app.put("/users/{user_id}")
def update_user(user_id: int, updated_user: User):
    for index, user in enumerate(users_db):
        if user.id == user_id:
            users_db[index] = updated_user
            return {
                "message": "User updated successfully",
                "data": updated_user
            }

    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for index, user in enumerate(users_db):
        if user.id == user_id:
            users_db.pop(index)
            return {
                "message": "User deleted successfully"
            }

    raise HTTPException(status_code=404, detail="User not found")