from flask import Flask, request, jsonify
import os
import json
import re

# Folder creation
app = Flask(__name__)
SAVE_DIR = "saved_games"
os.makedirs(SAVE_DIR, exist_ok=True)

def is_valid_name(name):
    return re.match(r'^[a-zA-Z0-9_-]+$', name) is not None

@app.route('/')
def home():
    return "Save/Load Microservice is running!"

@app.route('/save', methods=['POST']) # Received POST request to /save
def save_game():
    data = request.get_json()

    user_id = data.get('userId')
    slot = data.get('slot')
    progress = data.get('progress')

    # Error checking
    if not user_id or not slot or not progress:
        return jsonify({'error': 'Missing userId, slot, or progress data'}), 400

    if not is_valid_name(user_id) or not is_valid_name(slot):
        return jsonify({'error': 'Invalid characters in userId or slot'}), 400

    # Writes data to JSON file
    filepath = os.path.join(SAVE_DIR, f"{user_id}_{slot}.json")
    with open(filepath, 'w') as f:
        json.dump(progress, f)

    # Builds saved data to slot and returns a response
    return jsonify({'message': f"Progress saved for {user_id} in slot '{slot}'"}), 200

@app.route('/load', methods=['GET'])
def load_game():
    user_id = request.args.get('userId')
    slot = request.args.get('slot')

    # Error checking
    if not user_id or not slot:
        return jsonify({'error': 'Missing userId or slot'}), 400

    if not is_valid_name(user_id) or not is_valid_name(slot):
        return jsonify({'error': 'Invalid characters in userId or slot'}), 400

    filepath = os.path.join(SAVE_DIR, f"{user_id}_{slot}.json")
    if not os.path.exists(filepath):
        return jsonify({'error': 'Save file not found'}), 404

    # Reads data from file
    with open(filepath, 'r') as f:
        progress = json.load(f)

    # JSON response to send load data
    return jsonify({'userId': user_id, 'slot': slot, 'progress': progress}), 200

# Server start
if __name__ == '__main__':
    app.run(port=3000, debug=True)