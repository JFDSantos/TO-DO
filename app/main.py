from fastapi import FastAPI
from app.routes import auth, tasks
from app.database import init_db 
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(auth.router)
app.include_router(tasks.router)


    