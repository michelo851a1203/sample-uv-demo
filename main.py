from fastapi import FastAPI
from contextlib import asynccontextmanager
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def life_span(_: FastAPI):
    logger.info("FastAPI application starting on port 8080...")
    yield


app = FastAPI()

@app.get("/")
def root():
    return { "status": "OK" }

@app.get("/health")
def check_health():
    return { "status": "OK" }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
