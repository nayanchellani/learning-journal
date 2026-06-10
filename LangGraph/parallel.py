from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict
from dotenv import load_dotenv
load_dotenv()
model = ChatGoogleGenerativeAI(model="models/gemini-2.5-flash")

class BlogState(TypedDict):
    title: str
    outline: str
    content: str
    
    
def generate_outline(state: BlogState) -> BlogState:
    title = state['title']
    prompt = f'Generate an outline for a blog on the topic - {title}'
    outline = model.invoke(prompt).content
    state['outline'] = outline
    return state

def generate_blog(state: BlogState) -> BlogState:
    title = state['title']
    outline = state['outline']
    prompt = f'Generate a blog on the topic : {title} using the outline provided : - {outline}'
    content = model.invoke(prompt).content
    state['content']=content
    return state

graph = StateGraph(BlogState)
graph.add_node('generate_outline',generate_outline)
graph.add_node('generate_blog',generate_blog)
graph.add_edge(START,'generate_outline')
graph.add_edge('generate_outline','generate_blog')
graph.add_edge('generate_blog', END)
workflow = graph.compile()

initial_state = {'title':'Corruption'}
print(workflow.invoke(initial_state))
print(workflow.invoke(initial_state))