from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic'],
    
)
prompt2 = PromptTemplate(
    template='Generate a short summary in bullet points on {topic}',
    input_variables=['topic'],
    
)
parser = StrOutputParser()
chain =  prompt1 | model | parser | prompt2 | model | parser
result = chain.invoke({'topic': input('Enter topic for detailed report and summary')})
print(result)