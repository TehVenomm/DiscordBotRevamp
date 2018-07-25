import pymysql.cursors
import pymysql
import discord
from discord.ext import commands
import re
import secrets

########## EXAMPLE OF getConnection() in secrets.py
#def getConnection():
#    connection = pymysql.connect(host='localhost',
#                                user='username',
#                                password='password',
#                                db='database',
#                                charset='utf8mb4',
#                                cursorclass=pymysql.cursors.DictCursor)
#    return connection


def filterInput(inputString):
    newString = re.sub('[^A-Za-z0-9\s]+', '', inputString)
    return newString

def fetchBehemothDB(name):
    connection = secrets.getConnection()
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT B.Name AS BeheName, B.Element as BeheElement, W.Type AS WepType, W.Tier AS WepTier, W.Ability AS WepAbility, A.Ability AS ArmourAbility FROM behemothtable AS B INNER JOIN weapontable AS W ON W.IdWeapon = B.IdWeapon_BehemothTable INNER JOIN armourtable AS A ON A.IdBehemoth_ArmourTable = B.IdBehemoth WHERE B.Name LIKE '%{name}%' GROUP BY B.IdBehemoth"
            cursor.execute(sql) #this returns the amount of rows affected.
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

def fetchWeaponDB(name):
    connection = secrets.getConnection()
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT behemothtable.Name, behemothtable.Element, weapontable.Type, weapontable.Tier, weapontable.PhysAttack, weapontable.ElemAttack, weapontable.Ability, weapontable.Obs FROM behemothtable INNER JOIN weapontable ON weapontable.IdWeapon = behemothtable.IdWeapon_BehemothTable WHERE behemothtable.Name LIKE '%{name}%'"
            cursor.execute(sql) #this returns the amount of rows affected.
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

def fetchIconLinkDB(beheName, default):
    connection = secrets.getConnection()
    try:
        with connection.cursor() as cursor:
            sql = f"(SELECT imageLink FROM icontable WHERE behemothName = '{beheName}') UNION (SELECT imageLink FROM icontable WHERE behemothName = '{default}') LIMIT 1"
            cursor.execute(sql) #this returns the amount of rows affected.
            result = cursor.fetchall()
            return result[0]['imageLink']
    finally:
        connection.close()

def behemothEmbed(behemothArray):
    iconImage = fetchIconLinkDB(behemothArray[0]['BeheName'], "DefaultMonster")
    if (behemothArray[0]['BeheElement'] == "Fire"):
        embed = discord.Embed(title="Behemoth Information:", colour=discord.Colour(0xff0000), description=f"{behemothArray[0]['BeheName']}")
        embed.set_footer(text="SS Behemoth", icon_url="https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/a/a7/Def_elem_fire.png?version=49189da29988dfb12fd49afa9bfe14d5")
        embed.set_thumbnail(url=f"{iconImage}")

    if (behemothArray[0]['BeheElement'] == "Earth"):
        embed = discord.Embed(title="Behemoth Information:", colour=discord.Colour(0x03FA17), description=f"{behemothArray[0]['BeheName']}")
        embed.set_footer(text="SS Behemoth", icon_url="https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/0/05/Def_elem_soil.png?version=bdc0b25dd8263c2b695b46af1a83b59c")
        embed.set_thumbnail(url=f"{iconImage}")

    if (behemothArray[0]['BeheElement'] == "Lightning" or  behemothArray[0]['BeheElement'] == "Lightning or Earth"):
        embed = discord.Embed(title="Behemoth Information:", colour=discord.Colour(0xFAD603), description=f"{behemothArray[0]['BeheName']}")
        embed.set_footer(text="SS Behemoth", icon_url="https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/e/e3/Def_elem_thunder.png?version=a578454099ebd9d1c57556cd0eae6073")
        embed.set_thumbnail(url=f"{iconImage}")

    if (behemothArray[0]['BeheElement'] == "Water"):
        embed = discord.Embed(title="Behemoth Information:", colour=discord.Colour(0x00E0FF), description=f"{behemothArray[0]['BeheName']}")
        embed.set_footer(text="SS Behemoth", icon_url="https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/b/bd/Def_elem_water.png?version=712e4931b9f2cc7213304dd1c62c7ec2")
        embed.set_thumbnail(url=f"{iconImage}")

    if (behemothArray[0]['BeheElement'] == "Light (Holy)"):
        embed = discord.Embed(title="Behemoth Information:", colour=discord.Colour(0xFAFAB6), description=f"{behemothArray[0]['BeheName']}")
        embed.set_footer(text="SS Behemoth", icon_url="https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/3/3c/Def_elem_light.png?version=fbecc4bb28adadf24756c1c9c3723703")
        embed.set_thumbnail(url=f"{iconImage}")

    if (behemothArray[0]['BeheElement'] == "Dark"):
        embed = discord.Embed(title="Behemoth Information:", colour=discord.Colour(0x9013FE), description=f"{behemothArray[0]['BeheName']}")
        embed.set_footer(text="SS Behemoth", icon_url="https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/7/78/Def_elem_dark.png?version=3c1529b1fb3014e0bba43ed4488c5586")
        embed.set_thumbnail(url=f"{iconImage}")
    

    
    embed.add_field(name="Weapon Type:", value=f"{behemothArray[0]['WepTier']} {behemothArray[0]['WepType']}", inline=True)
    embed.add_field(name="Behemoth Element:", value=f"{behemothArray[0]['BeheElement']}", inline=True)
    embed.add_field(name="__Weapon Ability__:", value=f"{behemothArray[0]['WepAbility']}")
    embed.add_field(name="__Armour Ability__:", value=f"{behemothArray[0]['ArmourAbility']}")
    return embed


def weaponEmbed(behemothWeaponArray):

    iconImage = fetchIconLinkDB(behemothWeaponArray[0]['Name'], "DefaultWeapon")
    if (behemothWeaponArray[0]['Element'] == "Fire"):
        embed = discord.Embed(title="Weapon Information:", colour=discord.Colour(0xff0000), description=f"{behemothWeaponArray[0]['Name']}")
        embed.set_footer(text="SS Behemoth", icon_url="https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/a/a7/Def_elem_fire.png?version=49189da29988dfb12fd49afa9bfe14d5")
        embed.set_thumbnail(url=f"{iconImage}")

    if (behemothWeaponArray[0]['Element'] == "Earth"):
        embed = discord.Embed(title="Weapon Information:", colour=discord.Colour(0x03FA17), description=f"{behemothWeaponArray[0]['Name']}")
        embed.set_footer(text="SS Behemoth", icon_url="https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/0/05/Def_elem_soil.png?version=bdc0b25dd8263c2b695b46af1a83b59c")
        embed.set_thumbnail(url=f"{iconImage}")

    if (behemothWeaponArray[0]['Element'] == "Lightning"):
        embed = discord.Embed(title="Weapon Information:", colour=discord.Colour(0xFAD603), description=f"{behemothWeaponArray[0]['Name']}")
        embed.set_footer(text="SS Behemoth", icon_url="https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/e/e3/Def_elem_thunder.png?version=a578454099ebd9d1c57556cd0eae6073")
        embed.set_thumbnail(url=f"{iconImage}")

    if (behemothWeaponArray[0]['Element'] == "Water"):
        embed = discord.Embed(title="Weapon Information:", colour=discord.Colour(0x00E0FF), description=f"{behemothWeaponArray[0]['Name']}")
        embed.set_footer(text="SS Behemoth", icon_url="https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/b/bd/Def_elem_water.png?version=712e4931b9f2cc7213304dd1c62c7ec2")
        embed.set_thumbnail(url=f"{iconImage}")

    if (behemothWeaponArray[0]['Element'] == "Light (Holy)"):
        embed = discord.Embed(title="Weapon Information:", colour=discord.Colour(0xFAFAB6), description=f"{behemothWeaponArray[0]['Name']}")
        embed.set_footer(text="SS Behemoth", icon_url="https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/3/3c/Def_elem_light.png?version=fbecc4bb28adadf24756c1c9c3723703")
        embed.set_thumbnail(url=f"{iconImage}")

    if (behemothWeaponArray[0]['Element'] == "Dark"):
        embed = discord.Embed(title="Weapon Information:", colour=discord.Colour(0x9013FE), description=f"{behemothWeaponArray[0]['Name']}")
        embed.set_footer(text="SS Behemoth", icon_url="https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/7/78/Def_elem_dark.png?version=3c1529b1fb3014e0bba43ed4488c5586")
        embed.set_thumbnail(url=f"{iconImage}")

    embed.add_field(name="Weapon Type:", value=f"{behemothWeaponArray[0]['Tier']} {behemothWeaponArray[0]['Type']}", inline=True)
    embed.add_field(name="Behemoth Element:", value=f"{behemothWeaponArray[0]['Element']}", inline=True)
    embed.add_field(name="Physical Attack:", value=f"{behemothWeaponArray[0]['PhysAttack']}", inline=True)
    embed.add_field(name="Elemental Attack:", value=f"{behemothWeaponArray[0]['ElemAttack']}", inline=True)
    embed.add_field(name="__Weapon Ability__:", value=f"{behemothWeaponArray[0]['Ability']}")

    if (behemothWeaponArray[0]['Obs'] != ''):
        embed.add_field(name="__Observation__:", value=f"{behemothWeaponArray[0]['Obs']}")
    return embed