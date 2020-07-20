from flask import Flask 
from flask import render_template
from flask_pymongo import PyMongo 
import scraping
import final_scrape

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars, challenge=challenge)

@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scraping.scrape_all()
    mars.update({}, mars_data, upsert = True)
    return "Scraping Successful!"

@app.route("/Hemispheres")
def hemi():
    challenge = mongo.db.challenge
    challenge_data = final_scrape.scrape_all()
    challenge.update({},challenge_data, upsert = True)
    return "challenge scrape successful!"




if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port = 5000)

    