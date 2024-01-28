from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from tasks import send_email

main = Blueprint('main', __name__)

@main.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    filename = secure_filename(file.filename)

    send_email.delay("teset@gmail.com", "teste", filename)

    return jsonify({"message": "File received"}), 200
