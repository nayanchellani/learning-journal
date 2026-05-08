from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv
load_dotenv()
model = ChatGoogleGenerativeAI(model='models/gemini-2.5-flash')
chat_template = ChatPromptTemplate([
    ('system','you are a helpful {domain}expert'),
    ('human','Explain {topic} in simple terms to a beginner')
    
 ])
print(model.invoke(chat_template.invoke({'domain':'Software engineering', 'topic':'NLP'})))
