from .tweet import post_tweet, upload_media
from util.generator import generate_fact_and_image  # Updated import

def main():
    # Generate both fact and image
    fact, image_path = generate_fact_and_image()
    
    # Ensure image path is not None before proceeding
    if image_path:
        with open(image_path, 'rb') as img:
            media_id = upload_media(img)  
        tweet_text = f"🤖: {fact} #AUTOMATED"
        response = post_tweet(tweet_text, media_id=media_id)
        print("Tweet Response:", response)
    else:
        print("Failed to generate image, only text will be posted.")
        tweet_text = f"🤖: {fact} #AUTOMATED"
        response = post_tweet(tweet_text)
        print("Tweet Response:", response)

if __name__ == "__main__":
    main()
