# Quick Start Python SDK


# 1 Setup 
All setup task in this section only need to be done once on your dev host.

## 1.1 Create python venv with UV package tool
This section documents the cmds to install `UV` python package tool.

### Install UV
On Mac:
```shell
brew install uv
brew upgrade uv
uv --version
```
Note: `Self-update (uv self update)` is disabled by design via brew.

On Linux:
```
curl -LsSf https://astral.sh/uv/install.sh | sh
uv self update
uv --version
```

On Windows:
```powershell
winget install --id astral-sh.uv -e
uv self update
uv --version
```

### Display available python version with UV
Use the following cmd to show the python version
```shell
uv python list
```

### (Optional) Initialize UV project
This task is only necessary, should there be now `pyproject.toml` file in the uv project folder
```shell
uv init
# recreate teh pyproject.toml
uv add --prerelease=allow -r requirements.txt
```

## 1.2 Install az cli tool
This section documents the cmds to install `az` cli tool.
az cli tool allows you to fetch azure credentials over entra id user or managed identity, so that you don't need to save the api key in your environment variables.

### Install az cli for MacOSX:
```shell
brew update && brew install azure-cli
```
Source: https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-macos?view=azure-cli-latest

### Install az cli for for Linux:
Source: https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux?view=azure-cli-latest&pivots=apt

### Install az cli For Windows:
```powershell
winget install --exact --id Microsoft.AzureCLI
```
Source: https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows?view=azure-cli-latest&pivots=winget


## 1.3 Creating Python VENV

### 1.3.1 Creating VENV on Linux/MacOSX
You will use `uv` tool to create a python venv, `uv` tool is a rust implementation, doesn't have `pip` by design.
```shell
cd ./maf;
uv venv --python 3.12 && source .venv/bin/activate && uv sync --prerelease=allow;
```

### 1.3.2 Create VENV on Windows
```powershell
cd .\maf;
uv venv --python 3.12 && .\.venv\Scripts\activate && uv sync --prerelease=allow;
```

## 1.4 Login to azure tenant
You will use az cli tools to login to azure tenant with your entra id user, so that azure credential can be fetched with python sdks.

You entra id user shall have `Azure AI user` RBAC role and added to the new azure foundry project.

Use the following az cli cmds to login to azure tenant:
```shell
az logout
az account clear
az login --tenant <your_tenant_id>
```

## 1.5 Fill out the config .env file
Use the following cmds to fill out the config .env file for your python project.

### 1.5.1 Fill out config on Linux/MacOSX
```shell
cd ./maf;
cp .env.example .env
# Edit .env and add env variable with your foundry config
```

### 1.5.2 Fill out config on Windows
```powershell
cd .\maf;
Copy-Item .env.example .env
# Edit .env and add env variable with your foundry config
``` 

# 2 Run python sample scripts
After the dev host is setup successful, use following steps to run sample scripts.

## 2.1 Activate python venv
On Linux / MacOSX
```shell
cd ./maf;
## uv sync to install the dependency from pyproject.toml
source .venv/bin/activate && uv sync;
```

On Windows
```powershell
cd .\maf;
.\.venv\Scripts\activate && uv sync;
```

## 2.2 Run sample scripts in venv
with the venv activated

On Linux / MacOSX:
```shell
cd ./maf;
# run python script e.g. 01basic_llm_chatcompletions_client.py 
python3 01basic_llm_chatcompletions_client.py
```

On Windows
```powershell
cd .\maf;
python 01basic_llm_chatcompletions_client.py
```

**Note:**\
You can change the env variable `WITH_LOGGING="False"` or `WITH_LOGGING="True"` in the .env config file to turn on or turn off the logging outputs.