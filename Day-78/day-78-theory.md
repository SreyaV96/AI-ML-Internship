# 1. Define Conversation Memory. 
Conversation Memory is the ability of an AI chatbot to remember previous messages in a conversation and use them to answer future questions correctly. 

# 2. Explain Buffer Memory and Window Memory. 
### Buffer Memory
- Buffer Memory stores the entire conversation history.
- The model can access all previous interactions.
- Suitable for short or medium-length conversations.
- Increases token usage and computational cost.

### Window Memory
- Window Memory stores only the most recent N interactions.Older messages are automatically discarded.
- The window size is configurable (e.g., last 3 or last 5 exchanges).
- Faster and more efficient for long conversations.

# 3. Differentiate Memory and Retrieval. 

## 3. Differentiate Memory and Retrieval

| Memory | Retrieval |
|---------|-----------|
| Memory stores information from the current or previous conversation. | Retrieval fetches information from external sources such as PDFs, databases, or vector databases. |
| It maintains conversation context. | It finds relevant documents or knowledge for answering queries. |
| Data comes from chat history. | Data comes from external knowledge bases. |
| Used to remember user details, preferences, and previous messages. | Used to retrieve factual information that is not part of the conversation. |
| Example: Remembering the user's name during a chat. | Example: Searching an HR policy stored in ChromaDB. |

# 4. Why is Chat History important? 

- Maintains the context of the conversation.
- Avoids asking the same questions repeatedly.
- Produces more natural and human-like interactions.
- Personalizes responses based on previous messages.
- Improves the accuracy and consistency of answers.
- Enhances the overall user experience.

# 5. List four real-world applications of Conversation Memory. 

1. **Customer Support Chatbots**
   - Remember previous customer interactions, complaints, and order details to provide faster and more personalized support.

2. **Virtual Personal Assistants**
   - Remember user preferences, reminders, schedules, and frequently used commands to offer personalized assistance.

3. **Healthcare Chatbots**
   - Remember patient symptoms, medical history, and previous conversations to provide consistent healthcare guidance.

4. **Educational Tutoring Systems**
   - Remember a student's learning progress, completed lessons, strengths, and weak areas to deliver personalized learning experiences.