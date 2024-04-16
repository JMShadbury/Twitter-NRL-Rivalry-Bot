from util.generator import generate_fact
from .tweet import post_tweet

def main():
    fact = generate_fact()
    fact = "Did you know the Brisbane Broncos have won the grand finale more often on even years? That's right, they've claimed glory in '92, '93, '97, '98, '06! Maybe they have an undisclosed secret affinity for numbers divisible by 2? 🤔😂"
    fact_with_flag = f"🤖 {fact} #NRL"
    response = post_tweet(fact_with_flag)
    print("Tweet Response:", response)

if __name__ == "__main__":
    main()
