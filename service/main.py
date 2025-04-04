from fastapi import FastAPI, Depends
from api import tron_api
from database.connection import get_db
import uvicorn

app = FastAPI(title="Tron API")


app.include_router(tron_api.tron, prefix="/api/tron", tags=["tron"])


if __name__ == "__main__":
    uvicorn.run('main:app', host="localhost", port=8000, log_level="debug", reload=True)