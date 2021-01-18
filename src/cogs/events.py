from discord.colour import Colour
from discord.ext import commands
#import dialogflow_v2
from agent import detect_intent_texts
import database
import discord

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @commands.Cog.listener()
    async def on_ready(self):
        print("Help Bot is online!")
    
    @commands.Cog.listener()
    async def on_message(self, message):
        # If the message is from the bot then skip
        if message.author == self.bot.user:
            return
        elif not message.content.startswith('#'): 
            print(message.content)
            response = detect_intent_texts("commandlinehelper-fvr9","123456789",message.content,"en-US")
            await self.handle_query(response=response, message = message)


    async def handle_query(self, response, message):
        command_list = database.command_list
        name = str(response.query_result.intent.display_name)

        list = ["Welcome", "Fallback"]

        if name in list:
            something = response.query_result.fulfillment_text
            await message.channel.send(something)
            return


        await message.channel.send("Info retrieving...", delete_after = 0.5)
        query = {name: name}
        command = command_list.find_one(query)
        
        # If no info is found, let user know
        if command is None:
            await message.channel.send("No infomation available yet! Stay tuned!")
            return

        em = discord.Embed(
            title = name,
            colour = discord.Color.orange(),
            description = f"Brief info & sample usage"
        )
            
        em.add_field(name = "__Info__", value = command["info"], inline=False)
        em.add_field(name = "__Sample__", value = command["example"], inline=False)
        await message.channel.send(embed = em)

           
        



def setup(bot):
    bot.add_cog(Events(bot))
    print("Cog Event loaded")


