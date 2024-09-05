import logging
from .tweet import TweetManager
from util.generator import FactGenerator

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TwitterBot:
    def __init__(self):
        self.tweet_manager = TweetManager(logging)
        self.fact_generator = FactGenerator(logging)

    def run(self):
        fact = self.fact_generator.generate_fact()
        logging.info(f"Sending Tweet: {fact}")
        response = self.tweet_manager.post_tweet(f"{fact} #NRL #Automated")
        logging.info(f"Tweet Response: {response}")

if __name__ == "__main__":
    bot = TwitterBot()
    bot.run()
