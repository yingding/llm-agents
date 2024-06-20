#!/bin/sh

model_name="gorilla-openfunctions-v2-q4_K_M"
model_file_path="$HOME/VCS/github/ml/llm-agents/deployconfig/ollama"
ollama rm ${model_name}
model_file="${model_file_path}/Modelfile"
ollama create ${model_name} -f ${model_file}
ollama list