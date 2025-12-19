from fastapi import FastApi 
app = FastApi()

@app.get("/welcome")
def welcom():
    return{
        "message":"hello world"
    }
