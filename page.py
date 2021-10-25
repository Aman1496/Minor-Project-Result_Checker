from pymongo import MongoClient
client = MongoClient("mongodb+srv://manasvi:man14@rc.jxjlg.mongodb.net/test")
db = client["dbname"]
try:
 db.command("serverStatus")
except Exception as e: print(e)
else: print("You are connected!")
client.close()

