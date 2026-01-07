from transformers import pipeline

# load once at startup (important)
text_generator = pipeline(
    "text-generation",
    model="gpt2",
    max_new_tokens=100
)

def generate_text(prompt: str) -> str:
    result = text_generator(prompt)
    return result[0]["generated_text"]
