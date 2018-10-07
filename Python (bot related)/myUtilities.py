import pymysql.cursors
import pymysql
import discord
from discord.ext import commands
import re
import secrets


def getElementLink(stringInput):
    if (stringInput == "Fire"):
        return "https://media.discordapp.net/attachments/456208112790142977/472561214317395988/FireSmall.png" #old img, replace with the round icons

    if (stringInput == "Earth"):
        return "https://media.discordapp.net/attachments/456208112790142977/472561213281402880/EarthSmall.png" #old img, replace with the round icons

    if (stringInput == "Lightning"):
        return "https://media.discordapp.net/attachments/456208112790142977/472561215277629471/LightningSmall.png"#old img, replace with the round icons

    if (stringInput == "Water"):
        return "https://media.discordapp.net/attachments/456208112790142977/472561217764982804/WaterSmall.png"#old img, replace with the round icons

    if (stringInput == "Light (Holy)" or stringInput == "Light" or stringInput == "Holy"):
        return "https://media.discordapp.net/attachments/456208112790142977/472561216670138368/LightSmall.png"#old img, replace with the round icons

    if (stringInput == "Dark"):
        return "https://media.discordapp.net/attachments/456208112790142977/472561218855370775/DarkSmall.png"#old img, replace with the round icons

    if (stringInput == "Hybrid"):
        return "https://media.discordapp.net/attachments/456208112790142977/498370434912485406/IIC_90000001.png"

    if (stringInput == "Support"):
        return "https://media.discordapp.net/attachments/456208112790142977/498370436866899969/IIC_90000002.png"

    if (stringInput == "Heal"):
        return "https://media.discordapp.net/attachments/456208112790142977/498370439219904512/IIC_90000003.png"

    if (stringInput == "Passive"):
        return "https://media.discordapp.net/attachments/456208112790142977/498370434744582144/IIC_90000004.png"

    if (stringInput == "List"):
        return "https://media.discordapp.net/attachments/456208112790142977/471391949572800514/SS.png"

def getElementEmoji(stringInput):
    if (stringInput == "Fire"):
        return f"<:Fire:472523665292918796> - {stringInput}" 

    if (stringInput == "Earth"):
        return f"<:Earth:472523665280466959> - {stringInput}" 

    if (stringInput == "Lightning"):
        return f"<:Lightning:472523665586782239> - {stringInput}"

    if (stringInput == "Water"):
        return f"<:Water:472523665406165023> - {stringInput}"

    if (stringInput == "Light (Holy)" or stringInput == "Light" or stringInput == "Holy"):
        return f"<:LightHoly:472523665586651166> - {stringInput}"

    if (stringInput == "Dark"):
        return f"<:Dark:472523665616011266> - {stringInput}"

def getElementColor(stringInput):
    if (stringInput == "Fire"):
        return 0xff0000

    if (stringInput == "Earth"):
        return 0x03FA17

    if (stringInput == "Lightning"):
        return 0xFAD603

    if (stringInput == "Water"):
        return 0x00E0FF

    if (stringInput == "Light (Holy)" or stringInput == "Light" or stringInput == "Holy"):
        return 0xFAFAB6

    if (stringInput == "Dark"):
        return 0x9013FE

    if (stringInput == "Hybrid"):
        return 0x000000

    if (stringInput == "Support"):
        return 0x00ffff

    if (stringInput == "Heal"):
        return 0x00ff00

    if (stringInput == "Passive"):
        return 0xffe599
    
    if (stringInput == "List"):
        return 0x8e8e8e

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

def fetchArmorDB(name):
    connection = secrets.getConnection()
    
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT behemothtable.Name AS BeheName, behemothtable.Element AS BeheElement, armourtable.DefElement AS ArmorElement, armourtable.HpValue AS ArmorHP, armourtable.PhysDef AS ArmorPDef, armourtable.ElemDef AS ArmorEDef, armourtable.PhysAttack AS ArmorPAtk, armourtypelist.Name AS ArmorType, armourtable.Ability AS ArmorAbility, armourtable.Obs AS ArmorObs FROM behemothtable LEFT JOIN armourtable ON armourtable.IdBehemoth_ArmourTable = behemothtable.IdBehemoth LEFT JOIN armourtypelist ON armourtypelist.IdArmourTypeList = armourtable.IdArmourtype_ArmourTable WHERE behemothtable.Name LIKE '%{name}%'"
            cursor.execute(sql) #this returns the amount of rows affected.
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

def fetchMagiDB(name):
    connection = secrets.getConnection()
    
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT magitable.Name, magitable.Cooldown, magitable.HealAmount, magitable.Description, magitable.Obs, magitypelist.Name FROM magitable INNER JOIN magitypelist ON magitypelist.IdMagiType = magitable.IdMagiType_MagiTable WHERE magitable.Name LIKE '%{name}%'"
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
    elementLink = getElementLink(behemothArray[0]['BeheElement'])
    iconImage = fetchIconLinkDB(behemothArray[0]['BeheName'], "DefaultMonster")

    embed = discord.Embed(title="Behemoth Information:", colour=discord.Colour(getElementColor(behemothArray[0]['BeheElement'])), description=f"{behemothArray[0]['BeheName']}")
    embed.set_footer(text="SS Behemoth", icon_url=f"{elementLink}")
    embed.set_thumbnail(url=f"{iconImage}")
    
    embed.add_field(name="Weapon Type:", value=f"{behemothArray[0]['WepTier']} {behemothArray[0]['WepType']}", inline=True)
    embed.add_field(name="Behemoth Element:", value=f"{behemothArray[0]['BeheElement']}", inline=True)
    embed.add_field(name="__Weapon Ability__: (Perfect Roll)", value=f"{behemothArray[0]['WepAbility']}")
    embed.add_field(name="__Armour Ability__: (Perfect Roll)", value=f"{behemothArray[0]['ArmourAbility']}")

    return embed


def weaponEmbed(behemothWeaponArray):
    elementLink = getElementLink(behemothWeaponArray[0]['Element'])
    iconImage = fetchIconLinkDB(behemothWeaponArray[0]['Name'], "DefaultWeapon")

    embed = discord.Embed(title="Weapon Information:", colour=discord.Colour(getElementColor(behemothWeaponArray[0]['Element'])), description=f"{behemothWeaponArray[0]['Name']}")
    embed.set_footer(text="SS Behemoth", icon_url=f"{elementLink}")
    embed.set_thumbnail(url=f"{iconImage}")

    embed.add_field(name="Weapon Type:", value=f"{behemothWeaponArray[0]['Tier']} {behemothWeaponArray[0]['Type']}", inline=True)
    embed.add_field(name="Behemoth Element:", value=f"{behemothWeaponArray[0]['Element']}", inline=True)
    embed.add_field(name="Physical Attack:", value=f"{behemothWeaponArray[0]['PhysAttack']}", inline=True)
    embed.add_field(name="Elemental Attack:", value=f"{behemothWeaponArray[0]['ElemAttack']}", inline=True)
    embed.add_field(name="__Weapon Ability__: (Perfect Roll)", value=f"{behemothWeaponArray[0]['Ability']}")

    if (behemothWeaponArray[0]['Obs'] != ''):
        embed.add_field(name="__Observation__:", value=f"{behemothWeaponArray[0]['Obs']}")

    return embed

def armorEmbed(behemothArmorArray):
    iconImage = fetchIconLinkDB(behemothArmorArray[0]['BeheName'], "DefaultArmor")
    emojiString = getElementEmoji(behemothArmorArray[0]['ArmorElement'])
    elementLink = getElementLink(behemothArmorArray[0]['BeheElement'])

    embed = discord.Embed(title="Armor Information:", colour=discord.Colour(getElementColor(behemothArmorArray[0]['BeheElement'])), description=f"{behemothArmorArray[0]['BeheName']}") 
    embed.add_field(name="Elemental Defense:", value=f"{emojiString}", inline=True) 
    
    for row in behemothArmorArray:
        embed.add_field(name=f"{row['ArmorType']}:", value=f"HP: {row['ArmorHP']}  **|**  P.Defense: {row['ArmorPDef']}  **|**  E.Defense: {row['ArmorEDef']}  **|**  P.Attack: {row['ArmorPAtk']}")

    embed.add_field(name="__Armour Ability__: (Perfect Roll)", value=f"{behemothArmorArray[0]['ArmorAbility']}")

    if (behemothArmorArray[0]['ArmorObs'] != ''):
        embed.add_field(name="__Observation__:", value=f"{behemothArmorArray[0]['ArmorObs']}")
        
    embed.set_footer(text="SS Behemoth", icon_url=f"{elementLink}")
    embed.set_thumbnail(url=f"{iconImage}")

    return embed

def magiEmbedGenerator(magiArray, inputString):
    if (len(magiArray) == 1):
        embed = singleMagiEmbed(magiArray)
        return embed
    else:
        embed = magiListEmbed(magiArray, inputString)
    return embed

    

def singleMagiEmbed(magiArray):
    iconImage = fetchIconLinkDB(magiArray[0]['Name'], "DefaultMagi")
    elementLink = getElementLink(magiArray[0]['magitypelist.Name'])

    embed = discord.Embed(colour=discord.Colour(getElementColor(magiArray[0]['magitypelist.Name'])))
    embed.add_field(name="Magi Information:", value=f"{magiArray[0]['Name']}", inline=True)

    if (magiArray[0]['magitypelist.Name'] != 'Passive'):
        embed.add_field(name="Cooldown:", value=f"{magiArray[0]['Cooldown']}", inline=True)
    if (magiArray[0]['magitypelist.Name'] == 'Heal'):
        embed.add_field(name="Heal Amount:", value=f"{magiArray[0]['HealAmount']}", inline=True)

    embed.add_field(name="Description", value=f"{magiArray[0]['Description']}")

    if (magiArray[0]['Obs'] != ''):
        embed.add_field(name="__Observation__:", value=f"{magiArray[0]['Obs']}")

    embed.add_field(name="Magi Type:", value=f"{magiArray[0]['magitypelist.Name']}", inline=True)
        
    embed.set_footer(text="SS Magi", icon_url=f"{elementLink}") 
    embed.set_thumbnail(url=f"{iconImage}")                     

    return embed

def magiListEmbed(magiArray, userSearch):
    iconImage = fetchIconLinkDB("", "DefaultMagi")
    elementLink = getElementLink('List')

    embed = discord.Embed(colour=discord.Colour(getElementColor('List')))
    embed.add_field(name="Information:", value="The following magi match your request, input a complete name for specific information:", )

    for idx, line in enumerate(magiArray, start=1):
        embed.add_field(name=f"{idx}º Magi - Name: ", value=f"   \"{line['Name']}\" - **Type**: {line['magitypelist.Name']} magi")
        
    embed.set_footer(text=f"You searched for: {userSearch}", icon_url=f"{elementLink}")
    embed.set_thumbnail(url=f"{iconImage}")                    

    return embed