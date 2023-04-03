import nextcord as discord 
from nextcord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()


intents = discord.Intents.all()
client = commands.Bot(command_prefix=os.getenv("PREFIX"), intents=intents) 

#start event
@client.event
async def on_ready():
    print("Online!")

#spam command
@client.slash_command(description="This command spam at dm", guild_ids=[os.getenv("GUILDID")])
async def spam(interaction: discord.Interaction, user: discord.User, content: str, count: int):
    count1 = 0
    await interaction.send("Próbuje wysłać wiadomość..")
    for count1 in range(count):
        await user.send(f"{content}")
        count1 = count1 + 1
    await interaction.send("Wiadomość wysłana!")

@client.command()
async def spam(ctx, user: discord.User , count: int, *, content: str,):
    count1 = 0
    await ctx.send("Próbuje wysłać wiadomość..")
    for count1 in range(count):
        await user.send(f"{content}")
        count1 = count1 + 1
    await ctx.send("Wiadomość wysłana!")




#START BOT
client.run(os.getenv("TOKEN"))