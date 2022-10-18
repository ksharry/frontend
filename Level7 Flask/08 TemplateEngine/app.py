from flask import Flask, redirect, render_template
from flask import request
import json

app=Flask(__name__,static_folder="public", static_url_path="/")

@app.route("/")
def index():
    return render_template("index", name="小明")


app.run()