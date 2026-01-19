# pip install agent-framework --pre
# Use `az login` to authenticate with Azure CLI
"""
Docstring for maf.02basic_single_agent_client
This module demonstrates the use of Azure OpenAI Chat Client
as an agent that can interact with tools. 
Sample shows how to create a chat agent 
with ChatAgent(chat_client=..., ...) class.
"""
import asyncio
from agent_framework import (
    BaseChatClient, 
    ChatAgent
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
    completions_client: BaseChatClient = create_chat_client()
    agent = ChatAgent(
        chat_client=completions_client,
        instructions="You are a helpful weather agent.",
        tools=[get_weather_at_location],
    )
    message = "What's the weather in Munich and in Seattle?"
    stream = True
    print(f"User: {message}")
    if stream:
        logger.info("Using streaming response...")
        print("Assistant: ", end="")
        async for chunk in agent.run_stream(message):
            if chunk.text:
                print(chunk.text, end="")
        print("")
    else:
        logger.info("Using non-streaming response...")
        response = await agent.run(message)
        print(f"Assistant: {response}")

if __name__ == "__main__":
    asyncio.run(main())