import os
from pinecone import Pinecone, ServerlessSpec
from app.services.tools import split_text
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings 
from langchain_core.documents import Document
from uuid import uuid4


PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
pc = Pinecone(api_key=PINECONE_API_KEY)
embedding_model = OpenAIEmbeddings(model="text-embedding-3-large",
        api_key=os.environ.get("OPENAI_API_KEY"),
        dimensions=1024)

def embed_articles(articles, query, index_name="index-example"):
    # convert artciles to chunks
    chunked_articles = split_text(articles)
    documents = [Document(page_content=text) for text in chunked_articles]
    uuids = [str(uuid4()) for _ in range(len(documents))]

    
    
    if index_name not in pc.list_indexes().names():

        pc.create_index(name=index_name,
                        metric = "cosine",
                        dimension=1024,
                        spec=ServerlessSpec(
                        cloud="aws",
                        region="us-east-1"))
    
    index = pc.Index(index_name)
    vector_store = PineconeVectorStore(index=index, embedding=embedding_model)
    vector_store.add_documents(documents=documents, ids=uuids)
    
    retriever = vector_store.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={"k": 20, "score_threshold": 0.5},)
    
    top_content = retriever.invoke(query)
    context= []
    for c in top_content:
        context.append(c.page_content)
        
    return context



        