# 1. Define Metadata. 
Metadata is data that provides additional information about a document or text chunk. It helps identify, organize, filter, and retrieve documents efficiently in a RAG system.

#### Example
- Filename
- Page number
- Department
- Author
- Document title

# 2. Explain Metadata Filtering. 
Metadata Filtering is the process of retrieving documents based on specific metadata values instead of searching all documents.

For example, if a user wants information only from the HR department, the retriever searches only documents whose metadata contains `"Department": "HR"`.

**Benefits:**
- Faster retrieval
- More accurate answers
- Reduces irrelevant results
- Improves search efficiency

# 3. Why is Source Citation important? 
Source citation identifies where the retrieved information came from.

### Importance
- Increases trust in AI-generated answers.
- Allows users to verify information.
- Improves transparency.
- Makes debugging easier.
- Essential for enterprise and research applications.

# 4. List five metadata fields. 
1. Filename
2. Page Number
3. Department
4. Author
5. Document Title

# 5. Explain the role of metadata in enterprise RAG systems. 
Metadata helps enterprise RAG systems organize and retrieve documents efficiently.

Its roles include:
- Filtering documents by department or category.
- Improving search accuracy.
- Providing source citations.
- Supporting access control and security.
- Reducing retrieval time and improving scalability.