#!/bin/sh

# ollama pull zephyr:7b
# ollama pull llama3-groq-tool-use:8b
# ollama pull llama3.1:70b
ollama --version;
ollama pull mistral-nemo:12b-instruct-2407-fp16;
ollama pull mistral-nemo:12b;
ollama pull codellama:13b;
ollama pull llama3.1:8b;
ollama pull llama3.1:8b-instruct-q3_K_M;
ollama pull llama3.2:3b-instruct-q4_K_M;
ollama pull llama3.2:3b;