from flask import Flask, jsonify
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from datetime import datetime
import datetime as dt
# from app import app

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

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)


# 3. Define what to do when a user hits the index route
@app.route("/index.html")
def index():
    return render_template("index.html")


@app.route("/about")
def home():
    print("Server received request for 'Home' page...")
    return (f"Available Routes:<br/> Convert the query results to a Dictionary using date as the key and prcp as the value. <br/>"
        f"/api/v1.0/NationalMarriageDivorce<br/> National Marriage and Divorce rate.<br/>"
        f"/api/v1.0/DivorceByState<br/> Divorce rate by state.<br/>"
        f"/api/v1.0/MarriageByState<br/> Marriage rate by state.<br/>")



# 4. Define what to do when a user hits the route
@app.route("/api/v1.0/NationalMarriageDivorce")
def NationalMarriageDivorce():
    
    # Query
    session = Session(engine)
    results = session.query(MarriageDivorce.Year,MarriageDivorce.MarriageRate,MarriageDivorce.DivorceRate).all()

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
    import json

    with open('Resources/USA.json') as f:
        data = json.load(f)

    return data
if __name__ == "__main__":
    app.run(debug=True)
