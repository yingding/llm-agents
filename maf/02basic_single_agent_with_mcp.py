# pip install agent-framework --pre
# Use `az login` to authenticate with Azure CLI
"""
Docstring for maf.02basic_single_agent_with_mcp
This module demonstrates the use of ChatAgent with HostedMCPTool
to access remote Microsoft Learn MCP endpoint.
It uses an local AgentThread to maintain conversation state across multiple interactions.
"""

import asyncio
from agent_framework import (
    BaseChatClient, 
    ChatAgent,
    HostedMCPTool,
    MCPStreamableHTTPTool,
)
from typing import TYPE_CHECKING, Any
from pydantic import Field
import logging
from random import randint
from utils.model_client import create_chat_client

logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    from agent_framework import AgentProtocol, AgentThread, ChatMessage

async def handle_approvals_without_thread(query: str, agent: "AgentProtocol"):
    """When we don't have a thread, we need to ensure we return with the input, approval request and approval."""
    from agent_framework import ChatMessage

    result = await agent.run(query)
    while len(result.user_input_requests) > 0:
        new_inputs: list[Any] = [query]
        for user_input_needed in result.user_input_requests:
            print(
                f"User Input Request for function from {agent.name}: {user_input_needed.function_call.name}"
                f" with arguments: {user_input_needed.function_call.arguments}"
            )
            new_inputs.append(ChatMessage(role="assistant", contents=[user_input_needed]))
            user_approval = input("Approve function call? (y/n): ")
            new_inputs.append(
                ChatMessage(role="user", contents=[user_input_needed.create_response(user_approval.lower() == "y")])
            )

        result = await agent.run(new_inputs)
    return result


async def   handle_approvals_with_thread(query: str, agent: "AgentProtocol", thread: "AgentThread"):
    """
    Here we let the thread deal with the previous responses, and we just rerun with the approval.
    AgentThread stores the conversation state including user inputs and approvals.
    """
    from agent_framework import ChatMessage

    result = await agent.run(query, thread=thread, store=True)
    while len(result.user_input_requests) > 0:
        new_input: list[Any] = []
        for user_input_needed in result.user_input_requests:
            print(
                f"User Input Request for function from {agent.name}: {user_input_needed.function_call.name}"
                f" with arguments: {user_input_needed.function_call.arguments}"
            )
            user_approval = input("Approve function call? (y/n): ")
            new_input.append(
                ChatMessage(
                    role="user",
                    contents=[user_input_needed.create_response(user_approval.lower() == "y")],
                )
            )
        result = await agent.run(new_input, thread=thread, store=True)
    return result

async def print_thread_messages(thread: "AgentThread"):
    """Print all messages stored in the AgentThread's message store."""
    print("\nAgentThread stored messages:\n")
    messages: list["ChatMessage"] = await thread.message_store.list_messages()
    # add index for messages
    for idx, message in enumerate(messages):
        print(f"[{idx}] {message.role}: {message.text}")

async def run_remote_mcp_with_thread() -> None:
    """Example of Agent access to remote MCP with thread streaming."""
    # Initialize a chat agent with Azure OpenAI Chat(Completions) Client
    completions_client: BaseChatClient = create_chat_client()
    
    # source https://learn.microsoft.com/en-us/training/support/mcp
    MSLEARN_MCP_URL = "https://learn.microsoft.com/api/mcp"

    async with ChatAgent(
        chat_client=completions_client,
        name="MSDocsAgent",
        instructions="You are a helpful weather agent.",
        tools=HostedMCPTool(
            name="Microsoft Learn MCP",
            url=MSLEARN_MCP_URL,
            # we don't require approval for microsoft_docs_search tool calls in ms learn mcp.
            # but we do for any other tool, MS Learn MCP has multiple tools.
            # approval_mode={"never_require_approval": ["microsoft_docs_search"]},
            # approval_mode="never_require",
            # we require approval for all function calls
            approval_mode="always_require",
        )
    ) as agent:
        # # First query
        # query1 = "How to create an Azure storage account using az cli?"
        # print(f"User: {query1}")
        # result1 = await handle_approvals_without_thread(query1, agent)
        # print(f"{agent.name}: {result1}\n")
        # print("\n=======================================\n")
        # # Second query
        # query2 = "What is Microsoft Agent Framework?"
        # print(f"User: {query2}")
        # result2 = await handle_approvals_without_thread(query2, agent)
        # print(f"{agent.name}: {result2}\n")

        # First query
        thread: AgentThread = agent.get_new_thread()
        query1 = "How to create an Azure storage account using az cli?"
        print(f"User: {query1}")
        result1 = await handle_approvals_with_thread(query1, agent, thread)
        print(f"{agent.name}: {result1}\n")
        print("\n=======================================\n")
        # Second query
        query2 = "What is Microsoft Agent Framework?"
        print(f"User: {query2}")
        result2 = await handle_approvals_with_thread(query2, agent, thread)
        print(f"{agent.name}: {result2}\n")
        # print the AgentThread messages stored
        # state = await thread.serialize()
        ## display the local AgentThread state
        # print("#"*20)
        # print("## Total AgentThread State")
        # await print_thread_messages(thread)


if __name__ == "__main__":
    asyncio.run(run_remote_mcp_with_thread())