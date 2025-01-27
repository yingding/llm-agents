# PowerShell script to reload models

# Check Ollama version
ollama --version;

# Pull models
ollama pull mistral-nemo:12b;
ollama pull deepseek-r1:7b;
ollama pull deepseek-r1:1.5b;

# List models
ollama list;




