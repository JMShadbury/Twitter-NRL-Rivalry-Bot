from openai import OpenAI
from .config import GPT_API_KEY
from .scraper import WebScraper  
from .constants import AccountHandle, Messages, Team
import requests

client = OpenAI(api_key=GPT_API_KEY)

def download_image_from_url(url, save_path):
    """Download an image from a URL and save it to a specified path."""
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as out_file:
            for chunk in response.iter_content(chunk_size=1024):
                out_file.write(chunk)
        return save_path
    else:
        raise Exception(f"Failed to download image from URL: {response.status_code}")


def generate_image(prompt):
    """Generate an image based on the provided prompt using OpenAI's image generation API and returns the image path."""
    try:
        response = client.images.generate(
            model="dall-e-3", 
            prompt=prompt,
            n=1,  
            size="1024x1024"  
        )

        image_url = response.data[0].url
        image_path = 'generated_image.jpg'  
        return download_image_from_url(image_url, image_path)
    except Exception as e:
        raise Exception(f"Failed to generate image: {str(e)}")


def generate_fact_and_image():
    scraper = WebScraper()
    team_data = scraper.get_team_data()
    opponent = scraper.get_opponent(team_data)
    
    favorite_team = Team.FAVORITE_TEAM.value
    favorite_team_handle = getattr(AccountHandle, favorite_team.replace(" ", "_").upper(), None)
    
    if not favorite_team_handle:
        return "Favorite team handle not found in ENUM."
    
    if opponent:
        opponent_team = opponent['opponent_team'].replace(" ", "_").upper()
        opponent_handle = getattr(AccountHandle, opponent_team, None)
        if opponent_handle:
            text_prompt = Messages.OPPONENT_FOUND.value.format(favorite_team_handle=favorite_team_handle.value, opponent_handle=opponent_handle.value)
            image_prompt = Messages.IMAGE_PROMPT.value.format(favorite_team_handle=favorite_team_handle.value, opponent_handle=opponent_handle.value)
        else:
            text_prompt = Messages.OPPONENT_HANDLE_NOT_FOUND.value
            image_prompt = Messages.IMAGE_PROMPT.value.format(favorite_team_handle=favorite_team_handle.value, opponent_handle="the opposing team")
    else:
        text_prompt = Messages.NO_OPPONENT_FOUND.value.format(favorite_team_handle=favorite_team_handle.value)
        image_prompt = Messages.IMAGE_PROMPT.value.format(favorite_team_handle=favorite_team_handle.value, opponent_handle="other teams")
    
    text_response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": Messages.SYSTEM_PROMPT.value},
            {"role": "user", "content": text_prompt}
        ]
    )
    new_fact = text_response.choices[0].message.content.strip().strip('"')
    

    image_path = generate_image(image_prompt)  
    
    return new_fact, image_path

