from .config import GPT_API_KEY
from .scraper import WebScraper  
from .constants import AccountHandle, Messages, Team
from openai import OpenAI

client = OpenAI(api_key=GPT_API_KEY)

def generate_fact():
    favorite_team = Team.FAVORITE_TEAM.value
    scraper = WebScraper()
    team_data = scraper.get_team_data()
    opponent = scraper.get_opponent(team_data)

    favorite_team_handle = getattr(AccountHandle, favorite_team.replace(" ", "_").upper(), None)
    if not favorite_team_handle:
        return "Favorite team handle not found in ENUM."

    if opponent:
        opponent_team = opponent['opponent_team'].replace(" ", "_").upper()
        opponent_handle = getattr(AccountHandle, opponent_team, None)
        if opponent_handle:
            prompt = Messages.OPPONENT_FOUND.value.format(favorite_team_handle=favorite_team_handle.value, opponent_handle=opponent_handle.value)
        else:
            prompt = Messages.OPPONENT_HANDLE_NOT_FOUND.value
    else:
        prompt = Messages.NO_OPPONENT_FOUND.value.format(favorite_team_handle=favorite_team_handle.value)

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": Messages.SYSTEM_PROMPT.value
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    new_fact = response.choices[0].message.content.strip().strip('"')
    return new_fact