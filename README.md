# GraphRAG + Ollama + Cyberpunk

Project folder with the results of the experiments

## Getting started

for reference: https://microsoft.github.io/graphrag/get_started/

1. conda create --name jm_project python==3.11
2. conda activate jm_project
3. cd <project_folder_path>
4. add source text to ./input
5. edit settings.yaml
6. install requirements for embedding_proxy:
    - install torch with or without cuda support, https://pytorch.org/get-started/locally/
    - for example: pip install torch --index-url https://download.pytorch.org/whl/cu126
    - install other requirements: pip install -r requirements.txt
7. start embedding_proxy: python embedding_proxy.py --port 11435
8. stop Ollama if running and set env. variables:
    - set OLLAMA_HOST=0.0.0.0:11434 (if the ollama on the another machine)
    - set OLLAMA_CONTEXT_LENGTH=12288
    - pull the model (qwen3:14b)
    - start ollama: ollama serve
9. rum graphrag pipeline: graphrag index

    