from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'API is running!'

@app.route('/add-reward', methods=['POST', 'OPTIONS'])
def add_reward():
    if request.method == 'OPTIONS':
        return '', 200
        
    reward = request.get_json()
    rewards_file = '/tmp/rewards.json'
    
    # خواندن داده‌های موجود یا ساخت لیست خالی
    if os.path.exists(rewards_file):
        with open(rewards_file, 'r') as f:
            rewards = json.load(f)
    else:
        rewards = []
    
    rewards.append(reward)
    
    # ذخیره در مسیر tmp که مجوز نوشتن دارد
    with open(rewards_file, 'w') as f:
        json.dump(rewards, f)
    
    return jsonify({"status": "success"})

@app.route('/rewards', methods=['GET'])
def get_rewards():
    rewards_file = '/tmp/rewards.json'
    
    if os.path.exists(rewards_file):
        with open(rewards_file, 'r') as f:
            rewards = json.load(f)
    else:
        rewards = []
        
    return jsonify(rewards)