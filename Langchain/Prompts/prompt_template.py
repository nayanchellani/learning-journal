from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
prompt = PromptTemplate(
    template='Explain {topic} to a {audience}',
    input_variables=["topic","audience"],
    validate_template=True
)
formatted_prompt= prompt.format(
    topic='Machine Learning',
    audience='Beginner'
)
model= ChatGoogleGenerativeAI(model='models/gemini-2.5-flash')
print(model.invoke(formatted_prompt).content)