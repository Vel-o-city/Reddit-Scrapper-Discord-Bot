import discord
import praw

# Initialize the intents object
intents = discord.Intents.default()
intents.message_content=True
intents.messages=True

# Initialize the Discord bot client with intents
bot = discord.Client(intents=intents)

# Initialize the Reddit API wrapper
reddit = praw.Reddit(
    client_id="6cQQyxkGQOxQD1_USpOQaw",#my client id
    client_secret="geBqWor4swnVqUk-a1DRo3PZbH65wg",  #your client secret
    user_agent="scraper", #user agent name
    username = "6Sanket9",     # your reddit username
    password = "Srv@12345")     # your reddit password
def get_joke(x):
    sub = ['Jokes']
    for s in sub:
        subreddit = reddit.subreddit(s)   # Chosing the subreddit
        query = [x]
        joke_title="Sorry No matching jokes found"
        joke_body=""
        for item in query:
            for submission in subreddit.search(item,sort = "top",limit = 1):
                joke_title=submission.title
                joke_body=submission.selftext
    return joke_title,joke_body
async def send_joke_command(channel,word):
    title,body=get_joke(word)
    await channel.send(f"Here's a joke for '{word}':\n**{title}**\n{body}")
# Event when the bot is ready and connected to Discord
@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

# @bot.event
# async def on_message(message):
#     if message.content == "!test":
#         await message.channel.send("Test command received!")

# Event when a message is sent in a channel
@bot.event
async def on_message(message):
    # Ignore messages from the bot itself to avoid loops
    if message.author == bot.user:
        return

    if message.content.startswith("!joke"):
        # Get the word after the command
        word = message.content.replace("!joke", "").strip()
        # Get the word after the command
        await send_joke_command(message.channel, word)

# Run the bot with your Discord bot token
bot.run("MTEzMTU4ODk5NTMxNTQwNDk0MQ.GZjnDb.CXeTmQ9bDYybggcJCQiNL2fvLgbuy8pPFhBW1s")