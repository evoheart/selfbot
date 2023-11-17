import discord
from discord.ext import commands
import requests
import asyncio

client = commands.bot(command_prefix='.')

ltc = ""
qr = ""
bank1 = ""
bank2 = ""
twitch_url = "https://twitch.tv/wallibear" 





@client.command()
@commands.cooldown(1, 2, commands.BucketType.user)
async def boosts(ctx):
    await ctx.reply(f"> **This Server Has {ctx.guild.premium_subscription_count} Boosts**")


@client.command()
async def prefix(ctx):
    await ctx.reply('**> Default Prefix For This Selfclient Is** ```.```')

@client.command()
async def servernuke(ctx, amount: int = 25):
    for chn in ctx.guild.channels:
        await chn.delete()
    for i in range(30):
        await ctx.guild.create_text_channel("samir nuker")
        await ctx.guild.edit(name="Nuked By Samir")


@client.command()
async def calc(ctx, *, expression):
    try:
        result = eval(expression)
        await ctx.send(f'Result: {result}')
    except Exception as e:
        await ctx.send(f'Error: {e}')


@client.command()
async def massreact(ctx, emote):
    await ctx.message.delete()
    messages = await ctx.message.channel.history(limit=20).flatten()
    for message in messages:
        await message.add_reaction(emote)


@client.command(aliases=["streaming"])
async def stream(ctx, *, message):
    await ctx.reply("Samir xD | Changing Status.....", mention_author=True)
    stream = discord.Streaming(
        name=message,
        url="https://twitch.tv/https://Wallibear",
    )
    await client.change_presence(activity=stream)
    await ctx.reply("Streaming created!", mention_author=True)


@client.command(aliases=["playing"])
async def play(ctx, *, message):
    game = discord.Game(name=message)
    await ctx.reply("Samir xD | Changing Status......", mention_author=True)
    await client.change_presence(activity=game)
    await ctx.reply("Playing Created!", mention_author=True)


@client.command(aliases=["watch"])
async def watching(ctx, *, message):
    await ctx.reply("Samir xD | Changing Status.....", mention_author=True)
    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name=message))
    await ctx.reply("Watching created!", mention_author=True)



@client.command(aliases=["listen"])
async def listening(ctx, *, message):
    await ctx.reply("Samir xD | Changing Status.....", mention_author=True)
    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.listening,
        name=message,
    ))
    await ctx.reply("Listening created!", mention_author=True)


@client.command()
async def vouch(ctx):
    await ctx.message.delete()
    await ctx.send(
        '**> https://discord.gg/aTESAXDVQa \n\n VOUCH HERE \n FORMAT : +rep {user} Legit Got {quantity}{product} For {price} {method}| Thank You**'
    )


@client.command()
async def qr(ctx):
    await ctx.reply(f"> **Pay and Drop ScreenShot : **\n {qr}")

@client.command()
async def avatar(ctx, member: discord.Member):
    await ctx.reply(f'{member.avatar_url}')


@client.command()
async def ltc(ctx):
    await ctx.reply(f"> **Pay and Drop ScreenShot : ** {ltc}")


client.run("MTE3MjkyNTE4NzI3Mjk5OTAyNQ.Gtb1H9.F0CwXKG_laAErYH2zrRQTZr8FytcbywfC8JhCs" , bot=False)