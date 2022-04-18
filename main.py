from textblob import TextBlob
import nltk
nltk.download('punkt')

with open('reviews.txt', 'r') as f:
    text = f.read()

blob = TextBlob(text)
sentiment = blob.sentiment.polarity # -1 to 1
print(sentiment)