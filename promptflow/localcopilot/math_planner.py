import asyncio
import logging
import warnings
# https://stackoverflow.com/questions/14463277/how-to-disable-python-warnings
# warnings.filterwarnings("ignore", message="Invalid type NoneType")

# from pydantic import UrlConstraints
# from pydantic.networks import Url
# from typing import Annotated
# import semantic_kernel.kernel_pydantic as kernel_pydantic

# override, only necessary for AzureChatCompletion
# kernel_pydantic.HttpsUrl = Annotated[Url, UrlConstraints(max_length=2083, allowed_schemes=["https", "http"])]

# the core_plugins.math_plugin has no multiply function thus use a custom math plugin
# from semantic_kernel.core_plugins.math_plugin import MathPlugin
from plugins.math_plugin.math_plugin import MathPlugin as MyMathPlugin

import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion, AzureChatCompletion
from semantic_kernel.connectors.ai.ollama import OllamaChatCompletion

# from semantic_kernel.planning.sequential_planner import SequentialPlanner
# from semantic_kernel.planning.sequential_planner.sequential_planner_config import SequentialPlannerConfig
from semantic_kernel.planners.sequential_planner import SequentialPlanner
from semantic_kernel.planners.function_calling_stepwise_planner import FunctionCallingStepwisePlanner, FunctionCallingStepwisePlannerOptions
from semantic_kernel.planners.sequential_planner.sequential_planner_config import SequentialPlannerConfig
from semantic_kernel.connectors.ai.chat_completion_client_base import (
    ChatCompletionClientBase,
)
from semantic_kernel.connectors.ai.function_choice_behavior import FunctionChoiceBehavior 
from semantic_kernel.connectors.ai.chat_completion_client_base import ChatCompletionClientBase
from semantic_kernel.connectors.ai.open_ai.prompt_execution_settings.azure_chat_prompt_execution_settings import (
    AzureChatPromptExecutionSettings,
)
from semantic_kernel.connectors.ai.ollama.ollama_prompt_execution_settings import OllamaChatPromptExecutionSettings
from semantic_kernel.connectors.ai.open_ai.prompt_execution_settings.open_ai_prompt_execution_settings import (
    OpenAIChatPromptExecutionSettings,
)
from semantic_kernel.contents.chat_history import ChatHistory
from semantic_kernel.functions.kernel_arguments import KernelArguments

# from promptflow import tool
from promptflow.core import tool
# from promptflow.connections import AzureOpenAIConnection
from promptflow.connections import OpenAIConnection
from semantic_kernel.utils.logging import setup_logging

from openai import OpenAI, AsyncOpenAI
from openai._utils._logs import logger as openai_logger
from openai._utils._logs import httpx_logger as openai_httpx_logger

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
# .com/en-us/semantic-kernel/concepts/plugins/

# https://learn.microsoft.com/en-us/semantic-kernel/get-started/quick-start-guide?pivots=programming-language-python
@tool
def chat(
    question: str,
    deployment_name: str,
    connection: OpenAIConnection,
):
    # Create kernel for math plugin
    math_kernel = sk.Kernel()

    # Add the chat service
    service_id = "default"
    # service_id = "ollama"

    # slice the base_url to remove the last 3 characters
    # host must be http://localhost:11434, not http://localhost:11434/v1 
    # base_url = "http://localhost:11434/v1"
    # used for ollama chat completion host
    host = connection.base_url[:-3]

    # https://github.com/microsoft/semantic-kernel/issues/5931
    # chat_completion = OllamaChatCompletion(
    #     ai_model_id = deployment_name,
    #     host = host
    # )
    
    # chat_completion = AzureChatCompletion(
    #     deployment_name=deployment_name,
    #     api_key=connection.api_key,
    #     endpoint=host,
    # )
    
    '''create an async openai client with base url to the local ollama server for function calling'''
    async_client = AsyncOpenAI(
        api_key=connection.api_key,
        base_url=connection.base_url,
    )
    
    chat_completion = OpenAIChatCompletion(
        ai_model_id=deployment_name,
        async_client=async_client,
    )

    math_kernel.add_service(
        service=chat_completion,
    )

    # Set the logging level for  semantic_kernel.kernel to DEBUG.
    setup_logging()
    # logging.getLogger("math_kernel").setLevel(logging.DEBUG)
    # level = logging.CRITICAL
    level = logging.ERROR
    logging.getLogger("math_kernel").setLevel(level)
    # suppress oepntelemetry no token warning
    logging.getLogger("opentelemetry.attributes").setLevel(level)
    # openai_logger.setLevel(level)
    # openai_httpx_logger.setLevel(level)

    # Import the math plugin
    math_kernel.add_plugin(MyMathPlugin(), plugin_name="MyMath")

    # solve the math problem
    # execution_settings = AzureChatPromptExecutionSettings(tool_choice="auto")
    # auto, required, none
    # https://devblogs.microsoft.com/semantic-kernel/introducing-python-function-choice-behavior-streamlining-ai-model-configuration/
    # execution_settings = AzureChatPromptExecutionSettings(function_choice_behavior="auto")
    # execution_settings.function_choice_behavior = FunctionChoiceBehavior.Auto(filters={"included_plugins": ["MyMath"]})
    
    # uncomment the following lines to use the required function choice behavior
    # at the time or writing the OllamaChatComletion does not support function calling on semantic kernel 1.11.0
    execution_settings = OpenAIChatPromptExecutionSettings(
        max_tokens=2000,
        temperature=0.01,
        top_p=0.8,
        function_choice_behavior="auto"
    )

    # execution_settings = AzureChatPromptExecutionSettings(
    #     max_tokens=2000,WARNING
    #     temperature=0.01,
    #     top_p=0.8,
    #     function_choice_behavior="required"
    # )

    # execution_settings = OllamaChatPromptExecutionSettings(
    #     function_choice_behavior="required"
    # )
    execution_settings.function_choice_behavior = FunctionChoiceBehavior.Auto(filters={"included_plugins": ["MyMath"]})
    # execution_settings.function_choice_behavior = FunctionChoiceBehavior.Required(filters={"included_plugins": ["MyMath"]})
    # execution_settings.function_call_behavior = FunctionCallBehavior.EnableFunctions(auto_invoke=True, filters={})
    

    # Create a planner
    # https://github.com/microsoft/semantic-kernel/issues/5661
    # options = FunctionCallingStepwisePlannerOptions(
    #     max_iterations=10,
    #     execution_settings=execution_settings,
    # )

    # planner = FunctionCallingStepwisePlanner(
    #     service_id=service_id, 
    #     options=options)
    # goal = "Solve this math problem: " + question

    # async def create_and_execute_plan():
    #     plan = await planner.invoke(kernel=math_kernel, question=goal)
    #     return await plan.run()
    
    # math_answer = asyncio.run(create_and_execute_plan())

    # create a history of the conversation
    history = ChatHistory()
    ask = "Solve this math problem: " + question
    history.add_message({"role": "user", "content": ask})

    # Get the response from the AI
    math_answer = None

    math_answer = asyncio.run(chat_completion.get_chat_message_content(
        chat_history=history,
        settings=execution_settings,
        kernel=math_kernel,
        arguments=KernelArguments()
    ))

    # The client is already async openai client
    # math_answer = chat_completion.get_chat_message_content(
    #     chat_history=history,
    #     settings=execution_settings,
    #     kernel=math_kernel,
    #     arguments=KernelArguments()
    # )
    
    # Print the results
    print("Assistant > " + str(math_answer))

    # Add the message from the agent to the chat history
    # history.add_message(math_answer)

    # for index, step in enumerate(plan._steps):
    #     print("Function: " + step.skill_name + "." + step._function.name)
    #     print("Input vars: " + str(step.parameters.variables))
    #     print("Outpout vars: " + str(step._outputs))
    # print("Result:" + str(math_answer))


    # Add the answer of the math problem to the context as system instruction
    return f"The bot should respond with this answer to the user's question, {str(math_answer).strip()}"
