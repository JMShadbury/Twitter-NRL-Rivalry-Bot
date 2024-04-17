import re
import json
import os
from ..constants import DATA_DIRECTORY, DATA_FILENAME

class DataProcessor:
    def __init__(self, logging, directory=DATA_DIRECTORY):
        self.logging = logging
        self.directory = directory
        os.makedirs(self.directory, exist_ok=True)
        self.logging.info("Data Processor Initialized")

    def clean_team_name(self, name):
        self.logging.debug(f"Cleaning team name: {name}")
        cleaned_name = re.sub(r'^\d+(?=\D)', '', name)
        self.logging.debug(f"Cleaned team name: {cleaned_name}")
        
        
        return cleaned_name

    def process_data(self, raw_data):
        for item in raw_data:
            item['Name'] = self.clean_team_name(item['Name'])
        return raw_data

    def save_data(self, data, filename=DATA_FILENAME):
        filepath = os.path.join(self.directory, filename)
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=4)