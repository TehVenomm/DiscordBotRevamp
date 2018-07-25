import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random

Client = discord.Client()
client = commands.Bot(command_prefix = ".")

meme_list = {"readpin":"https://cdn.discordapp.com/attachments/416087880629354499/469136788678508544/inhale_pin_meme.jpg",
             "tableflip":"https://media.giphy.com/media/op4n9nZWhQiZ2/giphy.gif",
             "dafuq":"https://cdn.discordapp.com/attachments/276918944072204289/350418144512180234/image.jpg",
             "facepalm":"https://media.giphy.com/media/JUMLTR3dHEGpW/giphy.gif",
             "salt":"https://media.giphy.com/media/l4Jz3a8jO92crUlWM/giphy.gif",
             "angry":"https://cdn.discordapp.com/attachments/416087880629354499/433879960860491776/6ad7f2385d44eb3b5a8b445b3c7917635a75ff37_hq.gif",
             "moneyslap":"https://cdn.discordapp.com/attachments/416087880629354499/431179068625518592/yato_money_slap.gif",
             "why":"https://media.giphy.com/media/1M9fmo1WAFVK0/giphy.gif",
             "stahp":"http://gifyu.com/images/stop-sign.gif",
             "glare":"https://cdn.discordapp.com/attachments/276918944072204289/323857157525209088/image.png",
             "what":"https://goo.gl/Mcdj4g",
             "everyone":"http://i3.kym-cdn.com/photos/images/original/001/263/237/be8.gif",
             "no":"https://media.giphy.com/media/12XMGIWtrHBl5e/giphy.gif",
             "whalemoar":"https://cdn.discordapp.com/emojis/462505685800845312.gif?v=1",
             "willsee":"https://cdn.discordapp.com/attachments/418978768422567966/470950415882649600/Screen_Shot_2561-07-23_at_20.45.11.png",
             "dlh":"https://cdn.discordapp.com/attachments/418978768422567966/470950271565037568/Screen_Shot_2561-07-23_at_20.47.50.png",
             "staytuned":"https://cdn.discordapp.com/attachments/418978768422567966/470952052181172253/image.png"}
meme_list_key = meme_list.keys()
meme_help = ""
for x in meme_list_key:
    meme_help += "`"
    meme_help += x
    meme_help += "` "

classes_dict = {"sns":"Sword & Shield","gs":"Great Sword","spear":"Spear","db":"Dual Blades","bow":"Bow"}
classes_dict_key = classes_dict.keys()

welcome_msg_start = ["Hi **<@{0}>**! Welcome to Dragon Project Community Server. Here's something you can do:",
                     "As **<@{0}>** walks in the deep forest, an old gateway appeared with a wooden sign in front of it saying:\nWelcome to Dragon Project Community Server:",
                     "Ding Dong! Pizzaman **<@{0}>** arrived the door of Dragon Project Community Server and saw a sign:\nHey there!",
                     "Woosh! **<@{0}>** got transported through the portal immediately when opening the letter that says:\nWelcome!"]
welcome_msg_core = ("\n1. Spend some time to read <#470713924325474304>;"
                    "\n2. Register a class in <#470713716573208576>;"
                    "\n3. If you are new to the game, definitely check out <#470713961768026152>"
                    "\n4. Quick browse on <#470713900690833412> and <#470713934517764117> to get hold of new stuffs"
                    "\n\nIf you have any questions, you may ask the `@Moderators` through PMs.")
welcome_msg_end = ["\nEnjoy your stay ~~and hope you pull As and Bs in gacha~~ <a:WHALEHARD:462505685800845312>",
                   "\nThe gateway suddenly opens....",
                   "\nSo......Where is my pizza? :pizza:",
                   "\nand got teleported into the server"]



@client.event
async def on_ready():
    print("Bot is ready!")
    server_test = client.get_server("348010091389124610")
    print(server_test.name)

##@client.command
##async def massunban(ctx):
##    server = ctx.message.server
##    ban_list = await client.get_bans(server)
##    for member in ban_list:
##        await client.unban(server,member)
##        await client.send_message(member, msg)
    

@client.event
async def on_message(message):
    if message.content.startswith(client.command_prefix):
        await command_list(message,message.content)

@client.event
async def on_member_join(member):
    #welcome message
    serverchannel = member.server.get_channel("470713608838578176")
    msg_rand = random.randint(0,3)
    msg = (welcome_msg_start[msg_rand]+welcome_msg_core+welcome_msg_end[msg_rand]).format(member.id)
    try:
        await client.send_message(serverchannel, msg)
    except Exception:
        pass

@client.event
async def command_list(message,command):
    command = str(command)[1:]
    command = command.lower()
    command_meme_check = command
    if " " in command:
        #check for meme
        command_meme_check = command.split()
        command_meme_check = command_meme_check[0]
    #start of all command
    #------------------------------------------------------------------------------------------------------------------------------------------------
    if (command.startswith("hello")) or (command.startswith("hi")):
        if "it's me" in command:
            await client.send_message(message.channel, "Hello on the other *SIIIIIIIIIIIIIIIIIIIIIDE*~")
        else:
            await client.send_message(message.channel, "Hello there!")
    elif command.startswith("msg"):
        msg = ("testing\n"
               "https://discord.gg/DanmfKS")
        server_test = client.get_server("348010091389124610")
        await client.unban(server_test, message.author)
        await client.send_message(message.author, msg)
        print(message.author.server)
    elif command.startswith("unban"):
        server = message.author.server
        member_list = client.get_all_members()
        main_server = client.get_server("348010091389124610")
        ban_list = await client.get_bans(main_server)
        print(len(ban_list))
        msg1 = ("This is Karyu. I am very sorry for the incident that happened not long ago."
               "\nThe bot had been hacked by someone unknown people who decided to make fun of the server, and it's my mistake to not check the settings throughly."
               "\nI have edited the bot so that the hacker doesn't get access to the new settings."
               "\nHere, I sincerely invite you to come back to the server. I hope you can give me a second chance in managing the server. Thank you."
               "\nhttps://discord.gg/HQM6YVX"
               "\nPS, if you already joined back, just ignore the message, thanks")
        for member in member_list:
            if member in ban_list:
                try:
                    await client.unban(main_server,member)
                    await client.send_message(member, msg1)
                    print(len(ban_list))
                except Exception:
                    pass
            else:
                print(len(ban_list))
    elif command.startswith("help"):
        #display help embed
        emb_msg = await help_embed()
        await client.send_message(message.channel, embed = emb_msg)
    elif command.startswith("addclass"):
        #adding class roles
        class_tag = 0
        if " " in command:
            class_tag = command.split()
            class_tag = class_tag[1] #get the first class tag only to ignore anything behind
        else:
            await client.send_message(message.channel, "Please state which class role you want to add")
        if message.channel.name == "weapon-class":
            if class_tag in classes_dict_key:
                if class_tag in command:
                    roleID = discord.utils.get(message.author.server.roles, name = classes_dict[class_tag])
                    if roleID in message.author.roles:
                        msg = "You already have " + classes_dict[class_tag] + " class"
                        await client.send_message(message.channel, msg)
                    else:
                        msg = classes_dict[class_tag] + " class is added"
                        await client.add_roles(message.author, roleID)
                        await client.send_message(message.channel, msg)
            else:
                await client.send_message(message.channel, "You don't have permission to add this class or it's an invalid class")
        else:
            await client.send_message(message.channel, "You can't use this command here")
    elif command.startswith("removeclass"):
        #remove class tag
        class_tag = 0
        if " " in command:
            class_tag = command.split()
            class_tag = class_tag[1] #get the first class tag only to ignore anything behind
        else:
            await client.send_message(message.channel, "Please state which class role you want to remove")
        if message.channel.name == "weapon-class":
            if class_tag in classes_dict_key:
                if class_tag in command:
                    roleID = discord.utils.get(message.author.server.roles, name = classes_dict[class_tag])
                    if roleID in message.author.roles:
                        msg = classes_dict[class_tag] + " class has been removed"
                        await client.remove_roles(message.author, roleID)
                        await client.send_message(message.channel, msg)
                    else:
                        msg = "You don't have a " + classes_dict[class_tag] + " class in your existing roles"
                        await client.send_message(message.channel, msg)
            else:
                await client.send_message(message.channel, "You don't have permission to remove this class or it's an invalid class")
        else:
            await client.send_message(message.channel, "You can't use this command here")
    elif (command.startswith("database")) or (command.startswith("db")):
        #give database link command
        front_msg = ["That effort to summon the Bible is looking bad, but since I'm generous so here you go:\n",
                     "Here is the link to the database:\n",
                     "Thanks for using the express service! Here's the Bible you ordered:\n",
                     "Moshi moshi, database desu:\n",
                     "Suddenly a wind blew up, and a Bible link lands in front of you:\n"]
        random_msg_num = random.randint(0,4)
        msg = front_msg[random_msg_num]+"https://docs.google.com/spreadsheets/d/1iMoiSjTbahFxfOyU4F4_xOWtS3Va22_J1tyizyDltNU/edit?usp=sharing"
        await client.send_message(message.channel, msg)
    elif command.startswith("memelist"):
        #get list of meme embed
        emb = (discord.Embed(title="List of memes", description= (meme_help), colour=0xFF0000))
        await client.send_message(message.channel, embed = emb)
    elif not command_meme_check.isalpha():
        pass


@client.event
async def help_embed():
    emb = (discord.Embed(title="Karyu Help", description="Need some help on what commands I have? Read the following:", colour=0xFFFFFF))
    emb.set_thumbnail(url = "https://cdn.discordapp.com/attachments/349266633476538368/469151696048750593/stmp_10000018.png")
    emb.add_field(name = "Database command:", value = "`.db` or `.database`", inline=False)
    emb.add_field(name = "Class command:", value = "`.addclass <class>` and `.removeclass <class>`",inline=False)
    emb.add_field(name = "List of meme command:", value = "`.memelist`",inline=False)
    return emb


#MEMES FROM NOW ON

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


try:
    client.run("TOKEN HERE")
except Exception:
    client.loop.run_until_complete(client.logout())
