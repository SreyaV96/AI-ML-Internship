# 1. Define an embedding. 
An embedding is a numerical vector (list of numbers) that represents the meaning of text, images, audio, or other data in a machine-readable format. Similar data have similar embeddings, making it easier for AI models to compare and retrieve information.

# 2. Explain semantic search. 
Semantic search is a search technique that finds information based on the meaning and context of a query instead of exact keyword matching.

# 3. What is a Sentence Transformer? 
A Sentence Transformer is a pre-trained deep learning model that converts sentences, paragraphs, or documents into dense vector embeddings.

These embeddings capture semantic meaning and are useful for comparing text similarity.

### Popular Sentence Transformer Models

- all-MiniLM-L6-v2
- all-mpnet-base-v2
- multi-qa-MiniLM-L6-cos-v1
- paraphrase-MiniLM-L6-v2 

# 4. Differentiate keyword search and semantic search. 
 Keyword Search | Semantic Search |
|---------------|-----------------|
| Searches exact words | Searches based on meaning |
| Does not understand context | Understands context |
| Requires matching keywords | Finds related concepts |
| Lower accuracy | Higher accuracy |
| Simple implementation | Uses embeddings and AI |
| Example: "AI" matches only "AI" | "AI" matches "Artificial Intelligence" |

# 5. Why are embeddings important in RAG? 
Retrieval-Augmented Generation (RAG) combines document retrieval with Large Language Models.

Embeddings convert both user queries and documents into vectors. The system compares these vectors to retrieve the most relevant documents before generating an answer.

