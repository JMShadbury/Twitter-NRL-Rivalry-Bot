# Twitter-NRL-Rivalry-Bot

### Tweet status
![lint workflow](https://github.com/JMShadbury/Twitter-NRL-Rivalry-Bot/actions/workflows/tweet.yml/badge.svg)

## Description
This application is designed to generate fun and engaging content for sports fans, specifically focusing on rivalry and banter between different teams. Using the `Messages` enum, the bot can create specific prompts that are used to generate text based on the context of an upcoming sports event. The bot also incorporates team statistics into its generated content for added context and relevance.

## Features
- Generate system prompts based on the user's favorite team and the opponent.
- Craft humorous and engaging content to support a favorite team while playfully mocking the opponent.
- Handle cases where an opponent is not found or their Twitter handle is missing.
- Utilize team statistics to provide additional context and relevance to generated content.

## Installation
To set up the Sports Rivalry Bot, follow these steps:
1. Ensure you have Python installed on your machine. Python 3.8 or higher is recommended.
2. Clone this repository to your local machine.
3. Set up a virtual environment and install dependencies by running `make setup`.
4. Obtain necessary API keys and configurations as described in the project's documentation.

## Usage
The bot uses the following commands to interact:
- `generate_prompt(favorite_team_handle, opponent_handle)`: Generates a system prompt based on the provided team handles.
- In cases where the opponent's handle is missing or there's no match scheduled, appropriate messages from the enum will be used.

## Makefile
This project includes a Makefile for easy setup and operation. The following commands are available:
- `make setup`: Sets up a virtual environment and installs dependencies.
- `make get_data`: Fetches necessary data for the bot.
- `make run`: Runs the application.
- `make clean`: Removes the virtual environment and cleans up temporary files.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
