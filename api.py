from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/add-reward', methods=['POST'])
def add_reward():
    reward = request.json
    with open('rewards.json', 'r') as f:
        rewards = json.load(f)
    rewards.append(reward)
    with open('rewards.json', 'w') as f:
        json.dump(rewards, f)
    return jsonify({"status": "success"})

@app.route('/rewards', methods=['GET'])
def get_rewards():
    with open('rewards.json', 'r') as f:
        return jsonify(json.load(f))