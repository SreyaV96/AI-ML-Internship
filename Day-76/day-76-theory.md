# 1. Define Multi-PDF RAG

Multi-PDF RAG is an AI system that retrieves relevant information from **multiple PDF documents** and uses a Large Language Model (LLM) to generate accurate answers based on the retrieved content.

Instead of relying only on the LLM's internal knowledge, the system searches through several PDFs, finds the most relevant text chunks, and provides context to the model before generating a response.

### Advantages
- Supports multiple documents
- Provides source-based answers
- Reduces hallucinations
- Useful for research, education, legal, and business documents

# Explain the workflow of a Multi-PDF RAG system.

#### Multi-PDF RAG Workflow

```text
          Multiple PDFs
      (PDF1, PDF2, PDF3...)
               │
               ▼
       Document Loaders
               │
               ▼
        Text Extraction
               │
               ▼
         Text Splitting
               │
               ▼
      Generate Embeddings
               │
               ▼
   Store in Vector Database
      (ChromaDB / FAISS)
               │
               ▼
         User Question
               │
               ▼
           Retriever
               │
               ▼
     Retrieve Relevant Chunks
               │
               ▼
        Prompt Template
               │
               ▼
              LLM
               │
               ▼
         Final AI Response
```

### Workflow Explanation

1. **Multiple PDFs**
   - The system accepts multiple PDF documents as the knowledge source.

2. **Document Loaders**
   - PDF loaders (e.g., `PyPDFLoader`) read the PDF files and extract their contents.

3. **Text Extraction**
   - Text is extracted from each page of every PDF.

4. **Text Splitting**
   - Large documents are divided into smaller overlapping chunks for efficient retrieval.

5. **Generate Embeddings**
   - Each text chunk is converted into a numerical vector (embedding) using an embedding model.

6. **Store in Vector Database**
   - The embeddings and their metadata are stored in a vector database such as **ChromaDB** or **FAISS**.

7. **User Question**
   - The user asks a question related to the PDF documents.

8. **Retriever**
   - The user's question is converted into an embedding, and the retriever searches the vector database for similar chunks.

9. **Retrieve Relevant Chunks**
   - The most relevant text chunks from one or more PDFs are retrieved.

10. **Prompt Template**
    - The retrieved chunks and the user's question are combined into a prompt for the language model.

11. **LLM**
    - The Large Language Model (LLM) analyzes the provided context and generates an accurate response.

12. **Final AI Response**
    - The system returns the final answer, often including references to the source PDFs or page numbers.

# 3. Why is metadata important?

Metadata is additional information stored with each text chunk.

Examples:  PDF filename- Page number, Author, Document title, Chunk ID

Metadata identifies the source document and page number, making responses more trustworthy and easier to verify.

# 4. What are the challenges of Multi-PDF RAG? 

- Duplicate information across multiple PDFs
- Large storage requirements for embeddings
- Slower retrieval with many documents
- Poor chunking may lose context
- Inconsistent document formatting
- OCR errors in scanned PDFs
- Conflicting information between documents

# 5. Explain how duplicate information is handled. 
By removing duplicate chunks during preprocessing or combining similar retrieved chunks before generating the response. 



