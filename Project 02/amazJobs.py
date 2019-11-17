import FetchD 
from flask import Flask, render_template, url_for,jsonify,request,redirect
from flask_pymongo import PyMongo
from splinter import Browser


app = Flask(__name__)


app.config["MONGO_URI"] = "mongodb://localhost:27017/amazJobs"
mongo = PyMongo(app)

@app.route("/scrape")
def scrape():
    openRoles = mongo.db.openRoles   #the name of the collection is openRole
    dictio = FetchD.primeFunc()      #Create the dictionary by calling the primary function
   
    openRoles.insert(dictio)   
    return redirect("/", code = 302)


@app.route("/")
def home():
    openRoles = mongo.db.openRoles.find_one()
    # ds = mongo.db.ds.find_one()
    return render_template("index2.html", jobs= openRoles)


@app.route('/roles', methods=['GET'])
def get_all_roles():
  openRoles = mongo.db.openRoles
  output = []
  for s in openRoles.find():
    output.append({'Category' : s['category'], 'title' : s['title'], 'Location' : s['Location'], 'city_Coordinates' : s['city_Coordinates'], 'Posting_Date' : s['Posting_date'] })
  return jsonify({'result' : output})

@app.route('/ds', methods=['GET'])
def get_ds():
  filterthree = mongo.db.filterthree
  output = []
  for s in filterthree.find():
    output.append({'Category' : s['category'], 'title' : s['title'], 'Location' : s['Location'], 'city_Coordinates' : s['city_Coordinates'], 'Posting_Date' : s['Posting_date'] })
  return jsonify({'result' : output})

@app.route('/leaflet')
def leaf():
  return render_template('index2.html')

if __name__=='__main__':
    app.run(debug=True)