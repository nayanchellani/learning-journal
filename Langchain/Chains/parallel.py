from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt1 = PromptTemplate(
    template='Generate short and simple notes on  {text}',
    input_variables=['text'],
    
)
prompt2 = PromptTemplate(
    template='Generate 5 short MCQ type questions based on the following text {text}',
    input_variables=['text'],
    
)
prompt3 = PromptTemplate(
    template='Merge the provided notes and MCQ sheet in a single document and format it perfectly : /n notes: {notes} , mcq: {mcq}',
    input_variables=['notes','quiz'],
    
)
parser = StrOutputParser()

parallel_chain= RunnableParallel( {
    'notes': prompt1 | model | parser ,
    'mcq': prompt2 | model | parser
}   
)
merge_chain = prompt3 | model | parser
chain = parallel_chain | merge_chain
text ="""LangChain is an open-source framework that simplifies building applications using large language models. It helps developers connect LLMs with external data, tools and workflows and is available in both Python and JavaScript.
Simplifies chaining LLMs together for reusable and efficient workflows.
Offers tools for effective prompt engineering and memory handling.
Streamlines the process of building LLM-powered applications.Chains: Define a sequence of steps where each step can use an LLM, process data or call tools. Simple chains use one step, while multi step chains combine multiple actions.
Prompt Management: Helps design and manage prompts using templates, making it easier to control input, output format and model behavior.
Agents: Agents are LLM driven components that decide which actions to take, such as calling tools or APIs, based on input and predefined capabilities.
Vector Database: Stores data as vectors to enable similarity search, helping retrieve relevant information for tasks like document search and RAG.
Models: Supports multiple LLMs like OpenAI, Hugging Face and others, allowing flexibility in choosing the best model.
Memory Management: Maintains context from past interactions, enabling better responses in conversations and multi step tasks.How LangChain Works?
LangChain enables Retrieval-Augmented Generation (RAG) by combining document processing, vector storage and LLMs to generate accurate, context aware responses. It connects embeddings, vector databases and models into a smooth workflow.An LLM (Large Language Model) is the foundational intelligence—such as GPT-4 or Llama 3—that generates text, while LangChain is an open-source framework designed to build applications around that model by connecting it to external data, APIs, and complex workflows. LLMs provide the raw reasoning power, whereas LangChain provides the scaffolding for building functional, agentic tools """
print(chain.invoke({'text': text}))