from discord.ext import commands
import os
import sys
#from dotenv import load_dotenv

# Add path the modules
sys.path.append("./src/cogs")

# Load environment vars from .env
#load_dotenv()

# Inialize the discord bot
bot = commands.Bot(command_prefix=commands.when_mentioned_or('#'), help_command=None)
TOKEN = os.getenv("TOKEN")

# Load extensions
for file in os.listdir("./src/cogs"):
    if file.endswith(".py") and file != 'database.py' and file != 'agent.py':
        # Cog folder has to be in the same directory as main.py
        bot.load_extension(f'cogs.{file[:-3]}') # Remove the ".py"

if __name__ == "__main__":
    bot.run(TOKEN)
