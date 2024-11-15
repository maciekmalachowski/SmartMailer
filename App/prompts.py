from llama_index.core import PromptTemplate


instruction_str = """\
    1. Convert the query to executable Python code using Pandas.
    2. The final line of code should be a Python expression that can be called with the `eval()` function.
    3. The code should represent a solution to the query.
    4. PRINT ONLY THE EXPRESSION.
    5. Do not quote the expression."""

new_prompt = PromptTemplate(
    """\
    You are working with a pandas dataframe in Python.
    The name of the dataframe is `df`.
    This is the result of `print(df.head())`:
    {df_str}

    Follow these instructions:
    {instruction_str}
    Query: {query_str}

    Expression: """
)

context = """Purpose: The primary role of this agent is to retrieve relevant data from a specified 
            dataframe and send emails to the recipients listed within. Additionally, if requested 
            by the user, the agent can add new data entries to the dataframe, ensuring the data 
            remains current and relevant. This agent prioritizes accuracy and clarity in data 
            handling, providing timely email responses based on the information available and 
            any new data added upon user request."""
