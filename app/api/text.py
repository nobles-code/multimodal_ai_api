from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class TextRequest(BaseModel):
    prompt: str

@router.post("/generate/text")
def generate_text(request: TextRequest):
    # Implementation for generating text
    generate_text = f"Generated text based on prompt: {request.prompt}"
    
    return {
        "prompt": request.prompt,
        "output": generate_text
    }
    
