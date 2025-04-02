from fastapi import FastAPI
from api import tron_api
import uvicorn


app = FastAPI(title="Tron API")


app.include_router(tron_api.tron, prefix="/api/tron", tags=["tron"])

#curl -X POST -H "Content-Type: application/json" -d '{"address":"TNMcQVGPzqH9ZfMCSY4PNrukevtDgp24dK"}' http://localhost:8000/api/tron/?address=TE2RzoSV3wFK99w6J9UnnZ4vLfXYoxvRwP


if __name__ == "__main__":
    uvicorn.run('main:app', host="localhost", port=8000, log_level="debug", reload=True)