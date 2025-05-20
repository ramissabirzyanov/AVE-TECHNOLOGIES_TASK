from fastapi import FastAPI


from app.services.redis_service import redis
from app.api.endpoints import router as api_router



app = FastAPI()

app.include_router(api_router, prefix="/api")