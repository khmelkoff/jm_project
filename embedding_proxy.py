from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from typing import List, Union
import argparse
from langchain_huggingface.embeddings import HuggingFaceEmbeddings

parser = argparse.ArgumentParser(description="Run the embedding proxy server")
parser.add_argument("--port", type=int, default=11435, help="Port to run the server on")
parser.add_argument("--model", type=str, default="deepvk/user-bge-m3", help="Embedding model name")
parser.add_argument("--reload", action="store_true", help="Enable auto-reload for development")
parser.add_argument("--verbose", action="store_true", help="Enable diagnostic printing")
args = parser.parse_args()

app = FastAPI()

# hf_embedding = HuggingFaceEmbeddings(model_name="BAAI/bge-m3", model_kwargs={"device": 'cuda'})
hf_embedding = HuggingFaceEmbeddings(model_name=args.model, model_kwargs={"device": 'cuda'})


class EmbeddingRequest(BaseModel):
    input: Union[str, List[str]]
    model: str


class EmbeddingResponse(BaseModel):
    object: str
    data: List[dict]
    model: str


@app.post("/embeddings")
async def create_embedding(request: EmbeddingRequest):
    if isinstance(request.input, str):
        request.input = [request.input]

    for text in request.input:
        if args.verbose:
            print(f'INPUT TEXT:\n{text[:100]}...\n')

    ollama_requests = [{"model": request.model, "prompt": text} for text in request.input]

    embeddings = []

    for i, ollama_request in enumerate(ollama_requests):

        text = ollama_request['prompt']
        vector = hf_embedding.embed_documents(list(text))[0]

        result = {"embedding": vector}

        if args.verbose:
            print(f'OUTPUT RESULT {i}\n{result["embedding"][:10]}...\n')

        embeddings.append({
            "object": "embedding",
            "embedding": result["embedding"],
            "index": i
        })

    return EmbeddingResponse(
        object="list",
        data=embeddings,
        model=request.model,
    )

if __name__ == "__main__":

    uvicorn.run("embedding_proxy:app", host="0.0.0.0", port=args.port, reload=args.reload)
