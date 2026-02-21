from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Assistant Backend Running!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message")

    # Temporary AI response
    response = f"You said: {user_message}"

    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run()