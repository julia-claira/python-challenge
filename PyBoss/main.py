#-------imports necessary modules
import os
import pandas as pd


#---------declares variables
first_names=[] #the first names of employees
last_names=[] #the last names of employees
date_formated=[] #temporarily holds the reformated dates
ssn_last_four=[] #temporarily holds last four numbers
states_ab=[] #temporarily holds the list of abbreviated states

#dictionary for state abbreviations----------
us_state_abbrev = {
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


#-------opens csv file for reading
csvpath= os.path.join("Resources","employee_data.csv")
employee_df = pd.read_csv(csvpath)


#---------splits names into first and last
names_split=employee_df["Name"].str.split(" ")

for row in names_split:
    first_names.append(row[0])
    last_names.append(row[1])
    
employee_df["First Name"] = first_names #adds column
employee_df["Last Name"] = last_names #adds colum


#----------splits date and reformats
date_split=employee_df["DOB"].str.split("-")

for i in date_split:
    date_formated.append(i[1]+"/"+i[2]+"/"+i[0]) #reformats date
    
employee_df["DOB"] = date_formated #overwrites with new date formatting



#----------splits ssn number and then hides first five numbers
ss_split=employee_df["SSN"].str.split("-")

for i in ss_split:
    ssn_last_four.append("***-**-" + i[2])
    
employee_df["SSN"]= ssn_last_four #overwrites with new SSN formatting


#----------changes the States to their abbreviations
states_temp=employee_df["State"]

for i in states_temp:
    states_ab.append(us_state_abbrev[i])
    
employee_df["State"]= states_ab #overwrites with abbreviated States


#----------outputs newly reformated csv file-------------------------
employee_df_reformat=employee_df[["Emp ID","First Name","Last Name","DOB","SSN","State"]]

#print (employee_df_reformat.head())
output_path = os.path.join("Resources","employee_data_reformat.csv")
employee_df_reformat.to_csv(output_path, index=False, header=True)


    




