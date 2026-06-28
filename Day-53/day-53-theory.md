# 1. What is Stemming? 
**Stemming** is a text preprocessing technique in Natural Language Processing (NLP) that reduces a word to its **base or stem form** by removing prefixes or suffixes. The resulting stem may not be a valid dictionary word. The Purpose is to group similar words together and reduce the number of unique words in a dataset.

### Example:
- Playing → Play
- Played → Play
- Studies → Studi (not a valid English word)

# 2. What is Lemmatization? 
Lemmatization is an NLP technique that converts a word to its dictionary base form (lemma) by considering the word's meaning and grammatical context (such as part of speech).

The output is always a valid dictionary word.

### Example:
- Running → Run
- Better → Good

# 3. Difference between Stemming and Lemmatization. 
| Stemming | Lemmatization |
|----------|---------------|
| Removes prefixes/suffixes using simple rules. | Uses vocabulary and grammar rules to find the dictionary form. |
| May produce non-dictionary words. | Produces valid dictionary words. |
| Faster and simpler. | Slower but more accurate. |
| Does not consider context or meaning. | Considers context and part of speech. |
| Example: Studies → Studi | Example: Studies → Study |

# 4. Why is Lemmatization more accurate? 
Lemmatization is more accurate because it:
- Considers the meaning of the word.
- Uses grammar (part of speech) to determine the correct root form.
- Produces valid dictionary words instead of incomplete stems.
- Handles irregular word forms correctly.

### Example:
- Better → Good (Lemmatization)
- Better → Better (or an incorrect stem using stemming)
# 5. Give three examples of root word conversion. 
| Original Word | Stemming | Lemmatization |
|---------------|----------|---------------|
| Playing | Play | Play |
| Studies | Studi | Study |
| Mice | Mice | Mouse |