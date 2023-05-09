import pandas as pd
import numpy as np
import db_tools
import math
from sodapy import Socrata


# load the CSV file into a pandas DataFrame
df = pd.read_csv('ntaPop.csv')

# filter the data to only include the year 2000
df = df[df['Year'] == 2000]

# group the data by borough and sum up the population values
pop_by_borough = df.groupby('Borough')['Population'].sum()

# print the resulting Series
print(pop_by_borough)

#!/usr/bin/env python

# make sure to install these packages before running:
# pip install pandas
# pip install sodapy


# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:

'''
Film Permits by Borough
'''
client = Socrata("data.cityofnewyork.us", "qE4zlRbUa5QqMb2dbqEMQiCse")

# Example authenticated client (needed for non-public datasets):
# client = Socrata(data.cityofnewyork.us,
#                  MyAppToken,
#                  username="user@example.com",
#                  password="AFakePassword")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("tg4x-b46p", limit=14000)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)

permits_by_borough = results_df.groupby('borough')['eventid'].count()
print(permits_by_borough)
print(results_df.shape)


'''
Payroll by Borough
'''

# results2 = client.get("k397-673e", limit=6000000, fiscal_year=2022, pay_basis="per Annum")
# results_df2 = pd.DataFrame.from_records(results2)
# print(results_df2.shape)
# results_df2['base_salary'] = results_df2['base_salary'].astype(float)
# results_df2['total_ot_paid'] = results_df2['total_ot_paid'].astype(float)
# results_df2['total_other_pay'] = results_df2['total_other_pay'].astype(float)

# payroll_by_borough = results_df2.groupby('work_location_borough')['base_salary'].mean()
# payroll_by_borough2 = results_df2.groupby('work_location_borough')['total_ot_paid'].mean()
# payroll_by_borough3 = results_df2.groupby('work_location_borough')['total_other_pay'].mean()

# print(payroll_by_borough)
# print(payroll_by_borough2)
# print(payroll_by_borough3)

# # write a list combining the means of the three types of income by borough. Note that there are additional datapoints to the five boroughs of NYC
# Brooklyn = payroll_by_borough["BROOKLYN"] + payroll_by_borough2["BROOKLYN"] + payroll_by_borough3["BROOKLYN"]
# print("Brooklyn: ", Brooklyn)
# Manhattan = payroll_by_borough["MANHATTAN"] + payroll_by_borough2["MANHATTAN"] + payroll_by_borough3["MANHATTAN"]
# print("Manhattan: ", Manhattan)
# Queens = payroll_by_borough["QUEENS"] + payroll_by_borough2["QUEENS"] + payroll_by_borough3["QUEENS"]
# print("Queens: ", Queens)
# Bronx = payroll_by_borough["BRONX"] + payroll_by_borough2["BRONX"] + payroll_by_borough3["BRONX"]
# print("Bronx: ", Bronx)
# Richmond = payroll_by_borough["RICHMOND"] + payroll_by_borough2["RICHMOND"] + payroll_by_borough3["RICHMOND"]
# print("Richmond: ", Richmond)

# boros = [Brooklyn, Bronx, Manhattan, Queens, Richmond]
# db_tools.add_db_data("Total Payroll", boros)
'''
Rat Inspections by Borough
'''

rat_results = client.get("p937-wjvj", limit=3000000, result="Rat Activity")
rat_records = pd.DataFrame.from_records(rat_results)
#print(rat_records)
failed_inspections_by_borough = rat_records.groupby('borough')['job_id'].count()
print(failed_inspections_by_borough)

ft_results = client.get("wxhr-qbhz", limit=1000000)
ft_records = pd.DataFrame.from_records(ft_results)
fountains_by_borough = ft_records.groupby('borough')['ampsid'].count()
print(fountains_by_borough)


