import os
from openai import OpenAI
import json
from .config import GPT_API_KEY

client = OpenAI(
    api_key=GPT_API_KEY
)


def generate_fact():
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You are a bot that likes the Brisbane Broncs and are designed to make fun of a team provided in the user context. You should use embarrasing facts about the other team for your jokes and should use any fact before 2017 or after 2019"
            },
            {
                "role": "user",
                "content": "Can you come up with a funny historical fact about the @brisbanebroncos for a tweet. Lets make fun of an embarrasing fact about the @RaidersCanberra as they play them this weekend, staying under 265 characters? and no hashtags please"
            }
        ]

    )
    new_fact = response.choices[0].message.content.strip().strip('"')

    return new_fact
