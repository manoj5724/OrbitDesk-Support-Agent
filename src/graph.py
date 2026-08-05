from langgraph.graph import StateGraph, END
from typing import TypedDict


class AgentState(TypedDict):
    query: str
    classification: str
    results: list
    answer: str
    output: dict


workflow = StateGraph(AgentState)

from src.triage import Triage
from src.retriever import Retriever
from src.generator import generator
from src.verifier import Verifier
from src.loader import load_knowledge_base

documents = load_knowledge_base()

retriever = Retriever()
retriever.build_index(documents)

triage = Triage()
verifier = Verifier()

def triage_node(state):
    state["classification"] = triage.classify(state["query"])
    return state


def retrieve_node(state):
    state["results"] = retriever.search(state["query"], top_k=1)
    return state


def generate_node(state):
    context = ""

    for doc in state["results"]:
        context += doc["content"] + "\n\n"

    prompt = f"""
Answer ONLY using the context below.

Context:
{context}

Question:
{state['query']}

Answer:
"""

    response = generator(prompt, max_new_tokens=150)
    state["answer"] = response[0]["generated_text"]

    return state


def verify_node(state):
    output = {
        "classification": state["classification"],
        "answer": state["answer"],
        "sources": [],
        "confidence": 0.95,
        "requires_human": False,
        "reason": "Answer generated from retrieved knowledge base."
    }

    for doc in state["results"]:
        output["sources"].append({
            "source_id": doc["filename"],
            "passage": doc["content"][:200]
        })

    state["output"] = verifier.verify(output)
    return state

# Register Nodes
workflow.add_node("triage", triage_node)
workflow.add_node("retrieve", retrieve_node)
workflow.add_node("generate", generate_node)
workflow.add_node("verify", verify_node)

# Set Entry Point
workflow.set_entry_point("triage")

# Connect Nodes
workflow.add_edge("triage", "retrieve")
workflow.add_edge("retrieve", "generate")
workflow.add_edge("generate", "verify")
workflow.add_edge("verify", END)

# Compile Graph
app = workflow.compile()

print("LangGraph Created Successfully!")