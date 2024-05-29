# Why re-invent the wheel?
import pandas as pd
import numpy as np

# Collect data from given CSV into a pandas DataFrame
data = pd.read_csv('city-of-seattle-2012-expenditures-dollars.csv')

# Select unique department names
departments = data["Department"].unique()

#Replace NaN's with 0
data["2012 Actual"] = data["2012 Actual"].fillna(0)

# Loop over unique departments
for dept in departments:
	# Sum elements of the "2012 Actual" column, if their department is the current department
	dept_sum = + sum(data.loc[data["Department"] == dept]["2012 Actual"])

	# Print the sum nicely
	print(str(dept) + ":\t" + str(dept_sum))
