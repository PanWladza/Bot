# Mójbot hahaha

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk

bot = commands.Bot(command_prefix='W')

@bot.event
async def on_ready():
    print ("Biegam")
    print ("Skaczę")
    print ("Walczę")
    print (bot.user.name + bot.user.id)

@bot.command(pass_context=True)
async def coo(ctx):
    await bot.say("https://www.youtube.com/watch?v=RiiafmmqWHE")
    print ("niewiadomo")

@bot.command(pass_context=True)
async def noo(ctx):
    await bot.say("https://www.youtube.com/watch?v=lNbcA78d1Q8")

@bot.command(pass_context=True)
async def walka(ctx, user: discord.Member):
    await bot.say("**Niezboczony** ``{}".format(user.name) + "`` **walczy od** ``{}".format(user.joined_at) + "``")
    await bot.say("**Aktualny stan walki:** ``{}".format(user.status) + "``")
    print("Info o walczącym")


@bot.command(pass_context=True)
async def itam(ctx):
   await bot.say("Witam.", tts=False)

@bot.command(pass_context=True)
async def ITAM(ctx):
   await bot.say("Nie krzycz :worried:", tts=False)
   print ("Krzyczo")

@bot.command(pass_context=True)
async def zapierdolmu(ctx, user: discord.Member):
   await bot.say("https://78.media.tumblr.com/6cacb214427fdd8a1710a842e8d33cd6/tumblr_obbhm581P71t0gmsbo4_540.gif", tts=False)

@bot.command(pass_context=True)
async def amen(ctx):
   await bot.say("http://esauproject.com/wp-content/uploads/2016/06/HL2.png", tts=False)

@bot.command(pass_context=True)
async def apiesz(ctx):
   await bot.say("https://i.ytimg.com/vi/UC4LbHZovy4/hqdefault.jpg", tts=False)

@bot.command(pass_context=True)
async def papież(ctx):
    await bot.say("https://youtu.be/PLc7TYJYnAo")
    await bot.say("https://www.youtube.com/watch?v=NsYdmajMMOI")
    await bot.say("https://www.youtube.com/watch?v=NsYdmajMMOI")
    await bot.say("https://i.ytimg.com/vi/UC4LbHZovy4/hqdefault.jpg")
    await bot.say("https://www.youtube.com/watch?v=RHSJ8xTMc4w")
    await bot.say("https://www.youtube.com/watch?v=6NR-Lq-hhSw")
    await bot.say("https://youtu.be/Cgbwnp-GD28")
    await bot.say("https://www.youtube.com/watch?v=I4wytulZwaE")
    await bot.say("https://www.youtube.com/watch?v=egimhkHJI0I")
    await bot.say("https://www.youtube.com/watch?v=oUKEdSR2hSA")
    await bot.say("https://www.youtube.com/watch?v=pl_yerjJ1wM")
    await bot.say("https://www.youtube.com/watch?v=Gy-6IjuwkEY")
    await bot.say("https://www.youtube.com/watch?v=QOlxpPmY8cU")

@bot.command(pass_context=True)
async def uganda(ctx):
    await bot.say("https://www.youtube.com/watch?v=8w0SpnL_Ysg")
    await bot.say("https://www.youtube.com/watch?v=CZcMBWttLKs")
    await bot.say("https://www.youtube.com/watch?v=amnMq8_UdiE")
    await bot.say("https://www.youtube.com/watch?v=dXp0m9AM3aY")

@bot.command(pass_context=True)
async def hehe(ctx):
    await bot.say("https://www.youtube.com/watch?v=H01RWxMctMo")

bot.run("NDM1ODc0ODg1Nzk3OTM3MTUy.DbzMKA.S0FU5E--lFvnbmWOU5f2EbLgGO0")
