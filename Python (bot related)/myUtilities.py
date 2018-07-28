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

def getElementLink(stringInput):
    if (stringInput == "Fire"):
        return "https://media.discordapp.net/attachments/456208112790142977/472561214317395988/FireSmall.png" 

    if (stringInput == "Earth"):
        return "https://media.discordapp.net/attachments/456208112790142977/472561213281402880/EarthSmall.png" 

    if (stringInput == "Lightning"):
        return "https://media.discordapp.net/attachments/456208112790142977/472561215277629471/LightningSmall.png"

    if (stringInput == "Water"):
        return "https://media.discordapp.net/attachments/456208112790142977/472561217764982804/WaterSmall.png"

    if (stringInput == "Light (Holy)" or stringInput == "Light" or stringInput == "Holy"):
        return "https://media.discordapp.net/attachments/456208112790142977/472561216670138368/LightSmall.png"

    if (stringInput == "Dark"):
        return "https://media.discordapp.net/attachments/456208112790142977/472561218855370775/DarkSmall.png"

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
            sql = f"SELECT magitable.Name, magitable.Cooldown, magitable.Cooldown, magitable.HealAmount, magitable.Description, magitable.Obs, magitypelist.Name FROM magitable INNER JOIN magitypelist ON magitypelist.IdMagiType = magitable.IdMagiType_MagiTable WHERE magitable.Name LIKE '%{name}%'"
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

    embed = discord.Embed(colour=discord.Colour(getElementColor(behemothArmorArray[0]['BeheElement'])))
    embed.add_field(name="Armor Information:", value=f"{behemothArmorArray[0]['BeheName']}", inline=True) 
    embed.add_field(name="Elemental Defense:", value=f"{emojiString}", inline=True) 
    
    for row in behemothArmorArray:
        embed.add_field(name=f"{row['ArmorType']}:", value=f"HP: {row['ArmorHP']}  **|**  P.Defense: {row['ArmorPDef']}  **|**  E.Defense: {row['ArmorEDef']}  **|**  P.Attack: {row['ArmorPAtk']}")

    embed.add_field(name="__Armour Ability__: (Perfect Roll)", value=f"{behemothArmorArray[0]['ArmorAbility']}")

    if (behemothArmorArray[0]['ArmorObs'] != ''):
        embed.add_field(name="__Observation__:", value=f"{behemothArmorArray[0]['ArmorObs']}")
        
    embed.set_footer(text="SS Behemoth", icon_url=f"{elementLink}")
    embed.set_thumbnail(url=f"{iconImage}")

    return embed


def singleMagiEmbed(magiArray):
    iconImage = fetchIconLinkDB(behemothArmorArray[0]['BeheName'], "DefaultMagi")
    emojiString = getElementEmoji(behemothArmorArray[0]['ArmorElement'])
    elementLink = getElementLink(behemothArmorArray[0]['BeheElement'])

    embed = discord.Embed(colour=discord.Colour(getElementColor(behemothArmorArray[0]['BeheElement'])))
    embed.add_field(name="Armor Information:", value=f"{behemothArmorArray[0]['BeheName']}", inline=True) 
    embed.add_field(name="Elemental Defense:", value=f"{emojiString} - {behemothArmorArray[0]['ArmorElement']}", inline=True) 
    
    for row in behemothArmorArray:
        embed.add_field(name=f"{row['ArmorType']}:", value=f"HP: {row['ArmorHP']}  **|**  P.Defense: {row['ArmorPDef']}  **|**  E.Defense: {row['ArmorEDef']}  **|**  P.Attack: {row['ArmorPAtk']}")

    embed.add_field(name="__Armour Ability__: (Perfect Roll)", value=f"{behemothArmorArray[0]['ArmorAbility']}")

    if (behemothArmorArray[0]['ArmorObs'] != ''):
        embed.add_field(name="__Observation__:", value=f"{behemothArmorArray[0]['ArmorObs']}")
        
    embed.set_footer(text="SS Behemoth", icon_url=f"{elementLink}")
    embed.set_thumbnail(url=f"{iconImage}")

    return embed

def magiListEmbed(magiArray):
    iconImage = fetchIconLinkDB(behemothArmorArray[0]['BeheName'], "DefaultMagi")
    emojiString = getElementEmoji(behemothArmorArray[0]['ArmorElement'])
    elementLink = getElementLink(behemothArmorArray[0]['BeheElement'])

    embed = discord.Embed(colour=discord.Colour(getElementColor(behemothArmorArray[0]['BeheElement'])))
    embed.add_field(name="Armor Information:", value=f"{behemothArmorArray[0]['BeheName']}", inline=True) 
    embed.add_field(name="Elemental Defense:", value=f"{emojiString} - {behemothArmorArray[0]['ArmorElement']}", inline=True) 
    
    for row in behemothArmorArray:
        embed.add_field(name=f"{row['ArmorType']}:", value=f"HP: {row['ArmorHP']}  **|**  P.Defense: {row['ArmorPDef']}  **|**  E.Defense: {row['ArmorEDef']}  **|**  P.Attack: {row['ArmorPAtk']}")

    embed.add_field(name="__Armour Ability__: (Perfect Roll)", value=f"{behemothArmorArray[0]['ArmorAbility']}")

    if (behemothArmorArray[0]['ArmorObs'] != ''):
        embed.add_field(name="__Observation__:", value=f"{behemothArmorArray[0]['ArmorObs']}")
        
    embed.set_footer(text="SS Behemoth", icon_url=f"{elementLink}")
    embed.set_thumbnail(url=f"{iconImage}")

    return embed