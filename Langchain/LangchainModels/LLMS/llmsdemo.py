from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

llm = GoogleGenerativeAI(model="models/gemini-2.5-flash")
result = llm.invoke("Explain AI to a 5 year old kid")
print(result)