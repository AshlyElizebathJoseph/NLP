!pip install nltk

import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
# Download the 'punkt_tab' data for sentence tokenization
nltk.download('punkt_tab')
# Download the specific resource for English
nltk.download('averaged_perceptron_tagger_eng') # This line downloads the necessary language-specific data

text = "The quick brown fox jumps over the lazy dog."

# Tokenize the text
tokens = nltk.word_tokenize(text)

# Perform POS tagging
tagged_tokens = nltk.pos_tag(tokens)

# Print the tagged tokens
tagged_tokens
