from fastapi import Depends, FastAPI, HTTPException 

app = FastAPI()

@app.get("/hello_world")
def hello_world():
    """
    Hello world example to upload to heroku app
    """

    return {"key": "hello world"}