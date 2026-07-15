# 1. Explain the complete RAG pipeline. 
```text
Upload PDF
      │
      ▼
Extract Text
      │
      ▼
Split into Chunks
      │
      ▼
Create Embeddings
      │
      ▼
Store in Vector Database
      │
      ▼
User Question
      │
      ▼
Convert Question to Embedding
      │
      ▼
Similarity Search
      │
      ▼
Retrieve Best Chunks
      │
      ▼
LLM Generates Final Answer
```

A RAG pipeline extracts text from documents, splits it into chunks, converts the chunks into embeddings, stores them in a vector database, retrieves relevant chunks based on the user's query, and finally uses an LLM to generate an answer. 


# 2. Define chunking. 
Chunking is the process of dividing a large document into smaller, meaningful sections before generating embeddings.Chunking improves retrieval speed and accuracy. 



# 3. What is similarity search? 
Similarity Search finds the document chunks that are most semantically similar to the user's question. Common similarity measures are Cosine Similarity, Euclidean Distance, Dot Product etc.



# 4. Why are embeddings important? 
Embeddings convert text into numerical vectors that represent semantic meaning, so computers can compare meanings instead of exact words. 



# 5. Explain the role of a vector database. 
A vector database stores embeddings and retrieves the most relevant information using similarity search.

### Responsibilities

- Store embeddings
- Perform similarity search
- Return top-k matching chunks
- Enable efficient retrieval

### Examples

- FAISS
- ChromaDB
- Pinecone
- Weaviate
- Milvus