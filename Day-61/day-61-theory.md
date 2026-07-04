# 1. Define NLP.

Natural Language Processing (NLP) is a branch of Artificial Intelligence (AI) that enables computers to understand, interpret, analyze, and generate human language (text or speech). It combines linguistics, computer science, and machine learning to help machines communicate naturally with humans.

### Applications
- Chatbots
- Voice Assistants (Siri, Alexa, Google Assistant)
- Machine Translation
- Sentiment Analysis
- Spam Detection


# 2. Explain Intent Recognition. 
Intent Recognition is the process of identifying the purpose or goal behind a user's input. It helps a chatbot understand what the user wants to do.

### Example

User: `Book a flight to Delhi.`
Intent:** `Book a Flight`

# 3. Explain Entity Recognition.
Entity Recognition (Named Entity Recognition - NER)** is the process of identifying important information from a sentence, such as names, places, dates, times, organizations, and numbers.

### Example

Sentence:
```text
Book a flight to Chennai on Friday.
```

Entities:
- Location: Chennai
- Date: Friday

Entity Recognition helps chatbots extract the details needed to complete the user's request.

# 4. Differentiate Stemming and Lemmatization. 

| Stemming                                            | Lemmatization                                   |
| --------------------------------------------------- | ----------------------------------------------- |
| Removes prefixes or suffixes to find the root word. | Converts words to their dictionary (base) form. |
| Faster process.                                     | Slower but more accurate.                       |
| May produce invalid words.                          | Produces meaningful words.                      |
| Does not require a dictionary.                      | Requires a dictionary (lexicon).                |
| Example: studies → studi                            | Example: studies → study                        |


# 5. Explain the NLP workflow in chatbots. 

### 1. User Message

The user enters a message (text or voice) into the chatbot.

Example:
```text
Book a flight to Chennai on Friday.
```

### 2. Text Preprocessing

The chatbot cleans and prepares the text for analysis. This step may include:

- Converting text to lowercase
- Removing punctuation and special characters
- Tokenization (splitting text into words)
- Removing stop words (optional)
- Stemming or Lemmatization (optional)

Example:

Input:
```text
Book a flight to Chennai on Friday.
```

After preprocessing:
```text
['book', 'a', 'flight', 'to', 'chennai', 'on', 'friday']
```

### 3. Intent Recognition

The chatbot identifies the user's goal or purpose by analyzing the message.

Example:

User Message:
```text
Book a flight to Chennai on Friday.
```

Detected Intent:
```text
Book a Flight
```

The chatbot understands that the user wants to book a flight.

### 4. Entity Recognition

The chatbot extracts important information (entities) from the user's message.

Example:

Sentence:
```text
Book a flight to Chennai on Friday.
```

Extracted Entities:

| Entity Type | Value |
|-------------|-------|
| Destination | Chennai |
| Date | Friday |

These entities help the chatbot complete the requested task.


### 5. Response Selection

Based on the detected intent and extracted entities, the chatbot selects the appropriate response or performs the required action.

Example:

Intent:
```text
Book_Flight
```

Entities:
```text
Destination = Chennai
Date = Friday
```

Selected Action:
```text
Search available flights to Chennai on Friday.
```


### 6. Reply to User

Finally, the chatbot generates and sends a response to the user.


### Workflow Diagram

```text
User Message
      │
      ▼
Text Preprocessing
      │
      ▼
Intent Recognition
      │
      ▼
Entity Recognition
      │
      ▼
Response Selection
      │
      ▼
Reply to User
```
