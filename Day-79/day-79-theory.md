# 1. Define RAG Evaluation. 
RAG Evaluation is the process of measuring how accurately a Retrieval-Augmented Generation (RAG) system retrieves relevant information and generates correct responses. 

It evaluates both the retrieval and generation components using metrics such as context relevance, faithfulness, answer relevance, precision, and recall.

# 2. Differentiate Precision and Recall. 

| Precision                                                 | Recall                                                            |
| --------------------------------------------------------- | ----------------------------------------------------------------- |
| Measures how many retrieved documents are relevant.       | Measures how many relevant documents were successfully retrieved. |
| Formula: Precision = Relevant Retrieved / Total Retrieved | Formula: Recall = Relevant Retrieved / Total Relevant Documents   |
| High precision means fewer irrelevant documents.          | High recall means fewer relevant documents are missed.            |
| Focuses on quality of retrieval.                          | Focuses on completeness of retrieval.                             |


# 3. Explain Hallucination with an example. 
Hallucination occurs when an AI model generates information that is incorrect or unsupported by the retrieved documents.

Example

Question: Who invented Python?

Retrieved Document: Python was created by Guido van Rossum.

Chatbot Answer: Python was invented by James Gosling.

The chatbot answer is a hallucination because it is not supported by the retrieved document.


# 4. What is Faithfulness? 

Faithfulness measures whether the AI's answer is supported by the retrieved context. 

Example 

Retrieved Context: 

Training begins on August 1. 

Answer: 

Training begins on August 1. 

  Faithful Answer 

Answer: 

Training begins on September 1. 

  Not Faithful 


# 5. Why is Context Relevance important? 
Context relevance ensures that the retrieved documents are closely related to the user's query. Relevant context improves answer accuracy, reduces hallucinations, and increases the reliability of a RAG system.
