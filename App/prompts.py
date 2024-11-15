from llama_index.core import PromptTemplate


instruction_str = """\
    1. Convert the query to executable Python code using Pandas.
    2. If the query involves retrieving company names or emails, generate code to extract the requested information from the DataFrame.
    3. If the query involves sending emails, format the necessary data (e.g., company name and email) and use the provided `send_email` function to perform the task.
    4. If the query involves adding new records, the user will provide the company name and email. Format the provided data and use the `add_company_to_dataframe` function to add the new record to the dataframe.
    5. The final line of code should be a Python expression that can be called with the `eval()` function.
    6. PRINT ONLY THE EXPRESSION.
    7. Do not quote the expression."""



new_prompt = PromptTemplate(
    """\
    You are working with a pandas dataframe in Python.
    The name of the dataframe is `df`.
    This is the result of `print(df.head())`:
    {df_str}

    Your responsibilities include:
    1. Retrieving company names and emails from the dataframe based on user queries.
    2. Using the provided `send_email` function to send emails to the retrieved companies and their respective emails.
    3. Adding new company data to the dataframe using the `add_company_to_dataframe` function. The user will provide the company name and email in the prompt.

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
