import os
from openai import OpenAI
import json
from .config import GPT_API_KEY
from datetime import datetime

# Get the current date
current_date = datetime.now().strftime("%Y-%m-%d")


client = OpenAI(
    api_key=GPT_API_KEY
)

# File path to store generated facts
FACTS_FILE = "generated_facts.json"

def save_facts_to_file(facts):
    with open(FACTS_FILE, "w") as file:
        json.dump(list(facts), file)

def load_facts_from_file():
    if os.path.exists(FACTS_FILE):
        with open(FACTS_FILE, "r") as file:
            return set(json.load(file))
    else:
        return set()

# Initialize a set to store generated facts
generated_facts = load_facts_from_file()

def generate_fact():
    while True:
        response = client.chat.completions.create(
            model="gpt-4",
            messages = [
                {"role": "system", "content": "You are a funny sports historian with expertise in rugby league, particularly the Brisbane Broncos franchise."},
                {"role": "user", "content": "Provide an intriguing tweet about the history of the Brisbane Broncos that can fit in a tweet. Please no hashtags"}
            ]

        )
        new_fact = response.choices[0].message.content.strip().strip('"')
        
        # Check if the new fact is not a duplicate
        if new_fact not in generated_facts:
            break

    # Add the new fact to the set of generated facts
    generated_facts.add(new_fact)

    # Save the updated set of generated facts to file
    save_facts_to_file(generated_facts)

    return new_fact