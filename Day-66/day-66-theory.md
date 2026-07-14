# 1. Define RAG
Retrieval-Augmented Generation (RAG) is an AI technique that combines information 
retrieval with a Large Language Model (LLM) to generate accurate and context-aware 
answers. 
Instead of answering only from its pre-trained knowledge, the AI first retrieves relevant 
information from external sources and then generates a response. 
# 2. Explain the RAG Workflow
The RAG workflow consists of the following steps:

1. User Query
   - The user asks a question.

2. Convert Query into Embedding
   - The query is converted into a numerical vector (embedding).

3. Search Vector Database
   - The embedding is compared with stored document embeddings in a vector database.

4. Retrieve Relevant Documents
   - The most relevant document chunks are retrieved.

5. Provide Context to LLM
   - The retrieved documents are sent to the language model along with the user's question.

6. Generate Answer
   - The LLM produces an answer based on the retrieved information.
# 3. Differentiate ChatGPT and RAG

| ChatGPT | RAG |
|----------|-----|
| Uses only its trained knowledge. | Uses external knowledge sources during answering. |
| Knowledge may become outdated. | Can provide up-to-date information. |
| May hallucinate facts. | Reduces hallucinations by using retrieved documents. |
| Does not automatically access private documents. | Can answer questions from private documents like PDFs and databases. |
| Best for general conversations. | Best for document-based question answering and enterprise applications. |


# 4. What is an Embedding?

An embedding is a numerical representation (vector) of text, images, or other data. It captures the meaning of the content so that similar pieces of information have similar vector representations. Embeddings are used to compare the similarity between queries and stored documents.

# 5. What is a Vector Database?

A vector database is a specialized database that stores embeddings (vectors) and performs fast similarity searches. It retrieves the most relevant information based on vector similarity instead of exact keyword matching.

### Examples
- FAISS
- ChromaDB
- Pinecone
- Weaviate