# 1. Define a Vector Database. 
A Vector Database is a specialized database that stores embeddings (vectors) and performs fast similarity searches.

Instead of searching text directly, it searches vectors based on their meaning. 
### Popular vector databases
1. chromaDB
2. FAISS
3. Pinecone
4. Weaviate

# 2. Explain ChromaDB. 
ChromaDB is an open-source vector database built for AI and LLM applications. It stores document embeddings along with metadata and allows semantic search using similarity matching.

### Features
- Open source
- Easy to install and use
- Stores vectors and metadata
- Integrates with LangChain and LlamaIndex
- Ideal for RAG applications and chatbot development

# 3. Explain FAISS. 
FAISS (Facebook AI Similarity Search) is an open-source library developed by Meta for efficient similarity search and clustering of dense vectors.

### Features
- Extremely fast vector search
- Supports millions to billions of vectors
- CPU and GPU support
- Multiple indexing techniques for optimized search

# 4. Differentiate ChromaDB and FAISS. 
## Difference Between ChromaDB and FAISS

| **ChromaDB** | **FAISS** |
|--------------|-----------|
| Stores documents along with metadata. | Stores only vector embeddings for similarity search. |
| Easy to install and use, making it suitable for beginners. | More advanced and requires additional setup. |
| Designed specifically for Retrieval-Augmented Generation (RAG) applications. | Designed for high-speed vector similarity search on large datasets. |
| Includes built-in data storage and persistence. | Does not provide built-in database storage. |
| Works well with LangChain and LlamaIndex. | Commonly integrated into custom AI and machine learning pipelines. |
| Best for chatbots, document search, and AI assistants. | Best for large-scale vector search and recommendation systems. |

# 5. Why are vector databases used in RAG? 
- Retrieves relevant information quickly.
- Improves the accuracy of AI responses.
- Reduces incorrect or hallucinated answers.
- Allows AI models to use updated external knowledge.
