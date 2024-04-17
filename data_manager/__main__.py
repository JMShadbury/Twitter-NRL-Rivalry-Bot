import logging
from .scraper.scraper import WebScraper
from .processor.processor import DataProcessor

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    scraper = WebScraper(logging)
    processor = DataProcessor(logging)
    
    logging.info("Scraping data")
    
    data = scraper.scrape()
    
    logging.debug(f"Scraped Data: {data}")
    
    processed_data = processor.process_data(data)
    processor.save_data(processed_data)
    
    logging.debug(f"Processed Data: {processed_data}")
    logging.info("Data processing complete")

if __name__ == "__main__":
    main()
