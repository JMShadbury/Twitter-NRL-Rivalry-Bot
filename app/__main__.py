from .tweet import TweetManager
from util.generator import FactGenerator

class TwitterBot:
    def __init__(self):
        self.tweet_manager = TweetManager()
        self.fact_generator = FactGenerator()

    def run(self):
        fact = self.fact_generator.generate_fact()
        print(fact)
        # response = self.tweet_manager.post_tweet(f"{fact} #Automated - 🤖")
        # print("Tweet Response:", response)

if __name__ == "__main__":
    bot = TwitterBot()
    bot.run()
