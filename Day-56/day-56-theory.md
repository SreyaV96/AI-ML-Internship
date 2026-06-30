# 1. Define Word Embedding. 
Word Embedding is a technique that converts words into numerical vectors while preserving their meaning and relationships. Words with similar meanings are placed close to each other in this space.

#### Example:

King → [0.25, -0.18, 0.67, ...]
Queen → [0.27, -0.16, 0.65, ...]

# 2. What is Word2Vec? 
- Word2Vec is a popular word embedding algorithm developed by Google. It learns word meanings by analyzing surrounding words.
- Basic idea : Words appearing in similar contexts usually have similar meanings.
- There are two architectures:
    - CBOW (Continuous Bag of Words)
    - Skip-Gram

### Advantages:
- Captures semantic relationships between words.
- Produces dense vector representations.
- Faster than many traditional embedding methods.
# 3. Explain CBOW.
Continous bag of words (CBOW) predicts target Word from surrounding context words. 
### Example: 
I ___ AI 

Predict: love  

### Advantages:
- Faster to train.
- Works well with frequent words.
# 4. Explain Skip-Gram. 
Skip-Gram predicts the surrounding context words from a given target word.
### Example: 
Target: love 

Predict: I , AI 

### Advantages:
- Performs well for rare words.
- Produces better-quality embeddings on small datasets.

# 5. Why is Word2Vec better than TF-IDF? 

| **TF-IDF**                             | **Word2Vec (Word Embedding)**                 |
| -------------------------------------- | --------------------------------------------- |
| Counts word importance using frequency | Understands word meaning using context        |
| No semantic relationship between words | Captures semantic relationships between words |
| Produces sparse vectors                | Produces dense vectors                        |
| Traditional NLP technique              | Modern NLP technique                          |

### Example

Sentence 1: "I drive a car."

Sentence 2: "I drive an automobile."

- TF-IDF: Treats car and automobile as different, unrelated words.
- Word2Vec: Learns that car and automobile have similar meanings, so their vectors are close together.