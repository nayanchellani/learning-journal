from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
from app import workflow
from langchain_core.messages import HumanMessage, AIMessage

app = FastAPI(
    title="LangGraph Chatbot Backend",
    description="FastAPI backend for LangGraph Chatbot",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatMessagePayload(BaseModel):
    message: str
    thread_id: str

class MessageItem(BaseModel):
    role: str
    content: str

class ChatResponse(BaseModel):
    messages: List[MessageItem]

@app.post("/api/chat", response_model=ChatResponse)
async def chat(payload: ChatMessagePayload):
    try:
        config = {"configurable": {"thread_id": payload.thread_id}}
        
        state = workflow.invoke(
            {"messages": [HumanMessage(content=payload.message)]},
            config=config
        )
        
        formatted_messages = []
        for msg in state.get("messages", []):
            role = "user" if isinstance(msg, HumanMessage) else "assistant"
            content = msg.content if isinstance(msg.content, str) else str(msg.content)
            formatted_messages.append(MessageItem(role=role, content=content))
            
        return ChatResponse(messages=formatted_messages)
    except Exception as e:
        print(f"Error in chat endpoint: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to process chat: {str(e)}")

@app.get("/api/history/{thread_id}", response_model=ChatResponse)
async def get_history(thread_id: str):
    try:
        config = {"configurable": {"thread_id": thread_id}}
        state = workflow.get_state(config)
        
        formatted_messages = []
        if state and state.values and "messages" in state.values:
            for msg in state.values["messages"]:
                role = "user" if isinstance(msg, HumanMessage) else "assistant"
                content = msg.content if isinstance(msg.content, str) else str(msg.content)
                formatted_messages.append(MessageItem(role=role, content=content))
                
        return ChatResponse(messages=formatted_messages)
    except Exception as e:
        print(f"Error in history endpoint: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to retrieve history: {str(e)}")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
