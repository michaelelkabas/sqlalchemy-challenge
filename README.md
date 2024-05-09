In this assignment the use Python and SQLAlchemy to do a basic climate analysis and data exploration of your climate database. 
Specifically, you’ll use SQLAlchemy ORM queries, Pandas, and Matplotlib. 
The provided files (climate_starter.ipynb and hawaii.sqlite) are used to complete your climate analysis and data exploration located 
inside this local Git repository, create a directory for this Challenge. The folder name that corresponds to the Challenge is SurfsUp.
Jupyter notebook and app.py is in this folder. they contain the main scripts to run for analysis. 
Also the Resources folder contains the data files needed for this challenge.

App.py supports the following APIs: 
/api/v1.0/precipitation - Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value
/api/v1.0/stations - Return a JSON list of stations from the dataset
/api/v1.0/tobs - Query the dates and temperature observations of the most-active station for the previous year of data. Return a JSON list of temperature observations for the previous year.
/api/v1.0/start_date - /api/v1.0/<start> (YYYY-MM-DD) and /api/v1.0/<start>/<end> (YYYY-MM-DD). Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
/api/v1.0/start_date/end_date - Range of dates per above
