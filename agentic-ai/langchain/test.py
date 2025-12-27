import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# We are using 2.5 because 1.5 is likely retired/deprecated
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

try:
    print("🤖 Sending request to Gemini 2.5...")
    response = llm.invoke("Say 'System Operational' if you can hear me.")
    print(f"✅ SUCCESS: {response.content}")
except Exception as e:
    print(f"❌ ERROR: {e}")