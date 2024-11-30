<a id="readme-top"></a>
<h1 align="center">📧SmartMailer</h1>

<!-- TABLE OF CONTENTS -->
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
  </ol>

</br>

<!-- ABOUT THE PROJECT -->
<h2 align="center" id="about-the-project">About The Project</h2>

The multi-LLM agent can perform a variety of tasks, including sending personalized emails, querying company data, and managing records such as adding, updating, and deleting company information. It streamlines workflows by leveraging natural language processing to understand and execute tasks with minimal manual intervention.

Key Features:
- **Email Automation:** The agent can send emails to one or more companies based on the email addresses stored in the Excel file. It supports both individual and bulk email sending.
- **Data Querying:** Users can query the Excel file to retrieve company names, emails, and send status, making data retrieval straightforward and efficient.
- **Record Management:** The agent allows users to add new company records, update existing email addresses, or delete records entirely based on company names.
- **Efficient Workflow:** Powered by ``LlamaIndex``, the agent ensures personalized interactions with minimal effort, reducing time spent on repetitive tasks.

By using this AI-driven system, users can automate email campaigns, track communication status, and manage their company data without manual entry, all from a simple command-line interface.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<h3 id="built-with">Built With</h3>

* [![OpenAI]][OpenAI-url] Powers the agent's reasoning and decision-making capabilities using the **GPT-4 Turbo (gpt-4o-mini)** model.
* [![Ollama]][Ollama-url]  A locally hosted LLM leveraging the **Llama 3.1** model for efficient querying and analysis of the Excel dataset.
* [![Pandas]][Pandas-url] Facilitates data manipulation and management within the Excel file.
* [![Smtplib]][Smtplib-url] Handles email sending operations via the SMTP protocol.
* [![PyYAML]][PyYAML-url] Parses email content stored in markdown file for subject and message configuration.
* [![dotenv]][dotenv-url] Manages sensitive configuration settings like email credentials via environment variables.
* [![LlamaIndex]][LlamaIndex-url] Provides a flexible framework for building the AI-driven agent and enabling natural language interaction with tools and data.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
<h2 align="center" id="getting-started">Getting Started</h2>

<h3 id="prerequisites">Prerequisites</h3>

To use this project, you need to install **Ollama** and the **Llama 3.1** model locally. Follow the steps below:

1. **Install Ollama Locally:**
   - Download and install **Ollama** from [Ollama's official website](https://ollama.com/download).
   
2. **Install the Llama 3.1 Model:**
   - After installing Ollama, open a terminal and run the following command to pull the **Llama 3.1** model:
     ```bash
     ollama pull llama3.1
     ```

<h3 id="installation">Installation</h3>

To set up the project locally, follow these steps:

1. **Clone the Repository:**
   - Clone this repository to your local machine:
     ```bash
     git clone git@github.com:maciekmalachowski/SmartMailer.git
     cd SmartMailer
     ```

2. **Create a Virtual Environment:**
   - Create a virtual environment for the project:
     ```bash
     python -m venv ai_venv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```bash
       ai_venv\Scripts\activate
       ```
     - On macOS/Linux:
       ```bash
       source ai_venv/bin/activate
       ```

3. **Install Dependencies:**
   - Install the required dependencies from `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```

4. **Create a `.env` File:**
   - In the root of the project, create a `.env` file with the following environment variables:
     ```
     EMAIL = "example@gmail.com"
     PASSWORD = "examplepass"
     OPENAI_API_KEY = "exampleCZS5njczXqSBlOfavoO-iHOovT3BlbkFJwcWvyftM7ltRSS8Pkby8zGO4HK4TV8iJf4-fsuuNxayHUkmVPtBuFDUfvPq0czDInnsNWh_eEA"
     ```
    - **Google App Passwords:** If you are using a Google account and have 2-factor authentication enabled, you may need to generate an App Password for this project. You can read more about creating App Passwords [here](https://knowledge.workspace.google.com/kb/how-to-create-app-passwords-000009237).
      
   - **Optional (but recommended):** If you have limited space on your main disk, you can specify the location for caching the Ollama models by adding the following variable to the `.env` file:
     ```
     OLLAMA_MODELS = "D:\Example\ollama_models"
     ```
     This will redirect Ollama's model cache to the specified location.

Once these steps are completed, the environment will be ready to run the project!

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
<h2 align="center" id="usage">Usage</h2>

To use this AI-driven email agent, follow the steps below:

1. **Activate the Virtual Environment:**
   
   - Before running the agent, make sure to activate the virtual environment:
     - On Windows:
       ```bash
       ai_venv\Scripts\activate
       ```
     - On macOS/Linux:
       ```bash
       source ai_venv/bin/activate
       ```

3. **Run the Agent:**
   
   - Once the environment is activated, you can start the agent by running:
     ```bash
     python agent.py
     ```
   - This will load the agent, and you will be prompted to enter commands.

4. **Example Prompts:**
   
   You can interact with the agent by typing different prompts. Here are some examples:

   - **Query the Excel file:**
     - Retrieve all company names and emails:
       ```text
       Retrieve all company names and emails.
       ```
   
   - **Add a new record:**
     - Add a company with name and email:
       ```text
       Add company named example1 with email example@gmail.com.
       ```

   - **Delete a record:**
     - Delete a company record based on the company name:
       ```text
       Delete company named example1.
       ```

   - **Update a record:**
     - Update the email for a specific company:
       ```text
       Update email for company named example1 to agent@gmail.com.
       ```

   - **Send an email:**
     - Send an email to a company name listed in the Excel file:
       ```text
       Send email to company named example1.
       ```

   - **Check sent emails:**
     - Query the status of emails that have been sent:
       ```text
       Which emails have been sent?
       ```

5. **Excel File Structure:**
   
   The Excel file (`company_data.xlsx`) used by the agent contains the following columns:
   - **Company_name:** The name of the company.
   - **Company_email:** The email address of the company.
   - **Send_status:** A field that tracks the status of the email sent to the company (e.g., sent, pending).

6. **Updating Email Title and Subject:**
   
   You can easily customize the email's **Subject** and **Message** by updating the `email.md` markdown file.
   This file contains the following structure:
   ```markdown
    ---
    Subject: "TEST SUBJECT"
    Message: "TEST MESSAGE"
    ---
   ```

   Simply replace `"TEST SUBJECT"` and `"TEST MESSAGE"` with the desired email title and content. These changes will be reflected in the emails the agent sends.
   
Simply enter the prompts, and the agent will perform the corresponding actions like querying, adding, deleting, updating records, or sending emails.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
<h2 align="center" id="license">License</h2>

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->

[product-screenshot]: images/screenshot.png

[OpenAI]: https://img.shields.io/badge/OpenAI-ffffff?style=for-the-badge&logo=OpenAI&logoColor=black
[OpenAI-url]: https://openai.com/index/openai-api/

[LlamaIndex]: https://img.shields.io/badge/LlamaIndex-ffffff?style=for-the-badge&logo=llama_index&logoColor=black
[LlamaIndex-url]: https://www.llamaindex.ai

[Ollama]: https://img.shields.io/badge/Ollama-ffffff?style=for-the-badge&logo=ollama&logoColor=black
[Ollama-url]: https://ollama.com

[Pandas]: https://img.shields.io/badge/Pandas-ffffff?style=for-the-badge&logo=pandas&logoColor=black
[Pandas-url]: https://pandas.pydata.org

[Smtplib]: https://img.shields.io/badge/Smtplib-ffffff?style=for-the-badge&logo=gmail&logoColor=black
[Smtplib-url]: https://docs.python.org/3/library/smtplib.html

[PyYAML]: https://img.shields.io/badge/PyYAML-ffffff?style=for-the-badge&logo=YAML&logoColor=black
[PyYAML-url]: https://pypi.org/project/PyYAML/

[dotenv]: https://img.shields.io/badge/dotenv-ffffff?style=for-the-badge&logo=dotenv&logoColor=black
[dotenv-url]: https://pypi.org/project/python-dotenv/
