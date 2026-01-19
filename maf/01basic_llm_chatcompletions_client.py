# pip install agent-framework --pre
# Use `az login` to authenticate with Azure CLI
"""
Docstring for maf.01basic_llm_chatcompletions_client
This module demonstrates how to use the Azure OpenAI Chat Completions client
to call the chat completions endpoint of the model directly
"""
import asyncio
from agent_framework import BaseChatClient
from agent_framework import ChatMessage
from utils.model_client import create_chat_client


async def main() -> None:
    # Initialize a chat agent with Azure OpenAI Chat(Completions) Client
    chat_client: BaseChatClient = create_chat_client()
    messages = [
        ChatMessage(role="system", text="You are a helpful assistant."),
        ChatMessage(role="user", text="Write a haiku about Agent Framework.")
    ]

    response = await chat_client.get_response(messages)
    print(response.messages[0].text)


if __name__ == "__main__":
    asyncio.run(main())