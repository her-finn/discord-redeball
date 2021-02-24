import discord
from discord.ext import commands
from discord.utils import get
from pprint import pprint
import time
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="/redeball ", intents=intents,help_command=None)
#Wenn Bot Startklar ist
@bot.event
async def on_ready():
    print("Bot is ready")

@bot.command(pass_context=True)
async def self(ctx,warten=30):
    members = ctx.author.voice.channel.members
    pprint(members)
    for i in range(len(members)):
        await members[i].edit(mute=True)
    await ctx.author.edit(mute=False)
    time.sleep(warten)
    for i in range(len(members)):
        await members[i].edit(mute=False)

#Redeball durchreichen
@bot.command(pass_context=True)
async def start(ctx,warten=30):
    members = ctx.author.voice.channel.members
    pprint(members)
    
    for i in range(len(members)):
        pprint(members[i])
        await members[i].edit(mute=True)
    for i in range(len(members)):
        await members[i].edit(mute=False)
        time.sleep(int(warten))
        await members[i].edit(mute=True)
    for i in range(len(members)):
        pprint(members[i])
        await members[i].edit(mute=False)

@bot.command(pass_context=True)
async def help(ctx):
    embed=discord.Embed(title="Redeball-Hilfe", description="**/redeball start *<Sekunden>*** : Startet den Redeball und jeder Benutzer darf *<Sekunden>* lang reden \n \n **/redeball self *<Sekunden>*** : Der Benutzer, der den Befehl ausgeführt hat darf *<Sekunden>* lang reden",color=0x32CD32)
    embed.set_footer(text=f"Redeball 1.0 --- her-finn")
    await ctx.send(embed=embed)


bot.run("<Der Token deines Bots>")

