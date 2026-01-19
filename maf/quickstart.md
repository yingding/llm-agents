# Quick Start Python SDK



## Rust Python package manager UV
### Installl UV
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

### UV python version
Use the following cmd to show the python version
```shell
uv python list
```

### (optional) init UV project
```shell
uv init
uv add --prerelease=allow -r requirements.txt
```

## Install Python VENV

### Install VENV on Linux/MacOSX
```shell
cd ./maf;
uv venv --python 3.12 && source .venv/bin/activate && uv sync;


```