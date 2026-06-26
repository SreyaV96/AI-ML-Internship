# 1. Define Text Preprocessing. 
Text Preprocessing is the process of cleaning and preparing raw text data before feeding it into an NLP model. It involves removing noise, normalizing text, and converting it into a format that a machine can understand. Steps include lowercasing, removing punctuation, removing stop words, tokenization, and stemming/lemmatization..

# 2. What is Tokenization? 
Tokenization is the process of splitting a sentence or paragraph into smaller units called tokens. Tokens are usually words or sentences. Example: "I love NLP" becomes ["I", "love", "NLP"].
# 3. What are Stop Words? 
Stop words are common words that appear very frequently in a language but carry little or no meaningful information. They are usually removed during preprocessing to reduce noise. 

Example: is, the, a, an, on, in, at, was, were, it, this, that.
# 4. Why remove punctuation? 
Punctuation marks like !, ?, ., , do not add meaning to the text in most NLP tasks. They can confuse the model or cause the same word to be treated as different tokens (e.g., "amazing" vs "amazing!"). Removing them helps clean and standardize the text.
# 5. Why convert text to lowercase? 
Converting text to lowercase ensures consistency by treating words like "AI" and "ai" as the same word, reducing duplicate tokens.