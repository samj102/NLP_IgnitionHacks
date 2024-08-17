#Before beginning, make sure the sumy library is installed on your system, you can install it using 'pip install sumy'.

import nltk
nltk.download('punkt')

# Import necessary modules from sumy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer


# Example text for summarization, feel free to replace it with whatever you want. 
text = """
Natural Language Processing (NLP) is a field of artificial intelligence that gives the machines the ability to read, understand, and derive meaning from human languages. 
It is a field that is developing rapidly, and it has numerous applications in various industries. 
For example, NLP is used in sentiment analysis, which helps companies understand customer feedback by analyzing the emotions expressed in text. 
It is also used in machine translation, where it helps translate text from one language to another with great accuracy. 
Another application is in chatbots, which use NLP to have conversations with users, providing them with answers to their questions.
"""

# Parse the text
parser = PlaintextParser.from_string(text, Tokenizer("english"))

# Summarize the text using LSA (Latent Semantic Analysis)
summarizer = LsaSummarizer()
summary = summarizer(parser.document, 2)  

#Print the Original text
print("Original Text:\n", text)

#Print the summary
print("\nSummary:")
for sentence in summary:
    print(sentence)
