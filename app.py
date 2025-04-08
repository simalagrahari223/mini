# importing flask!
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

RASA_URL = "http://localhost:5005/webhooks/rest/webhook"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.json.get("message")
    payload = {
        "sender": "user",
        "message": message
    }
    response = requests.post(RASA_URL, json=payload)
    rasa_response = response.json()

    if rasa_response:
        reply = " ".join([r["text"] for r in rasa_response])
    else:
        reply = "🤖 Sorry, I didn't understand that."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
