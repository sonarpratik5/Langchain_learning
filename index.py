from dotenv import load_dotenv
import os
# import openai
from langchain_openai import OpenAI
from langchain_core.prompts import ChatPromptTemplate
# import langchain

#importing apikey from .env file which is ignored by git
load_dotenv()
if os.getenv("OPENAI_API_KEY"):
    api_key = os.getenv("OPENAI_API_KEY")
else:
    print("OpenAI API key not found")



# #normal template send prompt and get response
llm = OpenAI(openai_api_key=api_key, temperature=0.3, model_name="gpt-3.5-turbo-instruct")
# response = llm.invoke("Who made you OpenAI or Google or another company? 1 word answer only")
# print(response)

prompt = ChatPromptTemplate.from_template("Say My name is {name} in {output_language}")

chain = prompt | llm
response = chain.invoke(
    {
        "output_language": "German",
        "name": "Pratik",
    }
)
print(response)