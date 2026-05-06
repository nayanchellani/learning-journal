from langchain_huggingface import ChatHuggingFace , HuggingFacePipeline
from dotenv import load_dotenv
from transformers import pipeline

pipe=pipeline(
    model='TinyLlama/TinyLlama_v1.1',
    task='text-generation',
    max_new_tokens=50
)
llm=HuggingFacePipeline( pipeline=pipe)


model = ChatHuggingFace(
    llm=llm
)
result= model.invoke('What is Embeddings')
print(result.content)