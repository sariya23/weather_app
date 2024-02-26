from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def base_router():
    return {"msg": "its work!"}
