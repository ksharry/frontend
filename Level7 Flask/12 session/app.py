# get 普通信件  post 掛號信件(機密)

from flask import Flask, redirect, render_template, request, session
import json

app=Flask(__name__,static_folder="public", static_url_path="/")
app.secret_key="harry"


@app.route("/")
def index():
    return "Hello"

@app.route("/hello")
def hello():
    name=request.args.get("name", "")
    session["username"]=name
    return "你好"+name

@app.route("/talk")
def talk():
    name=session["username"]
    return "你好2"+name

app.run(port=3000)