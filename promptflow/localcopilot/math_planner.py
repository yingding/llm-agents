import asyncio 

# from plugins.math_plugin.Math import Math
# from plugins.math_plugin.math_plugin import MathPlugin
from semantic_kernel.core_plugins.math_plugin import MathPlugin

import semantic_kernel as sk
# from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion, AzureChatCompletion
from semantic_kernel.connectors.ai.ollama import OllamaChatCompletion

# from semantic_kernel.planning.sequential_planner import SequentialPlanner
# from semantic_kernel.planning.sequential_planner.sequential_planner_config import SequentialPlannerConfig
from semantic_kernel.planners.sequential_planner import SequentialPlanner
from semantic_kernel.planners.sequential_planner.sequential_planner_config import SequentialPlannerConfig
from semantic_kernel.connectors.ai.chat_completion_client_base import (
    ChatCompletionClientBase,
)

# from promptflow import tool
from promptflow.core import tool
# from promptflow.connections import AzureOpenAIConnection
from promptflow.connections import OpenAIConnection

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
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
    service_id = "default"
    math_kernel.add_service(
        OllamaChatCompletion(
            ai_model_id=deployment_name,
            service_id=service_id
        ),
    )


    # Import the math plugin
    # math_kernel.import_skill(Math())
    math_kernel.add_plugin(MathPlugin(), plugin_name="math")

    # Create the planner to solve the math problem
    planner = SequentialPlanner(kernel=math_kernel, service_id=service_id)

    # Create a plan to solve the math problem
    ask = "Solve this math problem: " + question
    # plan = asyncio.run(planner.create_plan_async(ask))
    plan = asyncio.run(planner.create_plan(goal=ask))
    # plan = asyncio.run(planner.create_plan(ask))
    # plan = planner.create_plan(goal=ask)



    # Get the result of the math problem
    # math_answer = asyncio.run(plan.invoke(math_kernel)).result
    # math_answer = asyncio.run(plan).result
    math_answer = asyncio.run(plan).result
    # math_answer = asyncio.run(math_kernel.run_async(plan)).result
    
    

    for index, step in enumerate(plan._steps):
        print("Function: " + step.skill_name + "." + step._function.name)
        print("Input vars: " + str(step.parameters.variables))
        print("Outpout vars: " + str(step._outputs))
    print("Result:" + str(math_answer))

    # Add the answer of the math problem to the context
    return "The bot should respond with this answer to the user's question: " + math_answer
