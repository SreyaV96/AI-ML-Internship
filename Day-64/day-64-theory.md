# 1. Define API.
API (Application Programming Interface) is a set of rules and protocols that allows different software applications to communicate with each other. It enables one application to request data or services from another application without needing to know its internal implementation.


# 2. Explain the OpenAI API.
The OpenAI API allows developers to integrate AI models into their own applications. 
Using the API, developers can build: 
- AI Chatbots 
- Virtual Assistants 
- AI Tutors 
- Content Generators 
- Code Assistants 
- Customer Support Systems 


## 3. What is an API Key?
An API key is a unique secret code issued by an API provider that identifies and authenticates a user or application when accessing the API. It helps control access, track usage, and protect the service from unauthorized use.
**Note:** Keep real API keys private and never share them publicly.


## 4. Explain the Workflow of an AI Chatbot Using an API

### Steps
1. The user enters a message.
2. The chatbot application receives the message.
3. The application sends the message and API key to the AI API.
4. The AI model processes the request.
5. The API returns the generated response.
6. The chatbot displays the response to the user.

### Workflow Diagram
```text
+------------------+
|       User       |
+------------------+
          |
          v
+------------------+
|  Python Program  |
+------------------+
          |
          v
+------------------+
|    OpenAI API    |
+------------------+
          |
          v
+------------------+
|  ChatGPT Model   |
+------------------+
          |
          v
+----------------------+
| Generated Response   |
+----------------------+
          |
          v
+------------------+
| Display to User  |
+------------------+
```

## 5. Compare Rule-Based and LLM-Based Chatbots

| Rule-Based Chatbot | LLM-Based Chatbot |
|--------------------|-------------------|
| Uses predefined rules and decision trees. | Uses Large Language Models (LLMs). |
| Responds only to predefined commands or patterns. | Understands natural language and context. |
| Limited flexibility. | Highly flexible and conversational. |
| Easy to build and maintain. | Requires AI models and API integration. |
| Suitable for FAQs and fixed workflows. | Suitable for virtual assistants and advanced customer support. |
| Low computational cost. | Higher computational cost but greater capability. |