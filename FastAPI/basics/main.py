from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")

def hello():
    return {"message": "Hello, World"}

@app.get("/about") 
def about():
    return "this is a simple API built with FastAPI"
