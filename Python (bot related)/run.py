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
async def behemoth(ctx, a):
    filteredInput = myUtilities.filterInput(a)
    queryResults = myUtilities.fetchBehemothDB(filteredInput)

    if (len(queryResults) == 1):
        embed = myUtilities.behemothEmbed(queryResults)
        await ctx.send(embed=embed)
    else:
       await ctx.send("Behemoth not found.")

@bot.command()
async def weapon(ctx, a): #NOT IMPLEMENTED
    filteredInput = myUtilities.filterInput(a)
    queryResults = myUtilities.fetchWeaponDB(filteredInput)

    if (len(queryResults) == 1):
        embed = myUtilities.weaponEmbed(queryResults)
        await ctx.send(embed=embed)
    else:
       await ctx.send("Behemoth not found.")

@bot.command()
async def armor(ctx, a): #NOT IMPLEMENTED
    filteredInput = myUtilities.filterInput(a)
    queryResults = myUtilities.fetchBehemothDB(filteredInput)
    if (len(queryResults) == 1):
        await ctx.send(queryResults)
    else:
       await ctx.send("Behemoth not found.")






@bot.command()
async def sendfile(ctx):
    embed = discord.Embed(title="DDDDDDDDDDDDDDDDDD")
    embed.set_image(url="https://cdn.discordapp.com/embed/avatars/0.png")
    await ctx.send(embed=embed)

@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

@bot.command()
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="nice bot", description="Nicest bot there is ever.", color=0xeee657)
    
    # give info about you here
    embed.add_field(name="Author", value="TeH_Venom")
    
    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    await ctx.send(embed=embed)

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="nice bot", description="A Very Nice bot. List of commands are:", color=0xeee657)

    embed.add_field(name="$add X Y", value="Gives the addition of **X** and **Y**", inline=False)
    embed.add_field(name="$multiply X Y", value="Gives the multiplication of **X** and **Y**", inline=False)
    embed.add_field(name="$greet", value="Gives a nice greet message", inline=False)
    embed.add_field(name="$cat", value="Gives a cute cat gif to lighten up the mood.", inline=False)
    embed.add_field(name="$info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name="$help", value="Gives this message", inline=False)

    await ctx.send(embed=embed)

# Experimental commands to unfuck the server
@bot.command()
async def addrole(ctx):
    role = discord.utils.get(ctx.guild.roles, name="Fuckupfixer")
    user = ctx.message.author
    await user.add_roles(role)

#MEMES
@bot.command()
async def dafuq(ctx):
    embed = discord.Embed()
    embed.set_image(url="https://cdn.discordapp.com/attachments/276918944072204289/350418144512180234/image.jpg")
    await ctx.send(embed=embed)

@bot.command()
async def facepalm(ctx):
    embed = discord.Embed()
    embed.set_image(url="https://media.giphy.com/media/JUMLTR3dHEGpW/giphy.gif")
    await ctx.send(embed=embed)

@bot.command()
async def salt(ctx):
    embed = discord.Embed()
    embed.set_image(url="https://media.giphy.com/media/l4Jz3a8jO92crUlWM/giphy.gif")
    await ctx.send(embed=embed)

@bot.command()
async def angry(ctx):
    embed = discord.Embed()
    embed.set_image(url="https://cdn.discordapp.com/attachments/416087880629354499/433879960860491776/6ad7f2385d44eb3b5a8b445b3c7917635a75ff37_hq.gif")
    await ctx.send(embed=embed)

@bot.command()
async def moneyslap(ctx):
    embed = discord.Embed()
    embed.set_image(url="https://cdn.discordapp.com/attachments/416087880629354499/431179068625518592/yato_money_slap.gif")
    await ctx.send(embed=embed)

@bot.command()
async def why(ctx):
    embed = discord.Embed()
    embed.set_image(url="https://media.giphy.com/media/1M9fmo1WAFVK0/giphy.gif")
    await ctx.send(embed=embed)

@bot.command()
async def stahp(ctx):
    embed = discord.Embed()
    embed.set_image(url="http://gifyu.com/images/stop-sign.gif")
    await ctx.send(embed=embed)

@bot.command()
async def glare(ctx):
    embed = discord.Embed()
    embed.set_image(url="https://cdn.discordapp.com/attachments/276918944072204289/323857157525209088/image.png")
    await ctx.send(embed=embed)

@bot.command()
async def what(ctx):
    embed = discord.Embed()
    embed.set_image(url="https://goo.gl/Mcdj4g")
    await ctx.send(embed=embed)

@bot.command()
async def everyone(ctx):
    embed = discord.Embed(title="@everyone")
    embed.set_image(url="http://i3.kym-cdn.com/photos/images/original/001/263/237/be8.gif")
    await ctx.send(embed=embed)

@bot.command()
async def no(ctx):
    embed = discord.Embed()
    embed.set_image(url="https://media.giphy.com/media/12XMGIWtrHBl5e/giphy.gif")
    await ctx.send(embed=embed)

@bot.command()
async def whalemoar(ctx):
    embed = discord.Embed()
    embed.set_image(url="https://cdn.discordapp.com/emojis/462505685800845312.gif?v=1")
    await ctx.send(embed=embed)

@bot.command()
async def willsee(ctx):
    embed = discord.Embed()
    embed.set_image(url="https://cdn.discordapp.com/attachments/418978768422567966/470950415882649600/Screen_Shot_2561-07-23_at_20.45.11.png")
    await ctx.send(embed=embed)

@bot.command()
async def dlh(ctx):
    embed = discord.Embed()
    embed.set_image(url="https://cdn.discordapp.com/attachments/418978768422567966/470950271565037568/Screen_Shot_2561-07-23_at_20.47.50.png")
    await ctx.send(embed=embed)

@bot.command()
async def staytuned(ctx):
    embed = discord.Embed()
    embed.set_image(url="https://cdn.discordapp.com/attachments/418978768422567966/470952052181172253/image.png")
    await ctx.send(embed=embed)

@bot.command()
async def readpin(ctx):
    embed = discord.Embed()
    embed.set_image(url="https://cdn.discordapp.com/attachments/416087880629354499/469136788678508544/inhale_pin_meme.jpg")
    await ctx.send(embed=embed)


@bot.command()
async def tableflip(ctx):
    embed = discord.Embed()
    embed.set_image(url="https://media.giphy.com/media/op4n9nZWhQiZ2/giphy.gif")
    await ctx.send(embed=embed)

bot.run(secrets.getToken())