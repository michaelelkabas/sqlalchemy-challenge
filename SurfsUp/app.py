# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
from sqlalchemy import func
from flask import Flask, jsonify

# SQLAlchemy setup
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

#################################################
# Database Setup
#################################################

# Create engine
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect an existing database into a new model
Base = automap_base()

# Reflect the tables
Base.prepare(engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create session
session = Session(engine)

#################################################
# Flask Setup
#################################################

# Flask setup
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    return (
        f"Welcome to the Climate App!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start_date<br/>"
        f"/api/v1.0/start_date/end_date"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Query precipitation data
    results = session.query(Measurement.date, Measurement.prcp).all()

    # Convert query results to a list of dictionaries
    precipitation_list = []
    for date, prcp in results:
        precipitation_dict = {}
        precipitation_dict["date"] = date
        precipitation_dict["prcp"] = prcp
        precipitation_list.append(precipitation_dict)

    # Return JSON response
    return jsonify(precipitation_list)


@app.route("/api/v1.0/stations")
def stations():
    # Query station data
    results = session.query(Station.station, Station.name).all()

    # Convert query results to a list of dictionaries
    station_list = []
    for station in results:
        station_dict = {}
        station_dict["station"] = station.station
        station_dict["name"] = station.name
        station_list.append(station_dict)

    # Return JSON response
    return jsonify(station_list)


@app.route("/api/v1.0/tobs")
def tobs():
    # Query temperature observations data
    results = session.query(Measurement.date, Measurement.tobs).all()

    # Convert query results to a list of dictionaries
    tobs_list = []
    for date, tobs in results:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["tobs"] = tobs
        tobs_list.append(tobs_dict)

    # Return JSON response
    return jsonify(tobs_list)

from sqlalchemy import func

@app.route("/api/v1.0/<start_date>")
def start_date(start_date):
    # Query temperature data from the specified start date
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
              filter(Measurement.date >= start_date).all()

    # Convert query results to a dictionary
    temperature_data = {
        "Minimum Temperature": results[0][0],
        "Average Temperature": results[0][1],
        "Maximum Temperature": results[0][2]
    }

    # Return JSON response
    return jsonify(temperature_data)


@app.route("/api/v1.0/<start_date>/<end_date>")
def start_end_date(start_date, end_date):
    # Query temperature data within the specified date range
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
              filter(Measurement.date >= start_date).\
              filter(Measurement.date <= end_date).all()

    # Convert query results to a dictionary
    temperature_data = {
        "Minimum Temperature": results[0][0],
        "Average Temperature": results[0][1],
        "Maximum Temperature": results[0][2]
    }

    # Return JSON response
    return jsonify(temperature_data)

if __name__ == "__main__":
    app.run(debug=True)

