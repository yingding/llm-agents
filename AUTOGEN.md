## About AutoGen and AutoGen Studio
**AutoGen** is a framework that enables the development of LLM applications using multiple agents that can converse with each other to solve tasks. AutoGen agents are customizable, conversable, and seamlessly allow human participation. They can operate in various modes that employ combinations of LLMs, human inputs, and tools.

**AutoGen Studio** is an AutoGen-powered AI app (user interface) to help you rapidly prototype AI agents, enhance them with skills, compose them into workflows and interact with them to accomplish tasks. It is built on top of the AutoGen framework, which is a toolkit for building AI agents.

## Start AutoGen Studio
```shell
cd <project root>
# autogenstudio ui --host 127.0.0.1 --port 8080 --reload --log-level debug --appdir ./autogen/studio/
autogenstudio ui --host 127.0.0.1 --port 8080 --appdir ./autogen/studio/
```



## Reference:
* Autogen Studio https://github.com/microsoft/autogen/tree/main/samples/apps/autogen-studio
* AutoGen github https://github.com/microsoft/autogen

## Function calling leader board
* https://gorilla.cs.berkeley.edu/leaderboard.html
