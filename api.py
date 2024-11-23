from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

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
