# Download the GGUF

```shell
python3 setup/download_gguf.py -t gorilla-gguf-v1 -m mac_local
```

## Ollama custom model deployment
### Install ollama

### Test ollama cli
```shell
open http://localhost:11434
```


### Create he Modelfile
```shell
touch ./deployment/Modelfile
```

* ollama model param - https://github.com/ollama/ollama/blob/main/docs/modelfile.md#parameter

### Add the GGUF and template to the Modelfile
* https://huggingface.co/TheBloke/gorilla-openfunctions-v1-GGUF

```Modelfile
FROM "/Users/yingding/MODELS/downloads/hf/gorilla-openfunctions-v2-q4_K_M.gguf"

TEMPLATE """
{{ .Prompt }}
"""
```

Reference:
* https://huggingface.co/gorilla-llm/gorilla-openfunctions-v2/discussions/7
* https://github.com/ollama/ollama/blob/main/docs/modelfile.md

### Create a ollama model from the Hf model
```shell
model_name=gorilla-openfunctions-v2-q4_K_M
model_file="$HOME/VCS/github/ml/llm-agents/deployconfig/ollama/Modelfile"
ollama create ${model_name} -f ${model_file}
```

View the 
```shell
ollama list
```

### Run the ollama model
```shell
model_name=gorilla-openfunctions-v2-q4_K_M
ollama run ${model_name}
```

### (optional) remove the ollama model
```shell
model_name=gorilla-openfunctions-v2-q4_K_M
ollama rm ${model_name}
```

### (optional) view Modelfile
```shell
model_name=adrienbrault/gorilla-openfunctions-v2:Q4_K_M
ollama show --modelfile ${model_name}
```

### (optional) exit ollama run
```shell
/byes
```

Reference:
* https://www.markhneedham.com/blog/2023/10/18/ollama-hugging-face-gguf-models/
* create ollama model from hf gguf - https://www.youtube.com/watch?v=TFwYvHZV6j0

### Patch to OpenAI response
Using custom response adaptor
* https://github.com/puppetm4st3r/local_function_calling/blob/main/openai.py