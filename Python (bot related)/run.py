import discord
from discord.ext import commands
import myUtilities
import secrets

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def behemoth(ctx, *a):
    i = 0
    joinedInput = " ".join(a)
    filteredInput = myUtilities.filterInput(joinedInput)
    inputWordArray = filteredInput.split()

    attributesArray = myUtilities.matchWeaponAttributes(inputWordArray)
    for key, content in attributesArray.items():
        if (content):
            i+=1

    if (i > 1):
        queryResults = myUtilities.fetchBehemothByTypeDB(attributesArray)
    else:
        queryResults = myUtilities.fetchBehemothDB(filteredInput)

    if (len(queryResults) > 0 and len(queryResults) <= 10):
        embed = myUtilities.behemothEmbedGenerator(queryResults, filteredInput)
        await ctx.send(embed=embed)
    else:
        await ctx.send("Behemoth not found.")


@bot.command()
async def weapon(ctx, *a):
    joinedInput = " ".join(a)
    filteredInput = myUtilities.filterInput(joinedInput)
    queryResults = myUtilities.fetchWeaponDB(filteredInput)

    if (len(queryResults) == 1):
        embed = myUtilities.weaponEmbed(queryResults)
        await ctx.send(embed=embed)
    else:
        await ctx.send("Behemoth not found.")

@bot.command()
async def armor(ctx, *a):
    joinedInput = " ".join(a)
    filteredInput = myUtilities.filterInput(joinedInput)
    queryResults = myUtilities.fetchArmorDB(filteredInput)

    if (len(queryResults) == 4):
        embed = myUtilities.armorEmbed(queryResults)
        await ctx.send(embed=embed)
    else:
        await ctx.send("Behemoth not found.")

@bot.command()
async def magi(ctx, *a):
    joined = " ".join(a)
    filteredInput = myUtilities.filterInput(joined)
    queryResults = myUtilities.fetchMagiDB(filteredInput)

    if (len(queryResults) > 0 and len(queryResults) <= 10):
        embed = myUtilities.magiEmbedGenerator(queryResults, filteredInput)
        await ctx.send(embed=embed)
    else:
        await ctx.send("Magi not found.")

bot.run(secrets.getToken())