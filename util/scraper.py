from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .constants import URL, Team

class WebScraper:
    def __init__(self):
        options = Options()
        options.add_argument("-headless")
        self.driver = webdriver.Firefox(options=options)

    def get_team_data(self):
        self.driver.get(URL.NRL_DRAW.value)
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "match-header")))
            html = self.driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            return self.extract_data(soup)
        finally:
            self.driver.quit()

    def extract_data(self, soup):
        matches = soup.find_all("div", class_="match-header")
        match_info = []
        for match in matches:
            date = match.find("p", class_="match-header__title").get_text(strip=True)
            home_team_info = match.find("div", class_="match-team--home")
            away_team_info = match.find("div", class_="match-team--away")

            game_details = {
                "date": date,
                "home_team": home_team_info.find("p", class_="match-team__name").get_text(strip=True),
                "home_position": home_team_info.find("p", class_="match-team__position").get_text(strip=True),
                "away_team": away_team_info.find("p", class_="match-team__name").get_text(strip=True),
                "away_position": away_team_info.find("p", class_="match-team__position").get_text(strip=True)
            }
            match_info.append(game_details)
        print(match_info)
        return match_info

    def get_opponent(self, matches):
        favorite_team = Team.FAVORITE_TEAM.value
        for match in matches:
            if favorite_team in match['home_team']:
                return {
                    "date": match["date"],
                    "opponent_team": match["away_team"],
                    "opponent_position": match["away_position"]
                }
            elif favorite_team in match['away_team']:
                return {
                    "date": match["date"],
                    "opponent_team": match["home_team"],
                    "opponent_position": match["home_position"]
                }
        return None
