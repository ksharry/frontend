import pymongo

client = pymongo.MongoClient("mongodb+srv://root:root@mycluster.jnhlxhm.mongodb.net/?retryWrites=true&w=majority")
db = client.website
collection=db.members  # 新增資料庫
collection.insert_one({  #新增表單
    "email":"ksharry1025@gmail.com",
    "password":"test"
})
print("資料新增成功")