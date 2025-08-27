from flask import Flask, request, jsonify
import os

app = Flask(__name__)
GCS_MOUNT_PATH = "/mnt/gcs"  # Change this based on your mount path

@app.route("/files", methods=["GET"])
def list_files():
    files = os.listdir(GCS_MOUNT_PATH)
    return jsonify(files)

port = int(os.environ.get("PORT", 9080))

@app.route("/files", methods=["POST"])
def create_file():
    data = request.json
    file_name = data.get("name")
    content = data.get("content", "")

    if not file_name:
        return jsonify({"error": "File name is required"}), 400

    file_path = os.path.join(GCS_MOUNT_PATH, file_name)
    with open(file_path, "w") as f:
        f.write(content)

    return jsonify({"message": f"File '{file_name}' created successfully"}), 201

@app.route("/files/<filename>", methods=["DELETE"])
def delete_file(filename):
    file_path = os.path.join(GCS_MOUNT_PATH, filename)

    if os.path.exists(file_path):
        os.remove(file_path)
        return jsonify({"message": f"File '{filename}' deleted successfully"}), 200
    else:
        return jsonify({"error": "File not found"}), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port, debug=True)

