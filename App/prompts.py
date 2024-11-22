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

    Before processing the query, ensure you are using the latest version of the dataframe. Reload the data from the file if any recent modifications have occurred.

    Follow these instructions:
    {instruction_str}
    Query: {query_str}

    Expression: """
)

context = """Purpose:
    The primary role of this agent is to send emails, retrieve data from a dataframe (`df`) in response to user queries, and to perform data modifications when requested, such as adding, deleting, or updating company records.

    - For any query that involves retrieving data, directly analyze the dataframe and provide the requested information.
    - If the query involves adding a new company record, first ensure the company exists, if it does not, abandon the user's task. Then use the `add_record_engine` to add the company name and email to the dataframe. Ensure the new record is properly formatted.
    - If the query involves deleting a company record, first ensure the company exists before attempting to delete. Then use the `delete_record_engine` to remove the record based on the company name provided.
    - If the query involves updating a company's email address, first ensure the company exists before updating, and if it does not, inform the user. Then use the `update_email_engine` to change the email for the company name provided.
    - If the query involves sending an email, ensure the prompt explicitly requests it (e.g., includes the word "send"). Only then should the `send_email_engine` be used to send the email to the specified recipients."""



