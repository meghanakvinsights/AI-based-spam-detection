import pandas as pd
import pickle
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC

# Simple text cleaning
def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text

print("Spam Detection App")

# Example messages
messages = [
    "Congratulations! You won a free ticket!",
    "Hey, are we meeting today?"
]

# Load dataset
df = pd.read_csv("data/spam.csv")

df['message'] = df['message'].apply(clean_text)

# Convert labels
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# Vectorization
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['message'])

y = df['label']

# Train model
model = SVC(probability=True)
model.fit(X, y)

# Test prediction
for msg in messages:

    msg_clean = clean_text(msg)

    msg_vector = vectorizer.transform([msg_clean])

    prediction = model.predict(msg_vector)

    if prediction[0] == 1:
        print(f"'{msg}' → SPAM")
    else:
        print(f"'{msg}' → HAM")
