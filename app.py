from flask import Flask, request, jsonify
from routes.auth import auth_bp
from utils.cors import apply_cors_headers

app = Flask(__name__)
app.register_blueprint(auth_bp, url_prefix="/api/auth")

@app.after_request
def apply_cors(response):
    return apply_cors_headers(response)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Briv AI Backend Running"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)