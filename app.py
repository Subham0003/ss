from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv


load_dotenv()

os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")


app=FastAPI(title="Lanchain Server",Version="1.0",Description='A Simple API Server')

add_routes(app,ChatOpenAI(),path="/openai") 

model=ChatOpenAI
llm=Ollama(model='gemma')
prompt1=ChatPromptTemplate.from_template("write a story on {topic}  wihtin 300 words")
prompt2=ChatPromptTemplate.from_template("write a poem on {topic}  wihtin 100 words")

add_routes(app,prompt1 | model,path='/essay')
add_routes(app,prompt2 | llm,path='/poem')


if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)