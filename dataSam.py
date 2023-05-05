# use pandas to read csv file Citywide.csv
import pandas as pd
import numpy as np

payrollData = pd.read_csv('Citywide_Payroll_Data__Fiscal_Year_.csv')
# Select only columns "Work Location Borough" and "Base Salary" and "Total OT Paid" and "Total Other Pay"
payrollData = payrollData[["Work Location Borough", "Base Salary", "Total OT Paid", "Total Other Pay"]]

print(payrollData.head(5))
