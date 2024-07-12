# ollama openai endpoint

## Ollama model file doc
* https://github.com/ollama/ollama/blob/main/docs/modelfile.md


Customize ollama response:
* https://github.com/ollama/ollama/issues/1729
* https://github.com/ollama/ollama/issues/1729#issuecomment-1937763369
```yaml
FROM ./gorilla-openfunctions-v1.Q4_K_M.gguf


TEMPLATE """

### User:
{{.Prompt }}
### System:
{{.System}}

### Response:
"""

SYSTEM """<<function>> functions = [
    {
        "name": "Uber Carpool",
        "api_name": "uber.ride",
        "description": "Find suitable ride for customers given the location, type of ride, and the a>
        "parameters":  [
            {"name": "loc", "description": "Location of the starting place of the Uber ride"},
            {"name": "type", "enum": ["plus", "comfort", "black"], "description": "Types of Uber rid>
            {"name": "time", "description": "The amount of time in minutes the customer is willing t>
        ]
    }
]\n
ASSISTANT:"""

PARAMETER stop "<|system|>"
PARAMETER stop "<|user|>"
PARAMETER stop "<|assistant|>"
PARAMETER stop "</s>"
```

```shell
./ollama run gorilla_test "USER: <<question>>"Call me an Uber ride type \"Plus\" in Berkeley at zipcode 94704 in 10 minutes ""
uber.ride(USER="plus", LOC="94704", TIME=10)
```

## Ollama OpenAI endpoint compatibility

Ollama openai endpoint isn't supporting function calling using openai compatible endpoint at the time of writing on 20th June 2024

* https://github.com/ollama/ollama/blob/main/docs/openai.md#endpoints
