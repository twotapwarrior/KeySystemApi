import key
from flask import Flask, request, jsonify

app = Flask(__name__)
special_key = key.generate_key()

@app.route("/")
def index():
    return "Key System Api"

@app.route("/encrypt", methods=["POST"])
def encrypt():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid or no JSON data provided"}), 400
    
    encrypted_data = key.encrypt(data, special_key)
    return jsonify({"encrypted_data": encrypted_data}), 200

@app.route("/decrypt", methods=["POST"])
def decrypt():
    raw_data = request.data.decode('utf-8')
    decrypted_data = key.decrypt(raw_data, special_key)
    return jsonify(decrypted_data), 200

if __name__ == "__main__":
    app.run(debug=True)