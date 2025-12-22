from fastapi import FastAPI
from pydantic import BaseModel   # 👈 yahan import

app = FastAPI()

# 🔹 Pydantic Model (yahan likhna hai)
class UserCreate(BaseModel):
    name: str
    email: str
    age: int


# 🔹 Routes (APIs)
@app.get("/")
def home():
    return {"message": "Hello FastAPI"}


@app.get("/hello")
def say_hello():
    return {"msg": "Hello User"}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id,
        "message": "User fetched successfully"
    }

@app.get("/search")
def search_user(name: str, age: int):
    return {
        "name": name,
        "age": age
    }


@app.get("/users")
def get_users(page: int = 1, limit: int = 10):
    return {
        "page": page,
        "limit": limit,
        "message": "Users list fetched"
    }


@app.post("/users")
def create_user(user: UserCreate):
    return {
        "message": "User created successfully",
        "user": user
    }
