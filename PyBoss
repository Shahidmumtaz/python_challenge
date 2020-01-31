# Import CSV file
import os
import csv
import re

us_State_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


employee_data = os.path.join("..", "PyBoss", "employee_data.csv")

Emp_ID = []
First_Name = []
Last_Name = []
DOB = []
SSN = []
State = []


with open(employee_data, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	
	for row in employee_data:
		EMP_ID = row[0]
		Emp_ID.append(Emp_ID)
		Name = Name.split()[","]
		FirstName = Name.split()[0]
		LastName = Name.split()[1]
		splitDOB = DOB.split[","]
		Year = splitDOB[0]
		Month = splitDOB[1]
		Day = splitDOB[2]
		formattedDOB = Month + "/" + Day + "/" + Year
		formattedSSN = "***_**_" + SSN.split("_")[2]
    	
		print(f"CSV Header: {csv_header}")	
		for row in csvreader:
			print(["Emp_ID", "First_Name", "Last_Name", "DOB", "SSN", "State"])
