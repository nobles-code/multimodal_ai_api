from diffusers import StableDiffusionPipeline
import torch
from app.core.config import settings

_image_pipeline = None

def get_image_pipeline():
    global _image_pipeline
    if _image_pipeline is None:
        device = settings.DEVICE
        _image_pipeline = StableDiffusionPipeline.from_pretrained(
            settings.IMAGE_MODEL_NAME,
            torch_dtype=torch.float16 if device == "cuda" else torch.float32,
        )
        _image_pipeline = _image_pipeline.to(device)
    return _image_pipeline

def generate_image(prompt: str):
    pipe = get_image_pipeline()
    image = pipe(
        prompt,
        height=settings.IMAGE_SIZE,
        width=settings.IMAGE_SIZE,
        num_inference_steps=settings.NUM_INFERENCE_STEPS,
    ).images[0]
    return image
