# Intro

## Install on Mac

```shell
brew tap microsoft/foundrylocal;
brew install foundrylocal;
```

```shell
foundry model list
```

```shell
# show model cache location
# $HOME/.foundry/cache/models
foundry cache location
# set model cache location
foundry cache cd $HOME/Code/MODELS/foundry/cache/models

# foundry service stop
foundry service stop
```

```shell
foundry model ls
foundry model run phi-4-mini
```

```shell
/exit
/get_config
/set_config system_prompt:you are a help assistant and always communication in english.
```

## References
* Get Startet with Foundry Local https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started