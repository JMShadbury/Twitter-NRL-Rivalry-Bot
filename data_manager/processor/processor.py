import re
import json
import os
from ..constants import DATA_DIRECTORY, DATA_FILENAME

class DataProcessor:
    def __init__(self, directory=DATA_DIRECTORY):
        self.directory = directory
        os.makedirs(self.directory, exist_ok=True)

    def clean_team_name(self, name):
        original_name = name 
        cleaned_name = re.sub(r'^\d+(?=\D)', '', name)
        return cleaned_name

    def process_data(self, raw_data):
        for item in raw_data:
            item['Name'] = self.clean_team_name(item['Name'])
        return raw_data

    def save_data(self, data, filename=DATA_FILENAME):
        filepath = os.path.join(self.directory, filename)
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=4)