import os
import json


def load_knowledge_base(folder_path="knowledge_base"):
    documents = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".md"):
            file_path = os.path.join(folder_path, filename)

            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()

            documents.append({
                "filename": filename,
                "content": content
            })

    return documents


def load_json(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        return json.load(file)