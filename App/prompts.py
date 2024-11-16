from llama_index.core import PromptTemplate

instruction_str = """\
1. Convert the query to executable Python code using Pandas.
2. The code should retrieve data directly from the dataframe based on the query.
3. The dataframe is named `df`.
4. The final line of code should be a Python expression that can be executed with the `eval()` function.
5. PRINT ONLY THE EXPRESSION.
6. Do not quote the expression."""

new_prompt = PromptTemplate(
    """\
    You are working with a pandas dataframe containing company names and emails in Python.
    The name of the dataframe is `df`.
    This is the result of `print(df.head())`:
    {df_str}

    Follow these instructions:
    {instruction_str}
    Query: {query_str}

    Expression: """
)

context = """Purpose: 
The primary role of this agent is to retrieve data from a dataframe (`df`) in response to user queries and to send emails when requested.

- For any query that involves retrieving data, directly analyze the dataframe to provide the requested information.
- If the query involves sending an email, use the provided `email_engine` to send the email based on the necessary data.
- Avoid unnecessary observations, thoughts, or steps.
- Focus on returning the data or sending the email immediately, and finalize the task after the first response."""

