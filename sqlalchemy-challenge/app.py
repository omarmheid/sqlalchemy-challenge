from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import session
from sqlalchemy import create_engine, func, inspect 

engine = create_engine("sqlite://Resources/hawaii.sqlite")

Base = automap_base()
#reflect the tables 
Base.prepare(engine, reflect = True)
Base.classes.keys()
Measurement = Base.classes.Measurement
Station = Base.classes.Station

app = Flask(__name__)
session = session(engine)

#List all routes that are available 
#@app.route("/")

#Convert the query results to a Dictionary using date as the key perception as the value 
#Return the JSON representation of your Dictionary 

@app.route("/api/v1.0/precipitation")
def precipitation():
    return jsonify(session.query(Measurement.date, Measurement.prcp).\
    filter(func.strftime(Measurement.date) >= "2016-08-23").\
    order_by(Measurement.date).all())

#Return a JSON list of stations from the dataset.

@app.route("/api/v1.0/stations")
def stations():
    return jsonify(session.query(Station.station).all())

#Query for the dates and temprature observations from a year from the last data point.
#Return a JSON list of Temperature Observations (tobs) for the previous year 

@app.route("/api/v1.0/tobs")
def tobs():
    return jsonify(session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date >= "2016-08-23").all())

