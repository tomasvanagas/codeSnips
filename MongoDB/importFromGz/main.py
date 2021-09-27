import sys
import json
import pymongo

dbName = "DatabaseName"
colName = "CollectionName"


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient[dbName]
collection = mydb[colName]


count = 0
toImport = []
for line in sys.stdin:
    obj = json.loads(line)


    toImport.append(obj)

    count += 1
    if(count % 100000 == 0):
        result = collection.insert_many(toImport)
        print(str(count/100000))
        toImport = []

result = collection.insert_many(toImport)
print(str(count/10000))


myclient.close()
