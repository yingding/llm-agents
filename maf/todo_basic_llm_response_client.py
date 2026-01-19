# pip install agent-framework --pre
# Use `az login` to authenticate with Azure CLI
import os
import asyncio
from dotenv import load_dotenv
from agent_framework.azure import AzureOpenAIResponsesClient
from agent_framework.azure import AzureOpenAIChatClient
from agent_framework import ChatAgent

# from azure.identity import AzureCliCredential
from utils.fdyauth import AuthHelper
from dotenv import load_dotenv
# override any existing env variables
load_dotenv(dotenv_path=".env", override=True)

settings = AuthHelper.load_settings()
az_credential = AuthHelper.test_credential()

async def main():
    # Initialize a chat agent with Azure OpenAI Responses
    # the endpoint, deployment name, and api version can be set via environment variables
    # or they can be passed in directly to the AzureOpenAIResponsesClient constructor
    agent = AzureOpenAIResponsesClient(
        endpoint=settings.azure_openai_responses_endpoint,
        deployment_name=settings.model_deployment_name,
        # api_version=settings.azure_openai_api_version,
        # api_key=settings.azure_openai_api_key,  # Optional if using AzureCliCredential
        credential=az_credential, # Optional, if using api_key
    ).as_agent(
        name="HaikuBot",
        instructions="You are an upbeat assistant that writes beautifully.",
    )

    print(await agent.run("Write a haiku about Microsoft Agent Framework."))

if __name__ == "__main__":
    asyncio.run(main())