from flask import Flask, request, jsonify, render_template
from chatbot_logic import get_chat_response
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_input = request.json.get('message')
        bot_reply = get_chat_response(user_input)
        return jsonify({'response': bot_reply})
    except Exception as e:
        return jsonify({'response': f"An error occurred: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)
