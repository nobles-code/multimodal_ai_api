# Multimodal AI Generation API

A production-style backend service for multimodal AI content generation, supporting
text and image generation via REST APIs.

## Features
- Text generation using Hugging Face Transformers
- Image generation using Stable Diffusion
- FastAPI-based REST endpoints
- Dockerized for deployment

## Tech Stack
- Python
- FastAPI
- Hugging Face Transformers
- Diffusers (Stable Diffusion)
- Docker

## API Endpoints

### POST /generate/text
```json
{
  "prompt": "Write a manga plot about a hero in Nairobi"
}
