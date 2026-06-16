from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict
from dotenv import load_dotenv
from typing import Annotated
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph.message import add_messages

load_dotenv()
model = ChatGoogleGenerativeAI(model="models/gemini-2.5-flash")

class ChatBotState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
    
graph = StateGraph(ChatBotState)

def chat_node(state: ChatBotState):
    messages = state["messages"]  
    response = model.invoke(messages)
    print(response.content)
    return {"messages": [response]}

graph.add_node("chat_node", chat_node)
graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)

workflow = graph.compile()


initial_state = {
    "messages":[
        HumanMessage(content=input("You: "))
    ]
        
}
workflow.invoke(initial_state)



    