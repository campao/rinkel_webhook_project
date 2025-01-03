from flask import Flask, request, jsonify
from config import API_KEY
print(f"Using API Key: {API_KEY}")

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print(f"Webhook received: {data}")
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(port=5000)
