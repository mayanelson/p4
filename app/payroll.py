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


sumMode = False
richmond = True
connection_id = "k397-673e" 
results = client.get(connection_id, limit=100000, fiscal_year=2022, pay_basis="per Annum")
results_df = pd.DataFrame.from_records(results)
print(results_df.columns)
borough_label = "work_location_borough"
if(sumMode):
# Convert to pandas DataFrame
    id_label = "job_number"
    data_by_borough = results_df.groupby(borough_label)[id_label].count()
    print(data_by_borough)
    #print(permits_by_borough)

else:
    data_label = "base_salary"
    data_label2 = "total_ot_paid"
    data_label3 = "total_other_pay"
    results_df[data_label] = results_df[data_label].astype(float)
    results_df[data_label2] = results_df[data_label2].astype(float)
    results_df[data_label3] = results_df[data_label3].astype(float)
    data_by_borough = results_df.groupby(borough_label)[data_label].mean()
    data_by_borough2 = results_df.groupby(borough_label)[data_label2].mean()
    data_by_borough3 = results_df.groupby(borough_label)[data_label3].mean()
    # write a list combining the means of the three types of income by borough. Note that there are additional datapoints to the five boroughs of NYC
    data_sum = data_by_borough + data_by_borough2 + data_by_borough3
    print(data_sum)

Brooklyn = data_sum["BROOKLYN"]
Manhattan = data_sum["MANHATTAN"]
Queens = data_sum["QUEENS"]
Bronx = data_sum["BRONX"]
if(richmond):
    StatenIsland = data_sum["RICHMOND"]
else:
    StatenIsland = data_sum["STATEN ISLAND"]

borose = [Brooklyn, Bronx, Manhattan, Queens, StatenIsland]
print(borose)

db_tools.add_db_data("total payroll", borose)
