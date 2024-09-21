# PromptFlow
Prompt flow is a suite of development tools designed to streamline the end-to-end development cycle of LLM-based AI applications, from ideation, prototyping, testing, evaluation to production deployment and monitoring. It makes prompt engineering much easier and enables you to build LLM apps with production quality.

* https://github.com/microsoft/promptflow

Deep delve into flow development
Getting started with prompt flow: A step by step guidance to invoke your first flow run.
* https://github.com/microsoft/promptflow/blob/main/docs/how-to-guides/quick-start.md

Tutorial: Chat with PDF: An end-to-end tutorial on how to build a high quality chat application with prompt flow, including flow development and evaluation with metrics.
* https://github.com/microsoft/promptflow/blob/main/examples/tutorials/e2e-development/chat-with-pdf.md

`Prompt flow for VS Code`
* https://marketplace.visualstudio.com/items?itemName=prompt-flow.prompt-flow

## Get startet with Prompt Flow
* https://microsoft.github.io/promptflow/how-to-guides/quick-start.html

Initialize a flow from cli
* https://microsoft.github.io/promptflow/how-to-guides/develop-a-dag-flow/init-and-test-a-flow.html

go to the flow root folder
```shell
cd ./promptflow;
```

create flow from cli
```shell
# cd ./promptflow;
flowname="localcopilot";
pf flow init --flow $flowname --type chat
```

add connection `openai`, use 
```yaml
$schema: https://azuremlschemas.azureedge.net/promptflow/latest/OpenAIConnection.schema.json
name: "local-ollama"
type: open_ai
api_key: "<user-input>" # Don't replace the '<user-input>' placeholder. The application will prompt you to enter a value when it runs.
organization: ""
base_url: "http://localhost:11434/v1" # Add this line to use customized API base
``` 
type the `api_key` is `dummy`.
and the model `llama3.1:8b` 

* in `$HOME` folder of your user home, a `.promptflow` folder will be created and contains `pf.sqlite` to save the 

Update the local connection api key.
```shell
pf connection show --name local-ollama

api_key="dummy";
pf connection update --set api_key=${api_key} --name local-ollama
```

test flow
```shell
# cd ./promptflow;
pf flow test --flow mycopilot --interactive
```

## Starting first project with PromptFlow local
Learning tutorial: A deeper dive on PromptFlow and Semantic Kernel
* https://www.youtube.com/watch?v=-maOEleJ1PE

## PromptFlow with LangChain
Integrate PromptFlow with LangChain
* https://learn.microsoft.com/en-us/azure/machine-learning/prompt-flow/how-to-integrate-with-langchain?view=azureml-api-2


## RAG with Semantic Kernel (1.x)
* https://www.youtube.com/watch?v=8QlFtKHzcaY

* Semantic Kernel tutorial 
use Semantic Kernel plugins to call function tool: https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/

* local ollama llm with Semantic Kernel https://www.youtube.com/watch?v=OEQDZLe3slM

## Reference
* https://pypi.org/project/promptflow/

