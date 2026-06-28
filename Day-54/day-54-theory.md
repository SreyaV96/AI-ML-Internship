# 1. What is Bag of Words? 
Bag of Words (BoW) is a text representation technique used in Natural Language Processing (NLP). It converts text into numerical vectors based on the frequency of words, ignoring grammar and word order.

### Example:
Sentence:
```
AI is powerful
```

BoW Representation:
```
AI: 1
is: 1
powerful: 1
```
# 2. Why do we need BoW? 
BoW is used because machine learning algorithms cannot understand text directly. It converts text into numerical data that can be used for tasks such as:

- Text classification
- Sentiment analysis
- Spam detection
- Document classification

# 3. What is a vocabulary? 
Collection of unique words in a dataset. 
# 4. Explain CountVectorizer. 
CountVectorizer is a Scikit-Learn tool that automatically converts text into Bag of Words vectors.

It:
- Creates the vocabulary.
- Counts the frequency of each word.
- Converts text into numerical vectors.

# 5. List BoW limitations. 
## 1. Ignores Word Order

BoW only counts the occurrence of words and ignores their order in a sentence.

### Example:

Sentence 1:
```
I love AI
```

Sentence 2:
```
AI love I
```

Both sentences produce the same BoW representation, even though their word order is different.


## 2. Ignores Meaning

BoW treats every word as a separate feature and does not understand the meaning of words.

### Example:

```
Good
```

and

```
Excellent
```

Both words have similar meanings, but BoW treats them as completely different words.


## 3. Large Vocabulary Problem

For large text datasets, the number of unique words (vocabulary) becomes very large.

As a result:
- The feature vectors become very large.
- More memory is required.
- Processing becomes slower.