import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import joblib


def preprocess_text(text):
    if not isinstance(text, str):
        return ""
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove special chars
    text = text.lower()
    text = text.strip()
    return text


# Load dataset
data = pd.read_csv('data/train.csv', encoding='latin1')
# print(data['text'].head())  # Display first 5 rows
# print(data['text'].dtype)   # Check the data type of the column
# print(data['text'].isnull().sum())  # Count missing values
data['cleaned_text'] = data['text'].apply(preprocess_text)

# Train-test split
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data['cleaned_text'])
y = data['sentiment']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Naive Bayes model
model = MultinomialNB()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("Model Accuracy:", accuracy_score(y_test, y_pred))

# Save model and vectorizer
joblib.dump(model, "models/sentiment_model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")
