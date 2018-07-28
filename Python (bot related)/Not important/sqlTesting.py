import pymysql.cursors
import pymysql

# Connect to the database
name = "gory"
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='karyu_db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    ##with connection.cursor() as cursor:
        # Create a new record
    ##    sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
    ##    cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    ##connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = f"SELECT B.Name AS BeheName, B.Element as BeheElement, W.Type AS WepType, W.Tier AS WepTier, W.Ability AS WepAbility, A.Ability AS ArmourAbility FROM behemothtable AS B INNER JOIN weapontable AS W ON W.IdWeapon = B.IdWeapon_BehemothTable INNER JOIN armourtable AS A ON A.IdBehemoth_ArmourTable = B.IdBehemoth WHERE B.Name LIKE '%{name}%' GROUP BY B.IdBehemoth"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()
