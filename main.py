from fastapi import FastAPI
from src.api import api, health

app = FastAPI()

app.include_router(api.router, prefix="/api")
app.include_router(health.router, prefix="/api")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
    
