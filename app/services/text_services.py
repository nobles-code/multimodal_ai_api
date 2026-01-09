from transformers import pipeline
from app.core.config import settings

_text_pipeline = None

def get_text_pipeline():
    global _text_pipeline
    if _text_pipeline is None:
        _text_pipeline = pipeline(
            "text-generation",
            model=settings.TEXT_MODEL_NAME,
            device=0 if settings.DEVICE == "cuda" else -1,
        )
    return _text_pipeline

def generate_text(prompt: str) -> str:
    pipe = get_text_pipeline()
    result = pipe(
        prompt,
        max_new_tokens=settings.MAX_NEW_TOKENS,
        do_sample=True,
        temperature=0.7,
    )
    return result[0]["generated_text"]
