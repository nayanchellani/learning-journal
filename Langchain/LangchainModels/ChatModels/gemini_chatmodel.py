from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

llm = ChatGoogleGenerativeAI(model="models/gemini-2.5-flash")
result = llm.invoke("Explain AI to a 5 year old kid")
print(result.content)