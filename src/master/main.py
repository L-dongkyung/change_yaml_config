from dataclasses import asdict

from fastapi import FastAPI
import uvicorn
from config import Config
from db import db
from routers import services

app = FastAPI()

# DataBase init
config = asdict(Config())
db.init_app(app, **config)

# router
app.include_router(services.router, tags=["mongodb"])


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
