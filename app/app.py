from contextlib import asynccontextmanager

from fastapi import FastAPI
from .routes import lm_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # До запуска приложения
    # Например подгрузка моделей

    yield

    # После конца работы приложения


app = FastAPI(
    title="ilps-serrvice-lm",
    description="Service that transcribes user voice input.",
    lifespan=lifespan,
)

app.include_router(lm_router)
