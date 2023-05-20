import pandas as pd
import numpy as np
import db_tools
import math
from sodapy import Socrata
from geopy.geocoders import Nominatim
n1 = 0

client = Socrata("data.cityofnewyork.us", "qE4zlRbUa5QqMb2dbqEMQiCse")

geolocator = Nominatim(user_agent="higher_lower_nyc")



def get_borough(zip_code):
    location = geolocator.geocode({"postalcode": zip_code, "country": "USA"}, addressdetails=True)
    global n1
    print(n1)
    n1 += 1
    if location is None:
        print("None")
        return "Unknown"
    if "suburb" in location.raw["address"]:
        borough = location.raw["address"]["suburb"]
        print(location.raw["address"]["suburb"])
        return borough
    else:
        print(location.raw["address"])
        return "Unknown"


sumMode = True
richmond = True
connection_id = "nu7n-tubp" 
query = "animalname='SAM'"
limit = 100000

# Fetch the data based on the query
results = client.get(connection_id, where=query, limit=limit)
#results = client.get(connection_id, limit=100000, breedname="Afghan Hound")
results_df = pd.DataFrame.from_records(results)
print(results_df.head(5))
results_df['borough'] = results_df['zipcode'].apply(get_borough)
print(results_df.head(5))
borough_label = "borough"
if(sumMode):
# Convert to pandas DataFrame
    id_label = "animalname"
    data_by_borough = results_df.groupby('borough').size().reset_index(name='n')
    print(data_by_borough)
    #print(permits_by_borough)

else:
    data_label = "base_salary"
    results_df[data_label] = results_df['data_label'].astype(float)

    data_by_borough = results_df.groupby(borough_label)[data_label].mean()

    print(data_by_borough)
    # write a list combining the means of the three types of income by borough. Note that there are additional datapoints to the five boroughs of NYC
Brooklyn = str(data_by_borough.loc[data_by_borough['borough'] == 'Kings County', 'n'].values[0])
Manhattan = str(data_by_borough.loc[data_by_borough['borough'] == 'Manhattan', 'n'].values[0])
Queens = str(data_by_borough.loc[data_by_borough['borough'] == 'Queens County', 'n'].values[0])
Bronx = str(data_by_borough.loc[data_by_borough['borough'] == 'The Bronx', 'n'].values[0])
if(richmond):
    StatenIsland = str(data_by_borough.loc[data_by_borough['borough'] == 'Richmond County', 'n'].values[0])
else:
    StatenIsland = str(data_by_borough["STATEN ISLAND"])

borose = [Brooklyn, Bronx, Manhattan, Queens, StatenIsland]
print(borose)

db_tools.add_db_data("Samdogs", borose)
