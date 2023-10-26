# Import the dependencies.
from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session


#################################################
# Database Setup
#################################################

# reflect an existing database into a new model
app = Flask(__name__)
engine = create_engine("sqlite:///your_database_file_name_here.sqlite")

# reflect the tables
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station


# Create our session (link) from Python to the DB
session = Session(engine)


#################################################
# Flask Setup
#################################################

app = Flask(__name)


#################################################
# Flask Routes
#################################################


@app.route("/")
def home():
    """Homepage that lists all available routes."""
    return (
        f"Welcome to the Climate App API!<br/><br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation - Precipitation data for the last 12 months<br/>"
        f"/api/v1.0/stations - List of stations<br/>"
        f"/api/v1.0/tobs - Temperature observations for the most active station (last year)<br/>"
        f"/api/v1.0/&lt;start&gt; - Min, Avg, and Max temperatures from the specified start date (YYYY-MM-DD)<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt; - Min, Avg, and Max temperatures between start and end dates (YYYY-MM-DD/YYYY-MM-DD)"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return the JSON representation of your dictionary"""
@app.route("/api/v1.0/stations")
def stations():
     """Return a JSON list of stations from the dataset"""
@app.route("/api/v1.0/tobs")
def tobs():
     """Return a JSON list of temperature observations for the previous year"""

@app.route("/api/v1.0/<start>")
def temperature_start(start):
     """Returns the min, max, and average temperatures calculated from the given start date to the end of the dataset"""

@app.route("/api/v1.0/<start>/<end>")
def temperature_range(start, end):
     """Returns the min, max, and average temperatures calculated from the given start date to the given end date """



if __name__ == "__main__":
    app.run(debug=True)