from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
model= ChatGoogleGenerativeAI(model='models/gemini-2.5-flash')
prompt = PromptTemplate(
    template='Summarise the key details from the given text : {text}',
    input_variables=['text']
)
parser = StrOutputParser()
def load_pdf_text(_):
    loader = PyPDFLoader('DocumentLoader\sample.pdf')
    docs = loader.load()
    return docs

loadpdf = RunnableLambda(load_pdf_text)

chain = {'text':loadpdf} | prompt | model | parser
print(chain.invoke(None))
print(load_pdf_text)
