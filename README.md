# OrbitDesk Support Agent Starter Pack

This package contains the source material for the AI Engineer Internship Assignment.

OrbitDesk is a fictional workspace product used by teams to build dashboards, schedule exports, connect data sources and manage API integrations. No external product knowledge is required or expected.

## Package Contents

- `knowledge_base/`: Current product documentation. Treat these files as the primary source of truth.
- `resolved_cases.json`: Previously resolved support cases. Cases marked `superseded` are historical and must not override current documentation.
- `sample_questions.json`: Five questions that exercise different workflow paths.
- `output_schema.json`: A starter JSON Schema for structured responses.

## Important Notes

- Build answers only from the supplied material.
- Source references should use document IDs, filenames or resolved-case IDs.
- The knowledge base takes precedence over resolved cases if the two conflict.
- A resolved case marked `superseded` may be useful for testing retrieval and verification, but its resolution must not be presented as current guidance.
- Do not assume that the system can perform account changes, issue refunds or contact external parties.
- You may add local indexes, embeddings or generated test fixtures inside your own repository.

## Suggested Entry Point

Start with the questions in `sample_questions.json`, but ensure that your application can accept new natural-language questions as well.


---

# Solution

This project implements an AI-powered OrbitDesk Support Agent using Retrieval-Augmented Generation (RAG). The agent answers support questions based only on the provided knowledge base and resolved cases.

## Features

- Knowledge Base Loader
- Semantic Search using Sentence Transformers
- FAISS Vector Index
- Question Classification (Triage)
- Local LLM Answer Generation
- Answer Verification
- LangGraph Workflow
- Structured JSON Output

## Technologies Used

- Python
- LangGraph
- FAISS
- Sentence Transformers
- Hugging Face Transformers
- FLAN-T5 Base
- NumPy

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

## Example Question

```text
Can Viewer create API credentials?
```

## Example Output

```json
{
  "classification": "answerable",
  "answer": "No. A Viewer cannot create API credentials.",
  "confidence": 0.95,
  "requires_human": false
}
```

## Author

**Manoj Chaudhary**
