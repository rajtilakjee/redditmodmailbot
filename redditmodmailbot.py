import praw
import discord
import os
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv('API_CLIENT'),
    client_secret=os.getenv('API_SECRET'),
    password=os.getenv('REDDIT_PASSWORD'),
    user_agent="Reddit Modmail Bot",
    username=os.getenv('REDDIT_USERNAME'),
    check_for_async=False
)

target_sub = "artofml"
subreddit = reddit.subreddit(target_sub)

webhook = discord.Webhook.from_url(os.getenv('DISCORD_URL'), adapter=discord.RequestsWebhookAdapter())

for modmail_conversation in subreddit.mod.stream.modmail_conversations(state='new'):
  author=str(modmail_conversation.authors[0])
  webhook.send("New Modmail from " + author)