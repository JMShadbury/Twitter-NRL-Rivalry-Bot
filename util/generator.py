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
    def __init__(self, logging):
        self.logging = logging
        self.client = OpenAI(api_key=GPT_API_KEY)
        self.scraper = WebScraper(self.logging)
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
            self.logging.error("Favorite team handle not found in ENUM.")
            return "Favorite team handle not found in ENUM."

        opponent_team = opponent['opponent_team'].replace(" ", "_").upper() if opponent else None
        opponent_handle = getattr(AccountHandle, opponent_team, None) if opponent_team else None

        prompt = Messages.NO_OPPONENT_FOUND.value.format(favorite_team_handle=favorite_team_handle.value)
        if opponent:
            if opponent_handle:
                prompt = Messages.OPPONENT_FOUND.value.format(favorite_team_handle=favorite_team_handle.value, opponent_handle=opponent_handle.value)
            else:
                prompt = Messages.OPPONENT_HANDLE_NOT_FOUND.value

        legend_prompt = Legend.STATS_LEGEND.value
        team_stats_prompt = json.dumps(self.team_stats)
        date_info = self.calculate_date_info(opponent)

        response = self.request_fact(Messages.SYSTEM_PROMPT.value, team_stats_prompt, legend_prompt, prompt, date_info)
        new_fact = response.choices[0].message.content.strip().strip('"')

        if len(new_fact) > 265:
            self.logging.warning(f"Generated content too long ({len(new_fact)} characters). Asking to shorten...")
            return self.request_shorten(new_fact)

        return new_fact

    def calculate_date_info(self, opponent):
        game_date_str = opponent['date']
        game_date_str = ' '.join(game_date_str.split()[1:]).replace('th', '')
        game_date = datetime.strptime(f"{game_date_str} 2024", "%d %B %Y").date()
        today_date = get_aest_date()
        delta_days = (game_date - today_date).days
        
        if delta_days > 0:
            return f"This game is in {delta_days} days."
        elif delta_days == 0:
            return "This game is today."
        else:
            return "This game has passed."

    def request_fact(self, system_prompt, team_stats_prompt, legend_prompt, game_prompt, date_info):
        self.logging.info("Requesting completion from GPT-4")
        print(date_info)
        return self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": team_stats_prompt},
                {"role": "user", "content": legend_prompt},
                {"role": "user", "content": game_prompt},
                {"role": "user", "content": Messages.REMINDER.value},
                {"role": "user", "content": date_info}
                
            ]
        )

    def request_shorten(self, fact):
        self.logging.info("Asking GPT-4 to shorten the content")
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "This tweet needs to be less than 265 characters long."},
                {"role": "user", "content": fact}
            ]
        )
        shortened_fact = response.choices[0].message.content.strip().strip('"')
        return shortened_fact

