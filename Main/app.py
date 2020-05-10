from flask import Flask, jsonify
import numpy as np
import json
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
from flask import render_template

engine = create_engine("sqlite:///Resources/data/marriage_data.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# Save references to each table
MarriageDivorce = Base.classes.national
DivorceByState = Base.classes.DivorceByState
MarriageByState = Base.classes.MarriageByState

app = Flask(__name__)

# Define what to do when a user a specific route
@app.route("/")
def index1():
    return render_template("about.html")

@app.route("/dashboardbystate.html")
def index2():
    return render_template("dashboardbystate.html")

@app.route("/about.html")
def home():
    # print("Server received request for 'Home' page...")
     return render_template("about.html")

@app.route('/dashboardbyeducation.html')
def scrape538():
### Setting up the browser
    executable_path={'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
### 538 marriage isn't dead website
    url = 'https://fivethirtyeight.com/features/marriage-isnt-dead-yet/'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
### get all 'p' tag
    results = soup.find_all('p')
### find images
    image1 = soup.find('img', class_='wp-image-54890')['src']
    image2 = soup.find('img', class_='wp-image-54889')['src']
    image3 = soup.find('img', class_='wp-image-54887')['src']
### convert to dict
    result = {
        'paragraph1': results[0].text.strip(),
        'paragraph2': results[1].text.strip(),
        'paragraph3': results[7].text.strip(),
        'image1': image1,
        'paragraph4': results[11].text.strip(),
        'paragraph5': results[12].text.strip(),
        'paragraph6': results[13].text.strip(),
        'paragraph7': results[17].text.strip(),
        'paragraph8': results[18].text.strip(),
        'paragraph9': results[20].text.strip(),
        'image2': image2,
        'paragraph10': results[24].text.strip(),
        'paragraph11': results[28].text.strip(),
        'paragraph12': results[35].text.strip(),
        'image3': image3,
        'paragraph13': results[37].text.strip(),
        'paragraph14': results[40].text.strip()
    }

    return render_template('dashboardbyeducation.html', data538=result)

@app.route("/api/v1.0/NationalMarriageDivorce")
def NationalMarriageDivorce():  
    # Query
    session = Session(engine)
    results = session.query(MarriageDivorce.Year,MarriageDivorce.MarriageRate,MarriageDivorce.DivorceRate).all()
    # create dict list
    national = []
    for Year,MarriageRate,DivorceRate in results:
        nat_dict = {}
        nat_dict["Year"] = Year
        nat_dict["Marriage_Rate"] = MarriageRate
        nat_dict["Divorce_Rate"] = DivorceRate
        national.append(nat_dict)
    return jsonify(national)

@app.route("/api/v1.0/MarriageByState")
def MState():
    # Query
    session = Session(engine)
    results = session.query(MarriageByState.state,MarriageByState.avg,MarriageByState.Year_2018,MarriageByState.Year_2017,MarriageByState.Year_2016,MarriageByState.Year_2015,MarriageByState.Year_2014,MarriageByState.Year_2013,MarriageByState.Year_2012,MarriageByState.Year_2011,MarriageByState.Year_2010,MarriageByState.Year_2009,MarriageByState.Year_2008,MarriageByState.Year_2007,MarriageByState.Year_2006,MarriageByState.Year_2005,MarriageByState.Year_2004,MarriageByState.Year_2003,MarriageByState.Year_2002,MarriageByState.Year_2001,MarriageByState.Year_2000,MarriageByState.Year_1999,MarriageByState.Year_1995,MarriageByState.Year_1990).all()
    # create dict list
    MarriageState = []
    for state,avg,Year_2018,Year_2017,Year_2016,Year_2015,Year_2014,Year_2013,Year_2012,Year_2011,Year_2010,Year_2009,Year_2008,Year_2007,Year_2006,Year_2005,Year_2004,Year_2003,Year_2002,Year_2001,Year_2000,Year_1999,Year_1995,Year_1990 in results:
        MS_dict = {}
        MS_dict["state"] = state
        MS_dict["avg"] = avg
        MS_dict["Year_2018"] = Year_2018
        MS_dict["Year_2017"] = Year_2017
        MS_dict["Year_2016"] = Year_2016
        MS_dict["Year_2015"] = Year_2015
        MS_dict["Year_2014"] = Year_2014
        MS_dict["Year_2013"] = Year_2013
        MS_dict["Year_2012"] = Year_2012
        MS_dict["Year_2011"] = Year_2011
        MS_dict["Year_2010"] = Year_2010
        MS_dict["Year_2009"] = Year_2009
        MS_dict["Year_2008"] = Year_2008
        MS_dict["Year_2007"] = Year_2007
        MS_dict["Year_2006"] = Year_2006
        MS_dict["Year_2005"] = Year_2005
        MS_dict["Year_2004"] = Year_2004
        MS_dict["Year_2003"] = Year_2003
        MS_dict["Year_2002"] = Year_2002
        MS_dict["Year_2001"] = Year_2001
        MS_dict["Year_2000"] = Year_2000
        MS_dict["Year_1999"] = Year_1999
        MS_dict["Year_1995"] = Year_1995
        MS_dict["Year_1990"] = Year_1990
        MarriageState.append(MS_dict)
    return jsonify(MarriageState)

@app.route("/api/v1.0/DivorceByState")
def DState():
    # Query
    session = Session(engine)
    results = session.query(DivorceByState.state,DivorceByState.avg,DivorceByState.Year_2018,DivorceByState.Year_2017,DivorceByState.Year_2016,DivorceByState.Year_2015,DivorceByState.Year_2014,DivorceByState.Year_2013,DivorceByState.Year_2012,DivorceByState.Year_2011,DivorceByState.Year_2010,DivorceByState.Year_2009,DivorceByState.Year_2008,DivorceByState.Year_2007,DivorceByState.Year_2006,DivorceByState.Year_2005,DivorceByState.Year_2004,DivorceByState.Year_2003,DivorceByState.Year_2002,DivorceByState.Year_2001,DivorceByState.Year_2000,DivorceByState.Year_1999,DivorceByState.Year_1995,DivorceByState.Year_1990).all()
    # create dict list
    DivorceState = []
    for state,avg,Year_2018,Year_2017,Year_2016,Year_2015,Year_2014,Year_2013,Year_2012,Year_2011,Year_2010,Year_2009,Year_2008,Year_2007,Year_2006,Year_2005,Year_2004,Year_2003,Year_2002,Year_2001,Year_2000,Year_1999,Year_1995,Year_1990 in results:
        DS_dict = {}
        DS_dict["state"] = state
        DS_dict["avg"] = avg
        DS_dict["Year_2018"] = Year_2018
        DS_dict["Year_2017"] = Year_2017
        DS_dict["Year_2016"] = Year_2016
        DS_dict["Year_2015"] = Year_2015
        DS_dict["Year_2014"] = Year_2014
        DS_dict["Year_2013"] = Year_2013
        DS_dict["Year_2012"] = Year_2012
        DS_dict["Year_2011"] = Year_2011
        DS_dict["Year_2010"] = Year_2010
        DS_dict["Year_2009"] = Year_2009
        DS_dict["Year_2008"] = Year_2008
        DS_dict["Year_2007"] = Year_2007
        DS_dict["Year_2006"] = Year_2006
        DS_dict["Year_2005"] = Year_2005
        DS_dict["Year_2004"] = Year_2004
        DS_dict["Year_2003"] = Year_2003
        DS_dict["Year_2002"] = Year_2002
        DS_dict["Year_2001"] = Year_2001
        DS_dict["Year_2000"] = Year_2000
        DS_dict["Year_1999"] = Year_1999
        DS_dict["Year_1995"] = Year_1995
        DS_dict["Year_1990"] = Year_1990
        DivorceState.append(DS_dict)
    return jsonify(DivorceState)

@app.route("/api/v1.0/USA")
def USA():
    with open('Resources/data/USA.json') as f:
        data = json.load(f)
    return data

# run app
if __name__ == "__main__":
    app.run(debug=True)
