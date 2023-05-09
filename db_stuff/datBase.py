import pandas as pd
import numpy as np
import db_tools
import math
from sodapy import Socrata


# make sure to install these packages before running:
# pip install pandas
# pip install sodapy


# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("data.cityofnewyork.us", "qE4zlRbUa5QqMb2dbqEMQiCse")

# Example authenticated client (needed for non-public datasets):
# client = Socrata(data.cityofnewyork.us,
#                  MyAppToken,
#                  username="user@example.com",
#                  password="AFakePassword")

# First 2000     results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
sumMode = True
richmond = False
connection_id = "kfp4-dz4h" 
results = client.get(connection_id)
results_df = pd.DataFrame.from_records(results)
print(results_df.columns)
borough_label = "borough"
if(sumMode):
# Convert to pandas DataFrame
    id_label = "job_number"
    data_by_borough = results_df.groupby(borough_label)[id_label].count()
    print(data_by_borough)
    #print(permits_by_borough)
#print(results_df.shape)
# results = [0,0,0,0,0,0]
# maps = {"Brooklyn":0, "Manhattan": 1, "Queens": 2, "Bronx": 3, "Staten Island": 4, "Richmond": 6}

# print(results_df.head(5)["borough"])
# count = 0
# for row in results_df:
#     if row["borough"] == "Brooklyn":
#         count += 1

#print(count)
else:
    data_label = "base_salary"
    results_df[data_label] = results_df['data_label'].astype(float)

    data_by_borough = results_df.groupby(borough_label)[data_label].mean()

    print(data_by_borough)
    # write a list combining the means of the three types of income by borough. Note that there are additional datapoints to the five boroughs of NYC
    Brooklyn = data_by_borough["BROOKLYN"]
    Manhattan = data_by_borough["MANHATTAN"]
    Queens = data_by_borough["QUEENS"]
    Bronx = data_by_borough["BRONX"]
    if(richmond):
        StatenIsland = data_by_borough["RICHMOND"]
    else:
        StatenIsland = data_by_borough["STATEN ISLAND"]

        