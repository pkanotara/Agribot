import os, json
from agribot.utils.constants import DATABASE

def load_conversations():
    if not os.path.exists(DATABASE):
        open(DATABASE, "w").write("{}")
    with open(DATABASE, "r") as f:
        return json.load(f)

def save_conversations(d):
    with open(DATABASE, "w") as f:
        json.dump(d, f, indent=2)
