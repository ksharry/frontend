import pymongo
from bson.objectid import ObjectId

client = pymongo.MongoClient("mongodb+srv://root:root@mycluster.jnhlxhm.mongodb.net/?retryWrites=true&w=majority")
db = client.mywebsite
collection=db.users  # 新增資料庫

#刪除一次
# result=collection.delete_one({
#     "email":"ccc@gmail.com"
# })

#更新多次
result=collection.delete_many({
    "level":4
})
print(result.deleted_count)
