# Intro

this section describes the steps to run a multi agent example with LangGraph framework.

## Steps

### Activate VENV

```powershell
cd $env:USERPROFILE\Documents\VCS\llm-agents;
& ".\setup\activate.ps1";
```

### Install package

```powershell
$PackageFile="requirements_win.txt";

Invoke-Expression "(Get-Command python).Source";

& "python" -m pip install --upgrade pip;
& "python" -m pip install -r $PackageFile --no-cache-dir;
```




## Reference
* LangGraph tutorial https://www.datacamp.com/tutorial/langgraph-tutorial
* LangGraph concept https://langchain-ai.github.io/langgraph/concepts/high_level/