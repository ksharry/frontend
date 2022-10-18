import pymongo
from bson.objectid import ObjectId

client = pymongo.MongoClient("mongodb+srv://root:root@mycluster.jnhlxhm.mongodb.net/?retryWrites=true&w=majority")
db = client.mywebsite
collection=db.users  # 新增資料庫

#篩選
# result=collection.find_one({
#     "$and":[
#     {"email":"ksharry1025@gmail.com"},
#     {"password":"test222"},
#     ]
# })
# print(result)
#篩選結果
cur = collection.find({
        "$or":[
            {"email":"ksharry1025@gmail.com"},
            {"password":"test"},
        ]
    }, sort=[
        ("level", pymongo.DESCENDING)
    ])

for doc in cur:
    print(doc)


