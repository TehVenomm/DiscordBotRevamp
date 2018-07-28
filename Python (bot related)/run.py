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
    joinedInput = " ".join(a)
    filteredInput = myUtilities.filterInput(joinedInput)
    queryResults = myUtilities.fetchBehemothDB(filteredInput)

    if (len(queryResults) == 1):
        embed = myUtilities.behemothEmbed(queryResults)
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
    await ctx.send(queryResults)
    
#    if (len(queryResults) == 1):
#        embed = myUtilities.MagiEmbed(queryResults)
#        await ctx.send(embed=embed)
#    elif (len(queryResults) >= 1):
#        embed = myUtilities.ListMagiEmbed(queryResults)
#        await ctx.send(embed=embed)
#    elif (len(queryResults) == 0):
#        await ctx.send("Magi not found.")
    
@armor.error
async def armor_on_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title="The correct syntax is:", colour=discord.Colour(0xff0000), description="`?armor [Behemoth's name]`")
        await ctx.send(embed=embed)
    raise error

@weapon.error
async def weapon_on_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title="The correct syntax is:", colour=discord.Colour(0xff0000), description="`?weapon [Behemoth's name]`")
        await ctx.send(embed=embed)
    raise error

@behemoth.error
async def behemoth_on_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title="The correct syntax is:", colour=discord.Colour(0xff0000), description="`?behemoth [Behemoth's name]`")
        await ctx.send(embed=embed)
    raise error


bot.run(secrets.getToken())