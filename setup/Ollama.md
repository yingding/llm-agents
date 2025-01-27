## Change the model download folder on Windows with Env variable

```
OLLAMA_MODELS
```

Reference:
* https://github.com/ollama/ollama/blob/main/docs/faq.md#where-are-models-stored

## Run the reload script
```powershell
.\reload.ps1
```

## Run an ollama model on console
```powershell
# run a model from console
ollama run deepseek-r1:1.5b
# stop the console
/bye
# see which model is loaded and Processor for the model used
ollama ps
```

Reference:
* https://www.hostinger.com/tutorials/ollama-cli-tutorial

## Ollama log on windows
```
cd C:\Users\<username>\AppData\Local\Ollama
less server.log
```
Reference:
* https://priyashpatil.com/posts/how-to-access-and-read-ollama-server-logs-on-various-systems