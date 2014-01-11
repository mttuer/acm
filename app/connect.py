import mysql.connector
import json
from pprint import pprint

json_data=open('app/config.json')

data = json.load(json_data)
json_data.close()

def getDB():
    global db 
    global cur
    db = mysql.connector.connect(host="localhost", # your host, usually localhost
        user=data["SqlData"]["usr"],
        password=data["SqlData"]["pwd"],
        database=data["SqlData"]["dbName"])

# you must create a Cursor object. It will let
#  you execute all the query you need
    cur = db.cursor() 
    return cur

def showTables(cur):
# Use all the SQL you like
    cur.execute("SHOW TABLES")

# print all the first cell of all the rows
    for row in cur.fetchall() :
        print row[0]

def getColNames(tbName):
    cur.execute("DESCRIBE " + tbName)
    names=list()
    for name in cur.fetchall():
        names.append(name[0])
    return names

def commit():
    db.commit()

def close():
    db.close()

