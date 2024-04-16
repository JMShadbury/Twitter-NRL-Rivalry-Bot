from util.generator import generate_fact
from .tweet import post_tweet

def main():
    fact = generate_fact()
    fact_with_flag = f"🤖: {fact} #AUTOMATED"
    response = post_tweet(fact_with_flag)
    print("Tweet Response:", response)

if __name__ == "__main__":
    main()
