# use pandas to read csv file Citywide.csv
import pandas as pd
import numpy as np
import db_tools
import math

payrollDataZ = pd.read_csv('../Citywide_Payroll_Data__Fiscal_Year_.csv')
payrollData = payrollDataZ[payrollDataZ["Fiscal Year"] == 2020]
payrollData = payrollData[["Fiscal Year", "Work Location Borough", "Base Salary", "Total OT Paid", "Total Other Pay"]]
print(payrollData.head(5))
#write a function to find all commas in the "Base Salary", Total OT paid, and total other pay column and replace them with nothing
payrollData["Base Salary"] = payrollData["Base Salary"].str.replace(',', '')
payrollData["Total OT Paid"] = payrollData["Total OT Paid"].str.replace(',', '')
payrollData["Total Other Pay"] = payrollData["Total Other Pay"].str.replace(',', '')
#trim down the data to only fiscal year 2022

print("test2")
for i in range(len(payrollData["Base Salary"])):
    if (i % 1000 == 0):
        print(i)       
    #print(payrollData.loc[i, "Base Salary"])
    payrollData.loc[i, "Base Salary"] = str(payrollData.loc[i, "Base Salary"])
    payrollData.loc[i, "Total OT Paid"] = str(payrollData.loc[i, "Total OT Paid"])
    payrollData.loc[i, "Total Other Pay"] = str(payrollData.loc[i, "Total Other Pay"])
    payrollData.loc[i, "Base Salary"] = payrollData.loc[i, "Base Salary"].replace(',', '')
    payrollData.loc[i, "Total OT Paid"] = payrollData.loc[i, "Total OT Paid"].replace(',', '')
    payrollData.loc[i, "Total Other Pay"] = payrollData.loc[i, "Total Other Pay"].replace(',', '')
    payrollData.loc[i, "Base Salary"] = float(payrollData.loc[i, "Base Salary"])
    payrollData.loc[i, "Total OT Paid"] = float(payrollData.loc[i, "Total OT Paid"])
    payrollData.loc[i, "Total Other Pay"] = float(payrollData.loc[i, "Total Other Pay"])
    payrollData.loc[i, "Total Pay"] = float(payrollData.loc[i, "Base Salary"]) + float(payrollData.loc[i, "Total OT Paid"]) + payrollData.loc[i, "Total Other Pay"]
# payrollData["Base Salary"] = payrollData["Base Salary"].astype(float)
# payrollData["Total OT Paid"] = payrollData["Total OT Paid"].astype(float)
# payrollData["Total Other Pay"] = payrollData["Total Other Pay"].astype(float)

#payrollData["Total Pay"] = float(payrollData["Base Salary"]) + float(payrollData["Total OT Paid"]) + float(payrollData["Total Other Pay"])
#payrollData = payrollData[["Work Location Borough", "Total Pay"]]
print("-------------------------------------")
print("total pay + borough")
print(payrollData.head(5))



# # Write a function to find the mean of total pay, given a borough
def findMean(borough):
    boroughData = payrollData[payrollData["Work Location Borough"] == borough]
    #use a for loop to find the mean of the total pay column
    total = 0
    #boroughData["Total Pay"] = boroughData["Total Pay"].astype(float)
    j = 1
    for i in range(len(boroughData)):
        if i in boroughData.index:
            if not(math.isnan(boroughData.loc[i, "Base Salary"])):
                total += boroughData.loc[i, "Base Salary"]
                j += 1
    print("FINAL TOTAL", total)
    return total / j
boroughs = ["BRONX","MANHATTAN",  "BROOKLYN", "QUEENS", "RICHMOND"]
for borough in boroughs:
    print(borough, ':')
    print(findMean(borough))
