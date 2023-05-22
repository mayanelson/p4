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


sumMode = True
richmond = True
connection_id = "k397-673e" 
results = client.get(connection_id, limit=100000000, fiscal_year=2022, pay_basis="per Annum", title_description="POLICE OFFICER")
results_df = pd.DataFrame.from_records(results)
print(results_df.columns)
borough_label = "work_location_borough"
if(sumMode):
# Convert to pandas DataFrame
    id_label = "job_number"
    data_by_borough = results_df.groupby(borough_label).size().reset_index(name='n')
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

Brooklyn = str(data_by_borough.loc[data_by_borough[borough_label] == 'BROOKLYN', 'n'].values[0])
Manhattan = str(data_by_borough.loc[data_by_borough[borough_label] == 'MANHATTAN', 'n'].values[0])
Queens = str(data_by_borough.loc[data_by_borough[borough_label] == 'QUEENS', 'n'].values[0])
Bronx = str(data_by_borough.loc[data_by_borough[borough_label] == 'BRONX', 'n'].values[0])
if(richmond):
    StatenIsland = str(data_by_borough.loc[data_by_borough[borough_label] == 'RICHMOND', 'n'].values[0])
else:
    StatenIsland = str(data_by_borough["STATEN ISLAND"])

borose = [Brooklyn, Bronx, Manhattan, Queens, StatenIsland]
print(borose)

db_tools.add_db_data("PoliceOfficers", borose)
