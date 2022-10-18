import pymongo

client = pymongo.MongoClient("mongodb+srv://root:root@mycluster.jnhlxhm.mongodb.net/?retryWrites=true&w=majority")
db = client.test
collection=db.users  # 新增資料庫
collection.insert_one({  #新增表單
    "name":"Harry2",
    "gender":"男"
})
print("資料新增成功")