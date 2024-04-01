import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from home.router import router as router_info
from weather.router import router as router_weather

app = FastAPI(title="Weather App")
app.mount("/src/static", StaticFiles(directory="static"), name="static")


app.include_router(router_info)
app.include_router(router_weather)


def main():
    uvicorn.run(app, host="127.0.0.1", port=8000)

if __name__ == "__main__":
    main()