from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict
from dotenv import load_dotenv

load_dotenv()
model = ChatGoogleGenerativeAI(model="models/gemini-2.5-flash")

class LLMState(TypedDict):
    question:str
    answer:str

graph = StateGraph(LLMState)
def ask_llm(state: LLMState) -> LLMState:
    question = state['question']
    prompt = f'answer the following question in a polite manner to a 5 year old kid {question}'
    answer = model.invoke(prompt)
    state['answer']=answer.content
    return state
    
    


graph.add_node('llm_demo',ask_llm)
graph.add_edge(START, 'llm_demo')
graph.add_edge('llm_demo', END)
workflow = graph.compile()
final_result = workflow.invoke({'question':'What is the meaning of an LLM'})
print(final_result)