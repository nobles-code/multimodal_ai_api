from fastapi import APIRouter
from pydantic import BaseModel
from app.services.text_services import generate_text

router = APIRouter()

class TextRequest(BaseModel):
    prompt: str

@router.post("/generate/text")
def generate_text_endpoint(request: TextRequest):
    output = generate_text(request.prompt)
    return {
        "prompt": request.prompt,
        "output": output
    }
