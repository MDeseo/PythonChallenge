# Assignment 3: Python Challenge 1 "pybank"

# Instructions: 
# 1. Count the total number of months included in the dataset
# 2. The net total amount of "Profit/Losses" over the entire period
# 3. The changes in "Profit/Losses" over the entire period, and then the average of those changes
# 4. The greatest increase in profits (date and amount) over the entire period
# 5. The greatest decrease in profits (date and amount) over the entire period

# Import the module
import os

# Module for reading CSV file
import csv

# Get the path to this script
scriptpath = os.path.dirname(__file__)

# Join script path to csv file
csvpath = os.path.join(scriptpath, 'Resources', 'budget_data.csv')

#----------------------------------------------------------
 # Print the current working directory to check
# print("Current working directory: {0}".format(os.getcwd()))
#----------------------------------------------------------

# Reading using CSV module
with open(csvpath) as csvfile:

    # Specify delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

   # Read the header row to check if reading the correct csv file
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # List to store data
    months = []
    profit_losses = []

    #Set start conditions
    total = 0
    a_change = 0
    m_change = 0
    m_count = 0
    delta1 = 0
    delta2 = 0
    delta_line1 = 0
    delta_line2 = 0
    loop1 = 0
    loop2 = 0

    # Read in each row of data after the header and write data into assigned lists
    for row in csvreader:
        month = row[0]
        profit_loss = row[1]
        months.append(month)
        profit_losses.append(profit_loss)
    # Count the total of months in the "Date" column
    m_count = len(months)

# Begin analysis
for loop1 in range (m_count):
    total=total+int(profit_losses[loop1])
#print(total)

for loop2 in range (m_count-1):
    a_change = a_change+(float(profit_losses[loop2+1])-float(profit_losses[loop2]))
#print(a_change/(m_count-1))
    m_change = (float(profit_losses[loop2+1])-float(profit_losses[loop2])) 
    if m_change > delta1: #Determine greatest increase
        delta1 = m_change
        delta_line1=loop2
    else:
        delta1 = delta1

#print(delta1)
#print(months[delta_line1+1])

    if m_change<delta2: #Determin greatest decrease
        delta2 = m_change
        delta_line2 = loop2
    else:
        delta2 = delta2

#print(delta2)
#print(months[delta_line2+1])

# Generate output
analysis = f'\
Financial Analysis\n\
----------------------------\n\
Total Months: {m_count}\n\
Total Amount: ${total}\n\
Average Change: ${round(a_change/(m_count-1),2)}\n\
Greatest Increase in Profits: {months[delta_line1+1]} (${int(delta1)})\n\
Greatest Decrease in Profits: {months[delta_line2+1]} (${int(delta2)})\n'

# Print output analysis results on terminal
print(analysis) #Output results on screen

# Write into text file named analysis_pybank.txt
results = os.path.join("Analysis", "analysis_pybank.txt")
with open(results, "w") as f:
    print(analysis, file=f)
