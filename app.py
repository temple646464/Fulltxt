
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "TXT File Uploader is Running!"

@app.route("/upload", methods=["POST"])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '' or not file.filename.endswith('.txt'):
        return jsonify({"error": "Invalid or missing .txt file"}), 400

    content = file.read().decode('utf-8')
    return jsonify({
        "filename": file.filename,
        "content": content
    })
