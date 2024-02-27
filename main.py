import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Sample text
text = "Natural language processing (NLP) is a subfield of artificial intelligence (AI) that focuses on enabling computers to understand, interpret, and generate human language."

# Tokenize the text into words
tokens = word_tokenize(text)

# Perform part-of-speech tagging
tagged_tokens = pos_tag(tokens)

# Display the tagged tokens with full POS tags
print("Token\t\tPOS Tag")
print("-----------------------")
for token, pos_tag in tagged_tokens:
    # Translate abbreviated POS tags to full form, No switch statement in py life :/
    if pos_tag == 'JJ':
        pos_tag = 'Adjective'
    elif pos_tag == 'NN':
        pos_tag = 'Noun'
    elif pos_tag == 'NNP':
        pos_tag = 'Proper Noun, Singular'
    elif pos_tag == 'VBZ':
        pos_tag = 'Verb, Third Person Singular Present'
    elif pos_tag == 'DT':
        pos_tag = 'Determiner'
    elif pos_tag == 'IN':
        pos_tag = 'Preposition or Subordinating Conjunction'
    elif pos_tag == 'WDT':
        pos_tag = 'Wh-Determiner'
    elif pos_tag == 'VBG':
        pos_tag = 'Verb, Gerund or Present Participle'
    elif pos_tag == 'NNS':
        pos_tag = 'Noun, Plural'
    elif pos_tag == 'TO':
        pos_tag = '"to" (Part of Infinitive Verb Form)'
    elif pos_tag == 'VB':
        pos_tag = 'Verb, Base Form'
    elif pos_tag == 'CC':
        pos_tag = 'Coordinating Conjunction'
    elif pos_tag == ',':
        pos_tag = 'Comma'
    elif pos_tag == '.':
        pos_tag = 'Period'

    print(f"{token}\t|\t{pos_tag}")
