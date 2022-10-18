import pymongo

client = pymongo.MongoClient("mongodb+srv://root:root@mycluster.jnhlxhm.mongodb.net/?retryWrites=true&w=majority")
db = client.mywebsite
collection=db.users  # 新增資料庫
result=collection.insert_many([{ 
    "name":"Mary",
    "email":"bbb@gmail.com",
    "password":"test",
    "level":3,
}, { 
    "name":"Sam",
    "email":"ccc@gmail.com",
    "password":"test",
    "level":3,
}])
print("資料新增成功")
print(result.inserted_ids)