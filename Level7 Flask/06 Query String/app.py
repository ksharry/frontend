from flask import Flask
from flask import request

app=Flask(__name__,static_folder="public", static_url_path="/")

@app.route("/getSum")
def getsum():
    maxNumber=request.args.get("max", 100)
    maxNumber=int(maxNumber)
    minNumber=request.args.get("min", 1)
    minNumber=int(minNumber)
    result=0
    for n in range(minNumber,maxNumber+1):
        result+=n
    return "結果:"+str(result)

@app.route("/")
def index():
    lang=request.headers.get("accept-language")
    if lang.startswith("en"):
        return "Hello"
    else:
        return "你好"

@app.route("/data")
def handleData():
    return "My Data"

@app.route("/user/<username>")
def handleUser(username):
    return "Hello "+username

app.run()