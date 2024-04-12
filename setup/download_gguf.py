import os
import click


from dataclasses import dataclass
@dataclass
class DirectorySetting:
    """set the directory for the model download"""
    home_dir: str="/home/jovyan/llm-models"
    transformers_cache_home: str="core-kind/yinwang/models"
    huggingface_token_file: str="core-kind/yinwang/.cache/huggingface/token"

    def get_cache_home(self):
        """get the cache home"""
        return f"{self.home_dir}/{self.transformers_cache_home}"
    
    def get_token_file(self):
        """get the token file"""
        return f"{self.home_dir}/{self.huggingface_token_file}"

model_map = {
    # "gorilla-gguf-v1": "TheBloke/gorilla-openfunctions-v1-GGUF",
    "gorilla-gguf-v2": "gorilla-llm/gorilla-openfunctions-v2-gguf",
}

# https://www.markhneedham.com/blog/2023/10/18/ollama-hugging-face-gguf-models/
# https://huggingface.co/gorilla-llm/gorilla-openfunctions-v2-gguf/blob/main/README.md
# 81% benchmark
file_name = "gorilla-openfunctions-v2-q4_K_M.gguf"

dir_mode_map = {
    "kf_notebook": DirectorySetting(),
    "mac_local": DirectorySetting(home_dir="/Users/yingding", transformers_cache_home="MODELS/ollama", huggingface_token_file="MODELS/.huggingface_token"),
}

default_model_type = "gorilla-gguf-v2"
default_dir_mode = "mac_local"


def need_token(model_type: str, model_name_prefix: list=["llama", "gemma"]):
    """check if the model needs token"""
    return any([model_type.startswith(prefix) for prefix in model_name_prefix])


def get_token(dir_setting: DirectorySetting):
    """get the token from the token file"""
    token_file_path = dir_setting.get_token_file()
    with open(token_file_path, "r") as file:
        # file read add a new line to the token, remove it.
        token = file.read().replace('\n', '')
    return token

# print the raw string to see if there is new line in the token
# print(r'{}'.format(token))

# Reference: https://click.palletsprojects.com/en/8.1.x/quickstart/
# @click.option(..., is_flag=True, ...) set the option to be boolean
# call with download_llms --help
# https://www.geeksforgeeks.org/argparse-vs-docopt-vs-click-comparing-python-command-line-parsing-libraries/
# https://click.palletsprojects.com/en/8.1.x/quickstart/
# https://click.palletsprojects.com/en/8.1.x/options/
# https://www.youtube.com/watch?v=kNke39OZ2k0
@click.command()
@click.option('-t','--model-type', 'model_type', default=default_model_type, type=str, required=False, help=f"set the llm type to download:\n{', '.join(model_map.keys())}, default is {default_model_type}")
@click.option('-m','--mode', 'dir_mode', default=default_dir_mode, type=str, required=False, help=f"set the directory settings to use:\n{', '.join(dir_mode_map.keys())}, default is {default_dir_mode}")
def download(model_type: str=default_model_type, dir_mode: str=default_dir_mode):
    """
    This method will download the llm model. If cache exists, the cached model will be used.
    
    get help:
    python3 download_gguf.py --help

    valid call:
    python3 download_gguf.py -t mistral7B-01
    python3 download_gguf.py --model-type mistral7B-01
    
    invalid call:
    python3 download_gguf.py -t=mistral7B-01
    python3 download_gguf.py --model-type=mistral7B-01

    set directory:
    python3 download_gguf.py -t mistral7B-01 -m kf_notebook
    
    Args:
      model_type: "gorilla-gguf-v2", ...
      dir_mode: "kf_notebook", "mac_local"
    """
 
    dir_setting=dir_mode_map.get(dir_mode, dir_mode_map[default_dir_mode])
    os.environ['XDG_CACHE_HOME']=dir_setting.get_cache_home()
    print("-"*10)
    print(f"download dir: {os.environ['XDG_CACHE_HOME']}")

    model_name = model_map.get(model_type, model_map[default_model_type])

    print("-"*10)
    print(f"model_type: {model_type}")
    print(f"model_name: {model_name}")
    print("-"*10)

    if need_token(model_type):
        kwargs = {"token": get_token(dir_setting)}
        print("huggingface token loaded")
    else:
        kwargs = {}
        print("huggingface token is NOT needed")
    print("-"*10)
    
    local_dir=dir_setting.get_cache_home()
    print(f"local_dir: {local_dir}")

    from huggingface_hub import snapshot_download, hf_hub_download
    # download all files https://github.com/ggerganov/llama.cpp/discussions/2948
    # snapshot_download(repo_id=model_name, local_dir=local_dir,
    #                 local_dir_use_symlinks=False, revision="main")
    # download a specific file https://huggingface.co/docs/huggingface_hub/en/guides/download
    hf_hub_download(repo_id=model_name, local_dir=local_dir, filename=file_name,
                    local_dir_use_symlinks=False, revision="main")
    
if __name__ == '__main__':
    download()