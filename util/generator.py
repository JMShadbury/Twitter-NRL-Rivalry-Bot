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
        
        self.logging.debug(f"Favorite Team: {favorite_team}")
        self.logging.debug(f"Team Data: {team_data}")
        self.logging.debug(f"Opponent: {opponent}")
        self.logging.debug(f"Favorite Team Handle: {favorite_team_handle}")

        if not favorite_team_handle:
            self.logging.error("Favorite team handle not found in ENUM.")
            return "Favorite team handle not found in ENUM."

        if opponent:
            opponent_team = opponent['opponent_team'].replace(" ", "_").upper()
            opponent_handle = getattr(AccountHandle, opponent_team, None)
            
            self.logging.debug(f"Opponent Team: {opponent_team}")
            self.logging.debug(f"Opponent Handle: {opponent_handle}")
            
            self.logging.info(f"Opponent found: {opponent['opponent_team']}")
            if opponent_handle:
                prompt = Messages.OPPONENT_FOUND.value.format(favorite_team_handle=favorite_team_handle.value, opponent_handle=opponent_handle.value)
            else:
                prompt = Messages.OPPONENT_HANDLE_NOT_FOUND.value
        else:
            prompt = Messages.NO_OPPONENT_FOUND.value.format(favorite_team_handle=favorite_team_handle.value)

        # Adding the legend prompt
        legend_prompt = Legend.STATS_LEGEND.value

        self.logging.debug(f"Prompt: {prompt}")
        team_stats_prompt = json.dumps(self.team_stats)
        
       # Transform date string
        game_date_str = opponent['date']
        # Removing the day of the week and the 'th' from the date
        game_date_str = ' '.join(game_date_str.split()[1:]).replace('th', '')

        # Parse the date with the year hardcoded as 2024
        game_date = datetime.strptime(f"{game_date_str} 2024", "%d %B %Y").date()

        # Get today's date directly as a date object for comparison
        today_date = get_aest_date()

        # Calculate the difference in days
        delta_days = (game_date - today_date).days
        
        
        if delta_days > 0:
            date_info = f"This game is in {delta_days} days."
        elif delta_days == 0:
            date_info = "This game is today."
        else:
            date_info = "This game is already over."
        
        self.logging.info("Requesting completion from GPT-4")
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": Messages.SYSTEM_PROMPT.value},
                {"role": "user", "content": team_stats_prompt},  
                {"role": "user", "content": legend_prompt},
                {"role": "user", "content": prompt},
                {"role": "user", "content": date_info},
                {"role": "user", "content": "Pay attention to the reminders that are about to come"},
                {"role": "user", "content": Messages.REMINDER.value}
            ]
        )
        
        self.logging.info("Response received")
        new_fact = response.choices[0].message.content.strip().strip('"')
        return new_fact
