#Before beginning, make sure the TextBlob library is installed on your system, you can install it using 'pip install textblob'.


# Import the TextBlob library
from textblob import TextBlob

# Function to analyze sentiment
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "Negative"
    else:
        return "Neutral"

# Example input
text = input("Enter a sentence to analyze sentiment: ")

# Get sentiment
result = analyze_sentiment(text)

# Output the result
print(f"The sentiment of the sentence is: {result}")
