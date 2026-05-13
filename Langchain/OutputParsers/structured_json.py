from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import ResponseSchema, StructuredOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
schema = [
    ResponseSchema(name='fact 1', description ='Fact 1 about the topic'),
    ResponseSchema(name='fact 2', description ='Fact 2 about the topic'),
    ResponseSchema(name='fact 3', description ='Fact 3 about the topic'),
    ResponseSchema(name='fact 4', description ='Fact 4 about the topic'),
    ResponseSchema(name='fact 5', description ='Fact 5 about the topic')
]
parser = StructuredOutputParser.from_response_schemas(schema)
template= PromptTemplate(
    template='Tell me 5 interesting facts about {topic} {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser
result = chain.invoke({'topic': 'vs code'})
print(result)