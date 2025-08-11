import os
import uuid
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def find_image(image_id):
    for filename in os.listdir(app.config['UPLOAD_FOLDER']):
        if filename.startswith(image_id):
            return filename
    return None

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image part in the request"}), 400

    file = request.files['image']

    if file.filename == '':
        return jsonify({"error": "No image selected for uploading"}), 400

    if file:
        file_extension = os.path.splitext(file.filename)[1]
        unique_id = str(uuid.uuid4())
        new_filename = unique_id + file_extension

        file.save(os.path.join(app.config['UPLOAD_FOLDER'], new_filename))

        return jsonify({"id": unique_id}), 201

@app.route('/image/<image_id>', methods=['GET'])
def get_image(image_id):
    filename = find_image(image_id)

    if filename:
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    else:
        return jsonify({"error": f"Image with ID {image_id} not found."}), 404

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)
