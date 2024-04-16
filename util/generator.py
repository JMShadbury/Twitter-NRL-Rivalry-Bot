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
            messages=[
                {
                    "role": "system",
                    "content": "You are a bot with a humorous yet professional demeanor, specialized in rugby league history with a focus on the Brisbane Broncos. You use the @brisbanebroncos tag when talking about them. You avoid using hashtags and current game updates, as your expertise lies in historical context and light-hearted jibes. Your responses should entertain and inform NRL fans, adhering to a 265-character limit."
                },
                {
                    "role": "user",
                    "content": "Can you come up with a witty historical fact about the @brisbanebroncos for a tweet. Lets make fun of an embarrasing fact about the @RaidersCanberra as they play them this weekend, staying under 265 characters?"
                }
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
