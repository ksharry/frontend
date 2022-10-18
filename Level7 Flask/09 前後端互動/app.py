from flask import Flask, redirect, render_template
from flask import request
import json

app=Flask(__name__,static_folder="public", static_url_path="/")

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/page")
def page():
    return render_template("page.html")

app.run(port=3000)