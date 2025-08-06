import discord
from discord import app_commands
from discord.ext import commands
import os

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logget ind som {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Kommandoer synkroniseret: {len(synced)}")
    except Exception as e:
        print(f"Fejl ved sync: {e}")

@bot.tree.command(name="raid_done", description="Annoncer at et raid er færdigt.")
@app_commands.describe(
    image="Upload et billede fra raidet",
    participants="Nævn deltagerne"
)
async def raid_done(interaction: discord.Interaction, image: discord.Attachment, participants: str):
    embed = discord.Embed(
        title="✅ Raid gennemført!",
        description=f"**Deltagere:** {participants}",
        color=discord.Color.green()
    )
    embed.set_image(url=image.url)
    embed.set_footer(text=f"Annonceret af {interaction.user.display_name}")

    await interaction.response.send_message(embed=embed)

bot.run(os.getenv("DISCORD_BOT_TOKEN"))
