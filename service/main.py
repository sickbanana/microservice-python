from fastapi import FastAPI, Depends
from .api import tron_api
import uvicorn

app = FastAPI(title="Tron API")


app.include_router(tron_api.tron, prefix="/api/tron", tags=["tron"])


if __name__ == "__main__":
    uvicorn.run('app.main:app', host="0.0.0.0", port=8000, log_level="debug", reload=True)