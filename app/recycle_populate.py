import pandas as pd
import numpy as np
import db_tools
import math
from sodapy import Socrata

client = Socrata("data.cityofnewyork.us", "qE4zlRbUa5QqMb2dbqEMQiCse")


sumMode = True
richmond = False
connection_id = "sxx4-xhzg"
results = client.get(connection_id, limit=1000)
results_df = pd.DataFrame.from_records(results)
print(results_df.columns)
borough_label = "dsny_zone"
if(sumMode):
# Convert to pandas DataFrame
    id_label = "site_location"
    data_by_borough = results_df.groupby(borough_label)[id_label].count()
    print(data_by_borough)
    #print(permits_by_borough)

else:
    data_label = "base_salary"
    results_df[data_label] = results_df['data_label'].astype(float)

    data_by_borough = results_df.groupby(borough_label)[data_label].mean()

    print(data_by_borough)
    # write a list combining the means of the three types of income by borough. Note that there are additional datapoints to the five boroughs of NYC
Brooklyn = str(data_by_borough["BKS"] + data_by_borough["BKN"])
Manhattan = str(data_by_borough["MAN"])
Queens = str(data_by_borough["QE"] + data_by_borough["QW"])
Bronx = str(data_by_borough["BX"])
if(richmond):
    StatenIsland = str(data_by_borough["RICHMOND"])
else:
    StatenIsland = str(data_by_borough["SI"])

borose = [Brooklyn, Bronx, Manhattan, Queens, StatenIsland]
print(borose)

db_tools.add_db_data("recycling_bins", borose)
