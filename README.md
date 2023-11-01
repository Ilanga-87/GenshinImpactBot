# Genshin Impact Bot
This is noncommercial informative bot for Genshin Impact players. 
It helps users obtain statistics about in-game characters, such as the number of Pyro characters available in Inazuma at the moment.

To use the bot without installation, visit: https://t.me/GenshinImpactCharsBot or search for @GenshinImpactCharsBot on Telegram.

## Description

The bot is written using the Python-Telegram-Bot module.

## Getting started

### Dependencies

- OS Linux or Windows with WSL2 support
- Docker

## Preparation

First, you need to obtain a token for your Telegram bot using BotFather.

## Installation

To install via Docker, follow these steps:

1. Clone this git repository by running the following command in your Linux/WSL terminal:
```commandline
git clone https://github.com/Ilanga-87/GenshinImpactBot
```
2. Navigate to the project directory using the "cd" command:

```commandline
cd GenshinImpactBot/
```

3. Create an ".env" file in the project directory and fill in the TELEGRAM_TOKEN variable:
```commandline
nano .env
```

```commandline
TELEGRAM_TOKEN=token_you_get_from_botfather
```

6. To build production image and run container, use the following command:
```
docker compose up --build -d
```

## Usage

Once the installation is complete, open your bot in Telegram. Now you can filter characters based on the options that interest you.


## Features

- Selection based on 4 options: region, weapon, element, rarity.
- Double selection by two options if necessary.
- Simple interface.
- Detailed output.

If you encounter any issues or have questions, feel free to reach out for support.
