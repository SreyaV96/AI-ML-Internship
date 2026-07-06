# 1. Define NLTK
NLTK (Natural Language Toolkit) is a Python library used for Natural Language Processing (NLP). It provides tools for processing and analyzing human language, including tokenization, stop word removal, stemming, lemmatization, text classification, and parsing.


# 2. Explain Tokenization with an Example
Tokenization is the process of splitting a text into smaller units called tokens. These tokens can be words, sentences, or characters.

### Example:

Input:
```text
Artificial Intelligence is changing the world.
```

Output:
```python
['Artificial', 'Intelligence', 'is', 'changing', 'the', 'world', '.']
```


# 3. Explain Stop Word Removal
Stop Word Removal is the process of removing common words such as is, the, a, an, to, in, of, which usually do not add significant meaning to a sentence. This helps improve the efficiency of NLP models.

### Example:

Input:
```text
I want to book a train ticket to Delhi.
```

Output:
```python
['want', 'book', 'train', 'ticket', 'Delhi']
```



# 4. Differentiate Stemming and Lemmatization

| Stemming | Lemmatization |
|----------|---------------|
| Removes prefixes or suffixes using simple rules. | Converts words to their dictionary (root) form. |
| Faster process. | More accurate but slower. |
| May produce non-dictionary words. | Produces meaningful dictionary words. |
| Example: Playing → play | Example: better → good |


## 5. Compare Rule-Based and NLP-Based Chatbots

| Rule-Based Chatbot | NLP-Based Chatbot |
|--------------------|-------------------|
| Uses predefined rules and keywords. | Uses Natural Language Processing to understand user input. |
| Gives fixed responses. | Provides context-aware responses. |
| Limited flexibility. | Can understand different sentence structures. |
| Easy to develop. | More complex to develop. |
| Suitable for simple tasks. | Suitable for intelligent conversations. |