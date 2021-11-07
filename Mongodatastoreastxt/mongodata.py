import pymongo
import json
import csv 
client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
 

db = client["data"]
 

col = db["sensor"]
 
x = col.find()
 
for data in x:
    print(data)
with open('/home/user/data.txt', 'w') as f:
        f.writelines(data)
    


