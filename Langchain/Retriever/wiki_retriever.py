import wikipedia
from langchain_community.retrievers import WikipediaRetriever

wikipedia.set_user_agent("MyApp/1.0")

retriever = WikipediaRetriever(top_k_results=2, lang="en")
query= 'Coding theory'
docs = retriever.invoke(query)
print(docs[0].page_content)