from fastapi import FastAPI

from src.routers import cities

app = FastAPI()

app.include_router(cities.router)
