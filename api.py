from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Reward(BaseModel):
    name: str
    value: str
    icon: str
    function: str

@app.post("/add-reward")
def add_reward(reward: Reward):
    with open('rewards.json', 'r') as f:
        rewards = json.load(f)
    rewards.append(reward.dict())
    with open('rewards.json', 'w') as f:
        json.dump(rewards, f)
    return {"status": "success"}

@app.get("/rewards")
def get_rewards():
    with open('rewards.json', 'r') as f:
        return json.load(f)