import nextcord
from nextcord import Interaction, SlashOption
from nextcord.ext import commands
import random


with open('token.txt', 'r') as f:
    TOKEN = f.readline()

intents = nextcord.Intents.all()
client = commands.Bot(intents=intents, command_prefix="?")


@client.event
async def on_ready():
    print("Bot is Loaded!")


@client.slash_command(
        name="8ball",
        description="Ask The bot a Question and let it answer"
)
async def ball(
    interaction: Interaction,
    question = SlashOption(
        name="question",
        description="What do you want to ask"
    )
):
    responses = ["Yes, Of Course", "yes, With no doubt", "i am very sure thats true", "There is Nothing More True than That", "No, Thats False Information", "No.", "There is nothing More False Than That"]
    response = random.choice(responses)
    embed = nextcord.Embed(
        description=f"Question: {question}\nAnswer: {response}",
        color=nextcord.Color.random()
    )
    await interaction.response.send_message(embed=embed)



@client.slash_command(
    name="ping",
    description="See The Bots Ping"
)
async def _ping(
    interaction: Interaction,
):
    ping = client.latency * 1000
    await interaction.response.send_message(f"My Ping is {round(ping)}ms")


client.run(TOKEN)
