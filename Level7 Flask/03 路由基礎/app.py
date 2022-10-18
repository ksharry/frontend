from flask import Flask
app=Flask(__name__)

@app.route("/")
def index():
    return "Hello Flask"

@app.route("/data")
def handleData():
    return "My Data"

@app.route("/user/<username>")
def handleUser(username):
    return "Hello "+username

app.run()