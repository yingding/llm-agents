# Download the GGUF

```shell
python3 setup/download_gguf.py -t gorilla-gguf-v1 -m mac_local
```

## Ollama custom model deployment
### Install ollama
* 0.3.4
* 0.2.8
* 0.2.1
* 0.1.48
* 0.1.45
* 0.1.37
* 0.1.32

```shell
ollama -v
```


### Test ollama cli
```shell
open http://localhost:11434
```


### Create he Modelfile
```shell
touch ./deployconfig/ollama/Modelfile
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

### Run the ollama model with ollama cli in terminal for testing
```shell
model_name=gorilla-openfunctions-v2-q4_K_M
ollama run ${model_name}
```

## Important Notice with Ollama Version update.
The ollama model converted from gguf must be recreated after every ollama version update
```shell
# remove
model_name=<model_name>
ollama rm ${model_name}
# recreate
model_file="<model_file_path>/Modelfile"
ollama create ${model_name} -f ${model_file}
```
or
```shell
source $HOME/VCS/github/ml/llm-agents/setup/update.sh
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

### (optional) exit ollama terminal cli
```shell
/byes
```

### pull model
```shell
ollama pull zephyr:7b
ollama pull llama3-groq-tool-use:8b
```
* https://ollama.com/library/zephyr


Reference:
* https://www.markhneedham.com/blog/2023/10/18/ollama-hugging-face-gguf-models/
* create ollama model from hf gguf - https://www.youtube.com/watch?v=TFwYvHZV6j0
* ollama with langchain local function calling - https://www.youtube.com/watch?v=Nfk99Fz8H9k


### Patch to OpenAI response
Using custom response adaptor
* https://github.com/puppetm4st3r/local_function_calling/blob/main/openai.py