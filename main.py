import json
from src.graph import app

query = input("Ask your question: ")

result = app.invoke({
    "query": query,
    "classification": "",
    "results": [],
    "answer": "",
    "output": {}
})

print("\n================ FINAL OUTPUT ================\n")
print(json.dumps(result["output"], indent=4))