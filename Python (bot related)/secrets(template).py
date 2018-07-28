import pymysql.cursors
import pymysql
import re

def getConnection():
    connection = pymysql.connect(host='localhost',
                                user='username',
                                password='password',
                                db='database',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
    return connection

def getToken():
    token = "YOUR-TOKEN-HERE"
    return token