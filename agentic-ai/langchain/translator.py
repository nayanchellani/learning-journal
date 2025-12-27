
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

#  The Model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    google_api_key=api_key
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a professional translator. Translate the user's text into {language}."),
    ("user", "{text}")
])
chain = prompt | llm

print("ENGLISH TO SPANISH TRANSLATOR")
response1 = chain.invoke({
    "text":"Hello , I am learning AGENTIC AI",
    "language":"spanish"
})
print(response1.content)

response2 = chain.invoke({
    "text":"Hello my name is nayan",
    "language":"Hindi"
})
print(response2.content)