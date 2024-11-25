import joblib
from app.sentiment_analysis import preprocess_text

# Load trained model and vectorizer
model = joblib.load('models/sentiment_model.pkl')
vectorizer = joblib.load('models/vectorizer.pkl')


def analyze_sentiment(user_input):
    processed_input = preprocess_text(user_input)
    input_vector = vectorizer.transform([processed_input])
    sentiment = model.predict(input_vector)[0]
    return sentiment


def chatbot_response(user_input):
    sentiment = analyze_sentiment(user_input)
    if sentiment == "positive":
        return "I'm glad to hear that! 😊"
    elif sentiment == "negative":
        return "I'm sorry to hear that. 😔 How can I help?"
    else:
        return "Thanks for sharing! 😊"
