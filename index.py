from dotenv import load_dotenv
import os
# import openai
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
# import langchain

#importing apikey from .env file which is ignored by git
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


#normal template send prompt and get response
llm = OpenAI(openai_api_key=api_key, temperature=0.3)
response = llm.invoke("Who made you OpenAI or Google or another company? 1 word answer only")
print(response)