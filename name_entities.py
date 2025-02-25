!pip install svgling
import nltk

# Download the 'maxent_ne_chunker' resource
nltk.download('maxent_ne_chunker')
# Download the 'words' resource (if needed)
nltk.download('words')
# Download the missing 'maxent_ne_chunker_tab' resource
nltk.download('maxent_ne_chunker_tab')

# Example text
text = "Barack Obama was born in Honolulu, Hawaii."

# Tokenize the text
tokens = nltk.word_tokenize(text)

# Perform Part-of-Speech (POS) tagging
tagged_tokens = nltk.pos_tag(tokens)

# Perform Named Entity Recognition (NER) using chunk.ne_chunk()
named_entities = nltk.ne_chunk(tagged_tokens)

# Print the named entities
named_entities
