from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
# import <<variable>>
import os

#authenticate
# app.config["<<variable>>"] = "<<variable link>>""

# mongo = Pymongo(app, url=<<variable link>>)

app = Flask(__name__)

app.config["MONGO_URL"] = os.environ.get('authentication')
mongo = PyMongo(app)

@app.route("/")
def home():

    amazon_info = mongo.db.amazon_info.find_one()
    return render_template("index.html", amazon_info=amazon_info)

    #run scrapped functions

    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug= True)

