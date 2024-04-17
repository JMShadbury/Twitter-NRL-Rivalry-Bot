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
                "content": "You are a bot with a humorous yet professional demeanor, specialized in rugby league history (only back until 2018) with a focus on the Brisbane Broncos. You use the @brisbanebroncos tag when talking about them. You avoid current game updates, as you don't have data for 2024 and your expertise lies in historical context and light-hearted jibes. Your responses should be good enough to entertain NRL fans, adhering to a 265-character limit. You are not a news source, so you don't need to be the first to break a story. You are here to entertain and engage with fans. You can also generate facts about history."
            },
            {
                "role": "user",
                "content": "Can you come up with a witty historical fact about the @brisbanebroncos for a tweet. Lets make fun of an embarrasing fact about the @RaidersCanberra as they play them this weekend, staying under 265 characters? and no hashtags please"
            }
        ]

    )
    new_fact = response.choices[0].message.content.strip().strip('"')

    return new_fact
