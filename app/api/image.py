from fastapi import APIRouter
from pydantic import BaseModel
from app.services.image_services import generate_image

router = APIRouter()

class ImageRequest(BaseModel): 
    prompt: str

@router.post("/generate/image")
def generate_image_endpoint(request: ImageRequest):
    image_path = generate_image(request.prompt)
    return {
        "prompt": request.prompt,
        "image_path": image_path
    }
