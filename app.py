from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os

app = Flask(__name__)
CORS(app)

# Get API key safely
api_key = os.environ.get("OPENAI_API_KEY")

if api_key:
    client = OpenAI(api_key=api_key)
else:
    client = None
    print("WARNING: OPENAI_API_KEY not set!")

# Root route
@app.route("/")
def home():
    return "AI Assistant Backend Running!"

# Chat route
@app.route("/chat", methods=["POST"])
def chat():

    if client is None:
        return jsonify({"reply": "API key not configured properly on server"})

    data = request.json
    user_message = data.get("message")

    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=user_message
        )

        reply = response.output[0].content[0].text

        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run()