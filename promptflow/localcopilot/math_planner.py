import asyncio 

# from plugins.math_plugin.Math import Math
# from plugins.math_plugin.math_plugin import MathPlugin
from semantic_kernel.core_plugins.math_plugin import MathPlugin

import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion, AzureChatCompletion
from semantic_kernel.connectors.ai.ollama import OllamaChatCompletion

# from semantic_kernel.planning.sequential_planner import SequentialPlanner
# from semantic_kernel.planning.sequential_planner.sequential_planner_config import SequentialPlannerConfig
from semantic_kernel.planners.sequential_planner import SequentialPlanner
from semantic_kernel.planners.sequential_planner.sequential_planner_config import SequentialPlannerConfig
from semantic_kernel.connectors.ai.chat_completion_client_base import (
    ChatCompletionClientBase,
)
from semantic_kernel.connectors.ai.function_choice_behavior import FunctionChoiceBehavior 
from semantic_kernel.connectors.ai.function_call_behavior import FunctionCallBehavior
from semantic_kernel.connectors.ai.chat_completion_client_base import ChatCompletionClientBase
from semantic_kernel.connectors.ai.open_ai.prompt_execution_settings.azure_chat_prompt_execution_settings import (
    AzureChatPromptExecutionSettings,
)
from semantic_kernel.contents.chat_history import ChatHistory

# from promptflow import tool
from promptflow.core import tool
# from promptflow.connections import AzureOpenAIConnection
from promptflow.connections import OpenAIConnection

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
# .com/en-us/semantic-kernel/concepts/plugins/
@tool
def chat(
    question: str,
    deployment_name: str,
    connection: OpenAIConnection,
):
    # Create kernel for math plugin
    # math_kernel = sk.Kernel(log=sk.NullLogger())
    math_kernel = sk.Kernel()

    # Add the chat service
    # service_id = "default"
    # math_kernel.add_service(
    #     OllamaChatCompletion(
    #         ai_model_id=deployment_name,
    #         service_id=service_id
    #     ),
    # )

    # chat_completion = AzureChatCompletion(
    #         deployment_name=deployment_name,
    #         api_key= connection.api_key,
    #         endpoint= connection.base_url,
    # )
    
    chat_completion = OllamaChatCompletion(
             ai_model_id=deployment_name
    )

    math_kernel.add_service(
        chat_completion,
    )


    # Import the math plugin
    # math_kernel.import_skill(Math())
    math_kernel.add_plugin(MathPlugin(), plugin_name="Math")

    # Create the planner to solve the math problem
    execution_settings = AzureChatPromptExecutionSettings(tool_choice="auto")
    # https://devblogs.microsoft.com/semantic-kernel/introducing-python-function-choice-behavior-streamlining-ai-model-configuration/
    execution_settings.function_choice_behavior = FunctionChoiceBehavior.Auto(filters={})
    # execution_settings.function_call_behavior = FunctionCallBehavior.EnableFunctions(auto_invoke=True, filters={})
    
    # planner = SequentialPlanner(kernel=math_kernel)

    # # Create a plan to solve the math problem
    # ask = "Solve this math problem: " + question
    # # plan = asyncio.run(planner.create_plan_async(ask))
    # plan = asyncio.run(planner.create_plan(goal=ask))
    # # plan = asyncio.run(planner.create_plan(ask))
    # # plan = planner.create_plan(goal=ask)

    # create a history of the conversation
    history = ChatHistory()
    ask = "Solve this math problem: " + question
    history.add_message({"role": "user", "content": ask})

    # Get the response from the AI
    math_answer = asyncio.run(chat_completion.get_chat_message_content(
        chat_history=history,
        settings=execution_settings,
        kernel=math_kernel,
    ))
    
    print(ask)
    # print(f"type {type(math_answer)}") 



    # Get the result of the math problem
    # math_answer = asyncio.run(plan.invoke(math_kernel)).result
    # math_answer = asyncio.run(plan).result
    # math_answer = asyncio.run(plan).result
    # math_answer = asyncio.run(math_kernel.run_async(plan)).result
    
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
    return f"The bot should respond with this answer to the user's question: {str(math_answer).strip()}"
