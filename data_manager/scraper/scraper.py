import requests
from bs4 import BeautifulSoup
import json
from constants import BASE_URL, DATA_PATH

class WebScraper:
    def __init__(self):
        self.base_url = BASE_URL
        self.headers = {'User-Agent': 'Mozilla/5.0'}

    def fetch_page(self, url_suffix):
        response = requests.get(self.base_url + url_suffix, headers=self.headers)
        response.raise_for_status()
        return response.text

    def parse_html(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table', class_='fiso-lab-table')
        headers = [th.get_text(strip=True) for th in table.find_all('th') if th.get_text(strip=True) != '']
        data = []

        for row in table.find_all('tr')[1:]:
            cols = row.find_all(['th', 'td'])
            team_data = {headers[i]: cols[i].get_text(strip=True) for i in range(len(cols))}
            data.append(team_data)

        return data

    def scrape(self):
        html_content = self.fetch_page(DATA_PATH)
        return self.parse_html(html_content)
