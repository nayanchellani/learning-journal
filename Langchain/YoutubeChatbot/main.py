from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import ChatGoogleGenerativeAI , GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from dotenv import load_dotenv
load_dotenv()
video_id = "maYMSSdb5Ug" 
ytt_api = YouTubeTranscriptApi()

try:
    
    transcript_list = ytt_api.fetch(video_id=video_id, languages=["en"])
    transcript = " ".join(chunk.text for chunk in transcript_list)
    print(transcript)

except TranscriptsDisabled:
    print("No captions available for this video.")
    
docs= [Document(
    page_content=transcript,
    metadata= {"source":"youtube"}
) ]

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 400,
    chunk_overlap = 50,)
chunks = splitter.split_documents(docs)

embedding_model = HuggingFaceEmbeddings(

    model_name=
    "sentence-transformers/all-MiniLM-L6-v2"
)
vector_store = FAISS.from_documents(
    documents=chunks,
    embedding=embedding_model
    
)
retriever =  vector_store.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 5}
)
prompt = PromptTemplate(
    template= '''You are answering questions about a YouTube video. Use ONLY the provided context. Context: {context} , Question: {question}.If answer isn't in context,
say: "I could not find that in the transcript.''',
    input_variables= ['context','question']
    
)
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser = StrOutputParser()
chain =     ({'context':retriever,'question': RunnablePassthrough()} | prompt | model | parser)
answer = chain.invoke('Summarise the video in 3 lines and tell me the length of the video')
print(answer)