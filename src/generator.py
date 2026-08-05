from transformers import pipeline

print("Loading Local LLM...")

generator = pipeline(
    task="text2text-generation",
    model="google/flan-t5-base"
)

print("Local LLM Loaded!")