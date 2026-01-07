from fastapi import FastAPI
from app.api import text

app = FastAPI(title="Multimodal AI API")

app.include_router(text.router, prefix="")

@app.get("/")
def health_check():
    return {"status": "API is running"}