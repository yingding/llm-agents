from utils.fdyauth import AuthHelper
from dotenv import load_dotenv
from agent_framework.azure import AzureOpenAIChatClient
from agent_framework import BaseChatClient
import logging

# override any existing env variables
load_dotenv(dotenv_path="../.env", override=True)

settings = AuthHelper.load_settings()
az_credential = AuthHelper.test_credential()

# Configure logging for this sample module
if settings.with_logging:
    level=logging.INFO
else:
    level=logging.WARNING

logging.basicConfig(
    level=level,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def create_chat_client(**kwargs) -> BaseChatClient:
    """Create an Azure OpenAIChatClient."""
    model_name = kwargs.get("model_name", settings.model_deployment_name)
    # Initialize a chat agent with Azure OpenAI Chat(Completions) Client
    # You can use either api_key or credential for authentication
    return AzureOpenAIChatClient(
        endpoint=settings.azure_openai_chatcompletions_endpoint,
        deployment_name=model_name,
        # api_version=settings.azure_openai_api_version,
        # api_key=settings.azure_openai_api_key,  # Optional if using AzureCliCredential
        credential=az_credential, # Optional, if using api_key
    )