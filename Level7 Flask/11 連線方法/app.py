# get 普通信件  post 掛號信件(機密)

from flask import Flask, redirect, render_template
from flask import request
import json

app=Flask(__name__,static_folder="public", static_url_path="/")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    maxNumber=request.form["max"]
    maxNumber=int(maxNumber)
    result=0
    for n in range(1, maxNumber+1):
        result+=n
    return render_template("result.html", data=result)

@app.route("/show")
def show():
    name=request.args.get("n","")
    return "歡迎光臨, "+name

@app.route("/page")
def page():
    return render_template("page.html")

app.run(port=3000)