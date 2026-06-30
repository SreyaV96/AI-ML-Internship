# 1. What are Pre-trained Word Embeddings? 
Pre-trained Word Embeddings are word vectors that have already been trained on very large text datasets. Instead of training from scratch, we can directly download and use these embeddings in our NLP applications.

### Advantages:
- Saves training time.
- Better accuracy because they are trained on large datasets.
- Captures semantic relationships between words.

### Examples:
- Word2Vec
- GloVe
- FastText
# 2. Explain GloVe. 
GloVe (Global Vectors for Word Representation) is a pre-trained word embedding model that learns word meanings using global word 
co-occurrence statistics. Instead of looking only at nearby words, GloVe learns from how often words appear together across the entire dataset. It is developed by Stanford University. Available in different dimensions such as 50d, 100d, 200d and 300d.

# 3. Explain FastText. 
FastText is a word embedding model developed by Meta (Facebook AI Research). It represents each word using character-level subwords (n-grams) instead of treating the word as a single unit.
#### Advantages
-  Handles rare words effectively.
- Can generate vectors for unseen (OOV) words.
# 4. What is OOV? 
OOV (Out-of-Vocabulary) refers to words that are not present in the vocabulary of a trained model.

# 5. Compare Word2Vec, GloVe, and FastText. 

| Feature | Word2Vec | GloVe | FastText |
|---------|----------|-------|----------|
| Developed by | Google | Stanford | Meta (Facebook) |
| Learning method | Predicts words from context | Uses global word co-occurrence | Uses context and character n-grams |
| Handles OOV words | No | No | Yes |
| Uses subword information | No | No | Yes |
| Suitable for rare words | Limited | Limited | Excellent |
| Training speed | Fast | Moderate | Fast |
| Best use | General NLP tasks | Semantic similarity | Rare words and text classification |