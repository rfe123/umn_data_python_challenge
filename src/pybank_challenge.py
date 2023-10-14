# In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. 
# You will be given a financial dataset called budget_data.csv.
# The dataset is composed of two columns: "Date" and "Profit/Losses".

#Load libraries
import os
import csv

# Your task is to create a Python script that analyzes the records to calculate each of the following values:
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period

# Load Dataset
budget_data = os.path.join('Starter_Code','PyBank','Resources','budget_data.csv')

with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheaders = next(csvreader)

    # Initialize Variables
    number_of_months = 0
    net_change = 0
    greatest_profit = ['date', 0]
    greatest_loss = ['date',0]

    # Iterate through rows in CSV
    for row in csvreader:
        # Count the number of Months
        number_of_months += 1
        # Grab the quantity from Profit/Loss column
        change = int(row[1])

        # Accumulate the transactions
        net_change += change
    
        #Store the largest gains and losses
        if change > int(greatest_profit[1]):
            greatest_profit = row
        
        if change < int(greatest_loss[1]):
            greatest_loss = row

#Output our Findings
output_string = "Financial Analysis"
output_string += "\n-------------------------"
output_string += f"\nNumber of Months: {number_of_months}"
output_string += f"\n\nAverage Change: $ {round((net_change/number_of_months),2):.2f}"
output_string += f"\n\nGreatest Profit Increase: {greatest_profit[0]} ($ {int(greatest_profit[1]):.2f})"
output_string += f"\n\nGreatest Profit Decrease: {greatest_loss[0]} ($ {int(greatest_loss[1]):.2f})"

print(output_string)

output_file = os.path.join('Results', 'budget_results.txt')

with open(output_file, 'w') as f:
    f.write(output_string)