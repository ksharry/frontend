# 初始化資料庫
import pymongo
client = pymongo.MongoClient("mongodb+srv://root:root@mycluster.jnhlxhm.mongodb.net/?retryWrites=true&w=majority")
db = client.member_system
print("資料庫連線建立成功")

#初始化Flask

from flask import *
app=Flask(__name__,static_folder="public", static_url_path="/")
app.secret_key="harry"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/member")
def member():
    if "nickname" in session:
        return render_template("member.html")
    else:
        return redirect("/")

@app.route("/error")
def error():
    message=request.args.get("msg", "發生錯誤，請聯繫客服")
    return render_template("error.html", message=message)

@app.route("/signup", methods=["POST"])
def signup():
    nickname=request.form["nickname"]
    email=request.form["email"]
    password=request.form["password"]
    # 檢查MAIL
    collection=db.user
    result=collection.find_one({
        "email":email
    })
    if result != None:
        return redirect("/error?msg=信箱已經被註冊")
    
    # 寫入資料庫
    collection.insert_one({
        "nickname":nickname,
        "email":email,
        "password":password
    })
    return redirect("/")

@app.route("/signin", methods=["POST"])
def signin():
    email=request.form["email"]
    password=request.form["password"]
    collection=db.user
    result=collection.find_one({
        "$and":[
            {"email":email},
            {"password":password}
        ]
    })
    if result==None:
        return redirect("/error?msg=帳號或密碼輸入錯誤")
    
    #session紀錄會員資訊
    session["nickname"]=result["nickname"]

    return render_template("/member.html", data=session)

@app.route("/signout")
def signout():
    del session["nickname"]
    return redirect("/")

app.run(port=3000)