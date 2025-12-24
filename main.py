from fastapi import FastAPI

app = FastApi()

@app.get("/welcome")
def welcom():
    return{
        "message":"hello world"
    }
