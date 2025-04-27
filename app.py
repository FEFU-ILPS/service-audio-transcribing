from contextlib import asynccontextmanager

from fastapi import FastAPI

from configs import configs
from models import model_manager
from routers import health_router, transcribing_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # on_startup
    await model_manager.load_models(
        rm_files=not configs.DEBUG_MODE,
    )

    yield

    # on_shutdown


service = FastAPI(lifespan=lifespan)

service.include_router(transcribing_router)
service.include_router(health_router)
