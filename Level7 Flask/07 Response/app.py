from flask import Flask, redirect
from flask import request
import json

app=Flask(__name__,static_folder="public", static_url_path="/")

@app.route("/en/")
def index_englist():
    return json.dumps({
        "status":"ok",
        "test":"Hello"
    })

@app.route("/zh/")
def index_chinese():
    return json.dumps({
        "status":"ok",
        "test":"你好"
    }, ensure_ascii=False)

@app.route("/")
def index():
    lang=request.headers.get("accept-language")
    if lang.startswith("en"):
        return redirect("/en/")
    else:
        return redirect("/zh/") 

@app.route("/data")
def handleData():
    return "My Data"

app.run()