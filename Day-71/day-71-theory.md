# 1. Define a PDF Question Answering Chatbot. 

It is an AI application that allows users to ask questions about the content of one or more PDF documents in natural language. Instead of reading the entire document, the chatbot searches the relevant sections and generates accurate answers based on the document.

### Applications 
PDF Question Answering is used in: 
- Company HR Manuals 
- Banking Documents 
- Insurance Policies 
- Medical Guidelines 
- College Brochures 
- Research Papers 
- Government Rules 


# 2. Explain the complete workflow. 
### Step 1: Load the PDF
- Read the PDF using **PyPDFLoader**.
- Extract all text from the document.

### Step 2: Split the Text
- Divide the extracted text into smaller chunks.
- Use **RecursiveCharacterTextSplitter**.

### Step 3: Create Embeddings
- Convert each text chunk into numerical vectors.
- Use embedding models such as **Sentence Transformers**.

### Step 4: Store in ChromaDB
- Save the embeddings in **ChromaDB**, a vector database.
- Enables fast retrieval of similar content.

### Step 5: User Asks a Question
Example:
> **What are the advantages of cloud computing?**

### Step 6: Convert Question into Embedding
- The user's question is converted into a vector using the same embedding model.

### Step 7: Similarity Search
- ChromaDB compares the question vector with stored document vectors.
- Retrieves the most relevant chunks.

### Step 8: Generate Answer
- The retrieved chunks are passed to an LLM.
- The chatbot generates the final answer.

# 3. What is LangChain? 
LangChain is an open-source Python framework for building applications powered by Large Language Models (LLMs).

It provides tools for:
- Loading documents
- Splitting text
- Creating embeddings
- Managing vector databases
- Building Retrieval-Augmented Generation (RAG) applications
- Connecting LLMs with external data

### Advantages
- Easy integration with AI models
- Supports multiple vector databases
- Modular architecture
- Simplifies chatbot development

# 4. Why do we use ChromaDB? 
ChromaDB is an open-source vector database used to store and retrieve text embeddings efficiently.

### Why ChromaDB?
- Stores embedding vectors
- Fast similarity search
- Lightweight
- Easy integration with LangChain
- Supports semantic search

Without ChromaDB, searching large PDF documents would be much slower.

# 5. Explain similarity search.
Similarity search finds document chunks whose meanings are closest to the user's question. Instead of matching exact words, it compares the meaning of the text using vector embeddings. 
