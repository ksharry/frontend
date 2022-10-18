import pymongo
from bson.objectid import ObjectId

client = pymongo.MongoClient("mongodb+srv://root:root@mycluster.jnhlxhm.mongodb.net/?retryWrites=true&w=majority")
db = client.mywebsite
collection=db.users  # 新增資料庫

#一次取單筆
# data=collection.find_one(ObjectId("634e53770ad798e53e8a5ff3"))
# print(data)
# print(data["email"])

#一次取多筆
cursor=collection.find()
print(cursor)
for doc in cursor:
    print(doc)