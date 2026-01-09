
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    APP_NAME: str = "Multimodal AI API"
    DEBUG: bool = False

    # Device
    DEVICE: str = "cpu"  # "cpu" or "cuda"

    # Text model
    TEXT_MODEL_NAME: str = "microsoft/phi-3-mini-4k-instruct"
    MAX_NEW_TOKENS: int = 200

    # Image model
    IMAGE_MODEL_NAME: str = "runwayml/stable-diffusion-v1-5"
    IMAGE_SIZE: int = 512
    NUM_INFERENCE_STEPS: int = 20

    HF_CACHE_DIR: Optional[str] = None

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
