# pip install agent-framework --pre
# Use `az login` to authenticate with Azure CLI
"""
Docstring for maf.01basic_llm_client_ignore_tools
This module demonstrates the use of Azure OpenAI Chat Client,
which ignores tool calls from the model and only interacts with the model API.
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
        # low-level method that only interacts with the Model API. It sends the tool definitions, 
        # but it does not contain the loop to execute the tool when the model requests it.
        async for chunk in complietions_client.get_streaming_response(message, tools=[get_weather_at_location]):
            if chunk.text:
                print(chunk.text, end="")
        print("")
    else:
        response = await complietions_client.get_response(message, tools=[get_weather_at_location])
        print(f"Assistant: {response}")

if __name__ == "__main__":
    asyncio.run(main())