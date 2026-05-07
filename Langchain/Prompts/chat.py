from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage , HumanMessage , AIMessage

load_dotenv()
model= ChatGoogleGenerativeAI(model='models/gemini-2.5-flash')
chat_history= [
    SystemMessage(content='you are a helpful AI assistant who provides insightful answers')
]

while True:
        user_input=input("User: ")
        if user_input == 'exit':
            break
        chat_history.append(HumanMessage(content=user_input))
        result= model.invoke(chat_history)
        chat_history.append(AIMessage(content=result.content))
        print('AI: ', result.content)
        
print('Chat history: \n',chat_history)