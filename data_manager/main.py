# main.py
from scraper.scraper import WebScraper
from processor.processor import DataProcessor

def main():
    scraper = WebScraper()
    processor = DataProcessor()
    data = scraper.scrape()
    processed_data = processor.process_data(data)
    processor.save_data(processed_data)

if __name__ == "__main__":
    main()
