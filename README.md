# Reddit Modmail Bot

![Python](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white) ![Open-Source](https://img.shields.io/badge/Open%20Source%20Initiative-3DA639.svg?style=for-the-badge&logo=Open-Source-Initiative&logoColor=white)

This is a Reddit bot that helps in making Reddit moderation easier.

Here's how the Reddit Modmail Bot functions:

 - The `redditmodmail.py` file is executed
 - The bot starts running in an infinite loop
 - It waits and listen to a designated sub Modmail queue
 - The said Modmail queue received a new message
 - The bot sends an alert to a designated Discord server with the name of the sender of the message

This bot is created using Python, and utilizes PRAW and Discord Webhooks to communicate with Reddit and Discord. This makes it pretty lightweight and easier to code.

## How to run this bot

I am running this Bot using GitHub Actions. The `redditmodmailbot.yml` file, located in the `.github/workflows/` directory of the repo, contains the instruction to run the bot on GitHub. The `*/10 * * * *` specifies a cron job which runs the bot every 10th minutes. However, `workflow_dispatch:` ensures that the bot can also be run manually.

## List of requirements

The `requirements.txt` file contains all the modules required to compile and run this bot.

Please note that we need to downgrade the `Discord.py` version to `1.7.2`, otherwise it would get a **AttributeError: module 'discord' has no attribute 'RequestsWebhookAdapter' error**. Thanks to [r/Lil_SpazJoekp](https://www.reddit.com/r/Lil_SpazJoekp) for their help in resolving this issue.

## Proposed improvements

Here are some of the points of improvements that can be implemented:

 - The bot can be made to listed to new submissions and posts instead of just Modmail
 - Can be used to monitor offensive/spam keywords

## Contribution

This is an open-source project. We invite your participation through issues and pull requests! Please ensure that you follow the [contributing guidelines](CONTRIBUTING.md). Also, do go through out [code of conduct](CODE_OF_CONDUCT.md) guidelines for contributors.

## List of Contributors

![GitHub Contributors Image](https://contrib.rocks/image?repo=rajtilakjee/redditmodmailbot)

## Additional Notes

This bot can be run 24/7 on PythonAnywhere service.
