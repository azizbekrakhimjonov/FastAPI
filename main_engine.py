from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from main_base import Functions
from models import start_tables

app = FastAPI()
temp = 0


class Signup(BaseModel):
    name: str
    surname: str
    age: int


class Post(BaseModel):
    word: str


@app.get("/")
def root():
    return {"greeting": "Welcome User! Welcome to our translator-API"}


@app.post("/trans/")
def translate(post: Post):
    global temp
    trans_back = Functions()
    back = trans_back.send_back(post.word)
    print(back)
    temp += 1
    if temp > 7:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="To continue please verify Privacy: please click here> http://127.0.0.1:8000/login/")
    temp += 1
    return {f"Request: {post.word}": f"Translate: {back}"}


@app.post("/login")
def verify(post: Signup):
    fun = Functions()
    fun.authentication(post.name, post.surname, post.age)


@app.post("/signup/")
def register(post: Signup):
    reg = Functions()
    back = reg.signup(post.name, post.surname, post.age)
    return {"feedback": back}


if __name__ == '__main__':
    start_tables()
