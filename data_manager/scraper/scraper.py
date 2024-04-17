import requests
from bs4 import BeautifulSoup
from ..constants import BASE_URL, DATA_PATH

class WebScraper:
    def __init__(self, logging):
        self.logging = logging
        self.base_url = BASE_URL
        self.headers = {'User-Agent': 'Mozilla/5.0'}
        self.logging.info("Web Scraper Initialized")

    def fetch_page(self, url_suffix):
        self.logging.info(f"Fetching page: {self.base_url + url_suffix}")
        response = requests.get(self.base_url + url_suffix, headers=self.headers)
        self.logging.debug(f"Response Status Code: {response.status_code}")
        response.raise_for_status()
        self.logging.info("Page fetched successfully")
        return response.text

    def parse_html(self, html):
        self.logging.info("Parsing HTML")
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table', class_='fiso-lab-table')
        self.logging.debug(f"Table: {table}")
        headers = [th.get_text(strip=True) for th in table.find_all('th') if th.get_text(strip=True) != '']
        self.logging.debug(f"Headers: {headers}")
        data = []

        for row in table.find_all('tr')[1:]:
            cols = row.find_all(['th', 'td'])
            team_data = {headers[i]: cols[i].get_text(strip=True) for i in range(len(cols))}
            data.append(team_data)
            
        self.logging.debug(f"Data: {data}")
        self.logging.info("HTML parsed successfully")
        return data

    def scrape(self):
        html_content = self.fetch_page(DATA_PATH)
        return self.parse_html(html_content)
