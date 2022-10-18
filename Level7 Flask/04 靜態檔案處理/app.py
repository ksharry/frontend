from flask import Flask
app=Flask(
    __name__,
    static_folder="static",  #資料夾名稱
    static_url_path="/static"  #網址路徑
)


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