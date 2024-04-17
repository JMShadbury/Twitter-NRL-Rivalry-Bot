import json
from .config import GPT_API_KEY
from .scraper import WebScraper
from .constants import AccountHandle, Messages, Team, Legend
from openai import OpenAI
from datetime import datetime, timedelta
import pytz



def get_aest_date():
    aest_timezone = pytz.timezone('Australia/Sydney')
    aest_date = datetime.now(aest_timezone).date()
    return aest_date

class FactGenerator:
    def __init__(self):
        self.client = OpenAI(api_key=GPT_API_KEY)
        self.scraper = WebScraper()
        self.team_stats = self.load_team_stats()

    def load_team_stats(self):
        with open('data/team_stats.json', 'r') as file:
            return json.load(file)

    def generate_fact(self):
        favorite_team = Team.FAVORITE_TEAM.value
        team_data = self.scraper.get_team_data()
        opponent = self.scraper.get_opponent(team_data)
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

        # Adding the legend prompt
        legend_prompt = Legend.STATS_LEGEND.value

        team_stats_prompt = json.dumps(self.team_stats)
        date_info = "Todays date is " + str(get_aest_date()) + " game date is " + opponent['date'] if opponent else "No game today"
        tweet_reminder = "Remember to use handles for both teams and avoid using hashtags. Keep it under 271 characters. Dont talk about stats like kicks"
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": Messages.SYSTEM_PROMPT.value},
                {"role": "user", "content": team_stats_prompt},  
                {"role": "user", "content": legend_prompt},
                {"role": "user", "content": date_info},
                {"role": "user", "content": prompt},
                {"role": "user", "content": tweet_reminder}
            ]
        )
        new_fact = response.choices[0].message.content.strip().strip('"')

        return new_fact
