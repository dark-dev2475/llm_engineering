#the langserve is used too  deploy you langchain apllliacations and it is alo o used to create api endpoints

from  langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from  langchain_core.output_parsers import StrOutputParser
from fastapi import FastAPI
import uvicorn
from langserve import add_routes

from dotenv import load_dotenv
load_dotenv()

#x sse starlette you need to pip install

system_template="translate this text in to {language}"

prompt_template =  ChatPromptTemplate.from_messages([
   ("system", system_template),
   ("user", "{text}")
   
])

model=ChatGoogleGenerativeAI(model="gemini-1.5-flash",convert_system_message_to_human=True)

parser=StrOutputParser()

chain=prompt_template|model|parser


app=FastAPI(
    title="my llm api",
    description="its very good",
    version="1.0"
)

add_routes(
    app,
    chain,
    path="/chain"
)


if __name__ == "__main__":
    uvicorn.run(app,host="localhost",port=8080)