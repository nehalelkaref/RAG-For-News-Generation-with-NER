# RAG based News Generation with NER (Q&A)
🏷️ LanghChain 🏷️ Pinecone 🏷️ OpenAI Models 🏷️ React 🏷️ Flask 🏷️ NewsAPI


A Flask-React JS webapp for News Generation:
 - User asks about world events (_ex: What's new with Donald Trump?_)
 - User's question is passed to an OpenAI's GPT-4 to extract Named Entities
 - Named Entities are used to form a search query that is passed to
    [NewsAPI](https://github.com/mattlisiv/newsapi-python) to retrieve relevant article urls
 - Each fetched article url is scraped and then embedded and stored in Pinecone's VectorStore database
 - The user's original question is passed to Pinecone's VectorStore to retrieve the top 20 relevant data chunks
   to the question
 - The context (_relevant data chunks_) is then taken to OpenAI's GPT-4 together with the uer's original query
 - The LLM is instructed to construct an answer given the question and the context
   
