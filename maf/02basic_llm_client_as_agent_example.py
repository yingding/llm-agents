# pip install agent-framework --pre
# Use `az login` to authenticate with Azure CLI
"""
Docstring for maf.02basic_llm_client_as_agent_example
This module demonstrates the use of Azure OpenAI Chat Client
as an agent that can interact with tools. 
Sample show the completions_client.as_agent() method usage
to create an agent from a chat client.
"""
import asyncio
from agent_framework import (
    BaseChatClient,
)
from typing import Annotated
from pydantic import Field
import logging
from random import randint
from utils.model_client import create_chat_client

logger = logging.getLogger(__name__)

def get_weather_at_location(
    location: Annotated[str, Field(description="The location to get the weather for.")],
) -> str:
    """mock the realtime weather for a given location."""
    conditions = ["sunny", "cloudy", "rainy", "stormy"]
    return f"The weather in {location} is {conditions[randint(0, 3)]} with a high of {randint(10, 30)}°C."


async def main() -> None:
    # Initialize a chat agent with Azure OpenAI Chat(Completions) Client
    complietions_client: BaseChatClient = create_chat_client()
    message = "What's the weather in Munich and in Seattle?"
    stream = True
    print(f"User: {message}")
    if stream:
        print("Assistant: ", end="")
        # The Agent wraps the client and handles the "ReAct" loop (Reasoning + Acting) or simply the tool calling loop.
        async for chunk in complietions_client.as_agent().run_stream(message, tools=[get_weather_at_location]):
            if chunk.text:
                print(chunk.text, end="")
        print("")
    else:
        response = await complietions_client.as_agent().run(message, tools=[get_weather_at_location])
        print(f"Assistant: {response}")

if __name__ == "__main__":
    asyncio.run(main())