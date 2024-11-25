from flask import Flask, render_template, request, jsonify
from app.chatbot import chatbot_response
app = Flask(__name__, template_folder='../templates')


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form["message"]
    response = chatbot_response(user_input)
    return jsonify({"response": response})
