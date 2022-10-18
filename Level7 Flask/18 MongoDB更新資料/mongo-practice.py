import pymongo
from bson.objectid import ObjectId

client = pymongo.MongoClient("mongodb+srv://root:root@mycluster.jnhlxhm.mongodb.net/?retryWrites=true&w=majority")
db = client.mywebsite
collection=db.users  # 新增資料庫

#更新一次,unset 把欄位刪除,inc是加的意思,mul是乘的意思
# result=collection.update_one({
#     "email":"ksharry1025@gmail.com"
# }, {
#     "$unset":{
#         "description":""
#     }
# })

#更新多次
result=collection.update_many({
    "level":3
}, {
    "$set":{
        "level":4
    }
})
print(result.matched_count)
print(result.modified_count)
