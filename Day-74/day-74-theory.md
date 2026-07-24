# 1 Define LangChain. 
LangChain is an open-source framework for building applications powered by Large Language Models (LLMs). It helps developers connect LLMs with external data sources such as PDFs, databases, APIs, and websites. LangChain simplifies tasks like document loading, text splitting, embedding generation, vector storage, retrieval, and question answering.

**Features:**
- Document loading
- Text splitting
- Embedding generation
- Vector databases
- Retrieval-Augmented Generation (RAG)
- Prompt templates
- Chains and agents

# 2 Explain Document Loaders. 
Document Loaders are components in LangChain used to load data from different sources into `Document` objects.

They support:
- PDF
- DOCX
- TXT
- CSV
- HTML
- Websites
- Databases

Example:

```python
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("sample.pdf")
documents = loader.load()
```
Each page is stored as a `Document` object containing:
- `page_content`
- `metadata`

# 3 Why do we use Text Splitters? 
Large Language Models have context-length limits, so large documents must be divided into smaller chunks before processing.

**Advantages:**
- Fits within the LLM's context window
- Improves retrieval accuracy
- Faster processing
- Preserves context with chunk overlap

Example:

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.split_documents(documents)
```

# 4 What is a Retriever in LangChain? 
A Retriever is a component in a RAG system that searches a knowledge base and retrieves the most relevant documents or text chunks for a user's query. 

The retrieved information is then passed to the Large Language Model (LLM) to generate the final answer.  

# 5 What is a Chain?
A Chain in LangChain connects multiple components into a workflow to accomplish a specific task. It automates the sequence of operations required to process user input and generate a response.

**Example Workflow:**

```text
Question → Retriever → LLM → Answer
```

### Simple Example

```python
from langchain.chains import RetrievalQA

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever
)
```

### The Chain Automatically Performs

- Retrieves the most relevant document chunks using the retriever.
- Prepares the retrieved context for the language model.
- Sends the context and user query to the LLM.
- Generates and returns the final response.