from fastapi import FastAPI

app = FastAPI(title="Multimodal AI API")

@app.get("/")
def health_check():
    return {"status": "ok"}
