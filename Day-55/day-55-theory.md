# 1. What is TF-IDF? 
TF-IDF is a feature extraction technique that measures how important a word is in a document relative to the entire dataset. It balances word frequency with how unique the word is across documents.
# 2. Define TF. 
Term Frequency (TF) measures how frequently a word appears in a document.
### Formula

\[
TF(t,d)=\frac{\text{Number of times term }t\text{ appears in document }d}{\text{Total number of words in document }d}
\]


Words that appear frequently in a document get a higher TF.

# 3. Define IDF. 
Inverse Document Frequency (IDF)measures how important or rare a word is across all documents.

### Formula
\[
   IDF(t) = \log \frac{\text{Total number of documents}}{\text{Number of documents containing term t}}
   \]


Words appearing in many documents have lower IDF values, while rare words have higher IDF values.
# 4. Why is IDF important? 
IDF is important because it reduces the importance of common words such as is, the, and, etc., which appear in many documents and provide little useful information.

Benefits:

- Reduces the weight of common words.
- Increases the importance of rare and meaningful words.
- Improves document representation.
- Helps machine learning models perform better.
# 5. Compare BoW and TF-IDF. 
## 5. Compare BoW and TF-IDF
## Comparison: Bag of Words (BoW) vs TF-IDF

| **Bag of Words (BoW)** | **TF-IDF** |
|------------------------|------------|
| Counts the frequency of words. | Calculates the importance of words using TF and IDF. |
| Gives equal importance to all words. | Gives higher importance to rare and meaningful words. |
| Common words may dominate the representation. | Common words receive lower weights. |
| Simple and easy to implement. | Smarter and more informative representation. |
| Less accurate for many NLP tasks. | More accurate for text analysis and classification. |
| Beginner-friendly approach. | Widely used in industry and real-world NLP applications. |
| Used for basic text representation. | Used for text classification, search engines, recommendation systems, and information retrieval. |