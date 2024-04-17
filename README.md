# Twitter-NRL-Rivalry-Bot

## Description
This application is designed to generate fun and engaging content for sports fans, specifically focusing on rivalry and banter between different teams. Using the `Messages` enum, the bot can create specific prompts that are used to generate text based on the context of an upcoming sports event.

## Features
- Generate system prompts based on user's favorite team and the opponent.
- Craft humorous and engaging content to support a favorite team while playfully mocking the opponent.
- Handle cases where an opponent is not found or their Twitter handle is missing.

## Installation
To set up the Sports Rivalry Bot, follow these steps:
1. Ensure you have Python installed on your machine. Python 3.8 or higher is recommended.
2. Clone this repository to your local machine.

## Setup with Makefile
This project uses a Makefile for easy setup and operation. To use it, perform the following:
- Run `make setup` to create a virtual environment and install all dependencies.
- Run `make run` to start the application.
- Run `make clean` to remove the virtual environment and clean up all temporary files.

## Usage
The bot uses the following commands to interact:
- `generate_prompt(favorite_team_handle, opponent_handle)`: Generates a system prompt based on the provided team handles.
- In cases where the opponent's handle is missing or there's no match scheduled, appropriate messages from the enum will be used.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
