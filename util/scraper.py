from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .constants import URL, Team

class WebScraper:
    def __init__(self, logging):
        self.logging = logging
        options = Options()
        options.add_argument("-headless")
        self.driver = webdriver.Firefox(options=options)
        
        self.logging.info("Starting Browser")

    def get_team_data(self):
        self.logging.info("Getting team data")
        
        self.logging.info(f"Wait for page to load: {URL.NRL_DRAW.value}")
        self.driver.get(URL.NRL_DRAW.value)
        try:
            WebDriverWait(self.driver, 1).until(EC.presence_of_element_located((By.CLASS_NAME, "match-header")))
            html = self.driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            self.logging.info("Page loaded successfully")
            return self.extract_data(soup)
        finally:
            self.logging.info("Quitting Browser")
            self.driver.quit()

    def extract_data(self, soup):
        self.logging.info("Extracting data")
        matches = soup.find_all("div", class_="match-header")
        match_info = []
        for match in matches:
            date = match.find("p", class_="match-header__title").get_text(strip=True)
            home_team_info = match.find("div", class_="match-team--home")
            away_team_info = match.find("div", class_="match-team--away")
            score_home = None
            score_away = None
            winning_attribute = "match-team__score match-team__score--home"
            losing_attribute = "match-team__score match-team__score--away u-font-weight-300"
            
            try:
                score_home = home_team_info.find("div", class_=winning_attribute).get_text(strip=True).strip("Scored").strip("points")
            except AttributeError:
                self.logging.debug("Score not found, check losing attribute.")
                try:
                    score_home = home_team_info.find("div", class_=losing_attribute).get_text(strip=True).strip("Scored").strip("points")
                except AttributeError:
                    self.logging.debug("No score for game.")
            try:
                score_away = away_team_info.find("div", class_=winning_attribute).get_text(strip=True).strip("Scored").strip("points")
            except AttributeError:
                self.logging.debug("Score not found, check losing attribute.")
                try:
                    score_away = away_team_info.find("div", class_=losing_attribute).get_text(strip=True).strip("Scored").strip("points")
                except AttributeError:
                    self.logging.debug("No score for game.")

            if score_home and score_away:
                game_details = {
                    "date": date,
                    "home_team": home_team_info.find("p", class_="match-team__name").get_text(strip=True),
                    "away_team": away_team_info.find("p", class_="match-team__name").get_text(strip=True),
                    "home_score": score_home,
                    "away_score": score_away
                }
            else:
                game_details = {
                    "date": date,
                    "home_team": home_team_info.find("p", class_="match-team__name").get_text(strip=True),
                    "away_team": away_team_info.find("p", class_="match-team__name").get_text(strip=True),
                    "home_score": "N/A",
                    "away_score": "N/A"
                }
            self.logging.debug(f"Game Details: {game_details}")
            match_info.append(game_details)
            self.logging.debug(f"Match Info: {match_info}")
            
        self.logging.info("Data extracted successfully")
        return match_info

    def get_opponent(self, team_data):
        favorite_team = Team.FAVORITE_TEAM.value.lower()
        for match in team_data:
            if favorite_team in match['home_team'].lower() or favorite_team in match['away_team'].lower():
                opponent = match['away_team'] if favorite_team in match['home_team'].lower() else match['home_team']
                opponent_score = match['away_score'] if favorite_team in match['home_team'].lower() else match['home_score']
                favorite_score = match['home_score'] if favorite_team in match['home_team'].lower() else match['away_score']
                return {'opponent_team': opponent, 'date': match['date'], 'opponent_score': opponent_score, 'favorite_score': favorite_score}
        return None
