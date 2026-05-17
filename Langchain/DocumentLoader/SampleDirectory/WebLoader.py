from langchain_community.document_loaders import WebBaseLoader
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()
model= ChatGoogleGenerativeAI(model='models/gemini-2.5-flash')
prompt = PromptTemplate(
    template='Tell me the latest news from the provided document : {text}',
    input_variables=['text']
)
parser = StrOutputParser()

url= 'https://www.artificialintelligence-news.com/news/malware-on-hugging-face-malicious-software-masquerading-as-openai-release/'
loader = WebBaseLoader(url)

doc = loader.load()

chain = prompt | model | parser
print(chain.invoke({'text':doc}))
