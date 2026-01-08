from transformers import pipeline

# Using a lightweight GPT-2 model for text generation
text_generator = pipeline(
    "text-generation",
    model="gpt2",
    max_new_tokens=100
)

# more powerful microsoft model (commented out for resource reasons)

# text_generator = pipeline(
#     "text-generation",
#     model="microsoft/phi-3-mini-4k-instruct",
#     trust_remote_code=True,
#     max_new_tokens=200
# )

def generate_text(prompt: str) -> str:
    result = text_generator(prompt)
    return result[0]["generated_text"]
