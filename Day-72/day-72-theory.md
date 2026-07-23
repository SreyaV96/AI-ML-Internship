# 1. Define Similarity Search.
Similarity Search is a technique used to find documents, images, or other data that are semantically similar to a given query instead of matching only exact words. It compares vector embeddings of the query and stored documents to retrieve the most relevant results. 

# 2. Differentiate Keyword Search and Similarity Search. 

| **Keyword Search** | **Similarity Search** |
|--------------------|-----------------------|
| Matches exact words | Matches meaning (semantic search) |
| Misses synonyms | Understands synonyms and similar sentences |
| Uses exact text matching | Uses vector embeddings |
| Traditional search engines | Modern AI applications |
| Less accurate | More accurate  |

# 3. Explain Cosine Similarity.
Cosine Similarity is a metric used to measure how similar two vectors are by calculating the angle between them. It compares the direction of the vectors rather than their magnitude, making it ideal for text embeddings and semantic search.

### Formula

```text
                      A · B
Cosine Similarity = -------------
                   ||A|| × ||B||
```

Where:
- **A** = Query vector
- **B** = Document vector
- **A · B** = Dot product of vectors A and B
- **||A||** = Magnitude (length) of vector A
- **||B||** = Magnitude (length) of vector B

### Range

- **1** → Vectors are identical (maximum similarity)
- **0** → Vectors are unrelated (no similarity)
- **-1** → Vectors point in opposite directions(Opposite meaning) ,
           (rarely occurs in text embeddings, where scores typically range from 0 to 1)

- Widely used in NLP, RAG, chatbots, and recommendation systems.

# 4. What is Top-K Retrieval? 
Top-K Retrieval returns the K most similar documents to a user query.

### Example

Suppose the user asks:

Query: *"How long is the internship?"*

If K = 3, the retrieved documents might be:

1. The internship duration is 6 weeks.
2. Classes are conducted during weekends.
3. Students receive a certificate after completion.

The LLM combines all relevant chunks to generate a better answer. 

# 5. Why is Similarity Search essential in RAG? 

- Retrieves documents based on meaning rather than exact keywords.
- Provides relevant context to the LLM before generating a response.
- Improves the accuracy and relevance of answers.
- Reduces hallucinations by grounding responses in retrieved information.
- Enables LLMs to answer questions using external or custom knowledge bases.
