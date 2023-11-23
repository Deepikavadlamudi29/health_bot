from flask import Flask, render_template, request, jsonify
from chat_bot import chatbot_response

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# API endpoint for handling chatbot requests
@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['user_message']
    # Call your chatbot function to get a response
    bot_response = chatbot_response(user_message)
    return jsonify({'bot_response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
