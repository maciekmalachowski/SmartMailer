import os
import pandas as pd
from dotenv import load_dotenv
from llama_index.llms.ollama import Ollama
from llama_index.experimental.query_engine import PandasQueryEngine
from prompts import instruction_str, new_prompt

load_dotenv()

data_path = os.path.join("data", "company_data.xlsx")
company_df = pd.read_excel(data_path)

llm = Ollama(model="mistral", request_timeout=60.0)

company_query_engine = PandasQueryEngine(df=company_df, verbose=True, instruction_str=instruction_str, llm=llm)

company_query_engine.update_prompts({"pandas_prompt": new_prompt})

company_query_engine.query("Display me all company names")