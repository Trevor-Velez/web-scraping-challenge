from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars")


@app.route("/")
def home():

    mars_data = mongo.db.mars.find_one()

    # Return template and data
    return render_template("index.html", data = mars_data)

@app.route("/scrape")
def scrape():

    # Run the scrape function
    mars_data = scrape_mars.complete_scrape()

    # Update the Mongo database using update and upsert=True
    mongo.db.mars.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

