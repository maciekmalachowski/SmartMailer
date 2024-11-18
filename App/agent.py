import os
import pandas as pd
from llama_index.llms.ollama import Ollama
from llama_index.experimental.query_engine import PandasQueryEngine
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.core.agent.react import ReActChatFormatter
from prompts import instruction_str, new_prompt, context
from mailing import send_email_engine
from df_adjusting import add_record_engine, delete_record_engine, update_email_engine
from data_manager import company_df


# Initialize the LLMs from Ollama
llm = Ollama(model="mistral", request_timeout=60.0)
agent_llm = Ollama(model="llama3.1", request_timeout=60.0)

# Create a PandasQueryEngine for querying the company DataFrame using the given mistrl LLM
company_query_engine = PandasQueryEngine(df=company_df, verbose=False, instruction_str=instruction_str, llm=llm)
company_query_engine.update_prompts({"pandas_prompt": new_prompt})

# Define list of tools
tools = [
    QueryEngineTool(
        query_engine=company_query_engine,
        metadata=ToolMetadata(
            name="company_data",
            description="This tool retrieves information about company names and their associated email addresses."
        )
    ),
    add_record_engine,
    delete_record_engine,
    update_email_engine,
    send_email_engine,
]

# Initialize the ReAct agent
agent = ReActAgent.from_tools(
    tools=tools,
    llm=agent_llm,
    verbose=True,
    max_iterations=15,
    react_chat_formatter=ReActChatFormatter.from_defaults(context=context)
)

# The user inputs a prompt, and the agent provides a result based on the tools available
while (prompt := input("Enter a prompt (q to quit): ")) != "q":
    result = agent.chat(prompt)
    print(result)
