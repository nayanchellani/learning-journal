from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict, Annotated
from dotenv import load_dotenv
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver
import os

load_dotenv()
load_dotenv(os.path.join(os.path.dirname(__file__), "..", "..", ".env"))
load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))

class ChatBotState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

model = ChatGoogleGenerativeAI(model="models/gemini-2.5-flash")

graph = StateGraph(ChatBotState)

def chat_node(state: ChatBotState):
    messages = state["messages"]
    response = model.invoke(messages)
    print(f"Bot response: {response.content}")
    return {"messages": [response]}

graph.add_node("chat_node", chat_node)
graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)

memory = MemorySaver()
workflow = graph.compile(checkpointer=memory)
