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

    first = next(csvreader)

    # Initialize Variables
    number_of_months = 1
    previous_result = int(first[1])

    # ignore the first month when finding the greatest increase/decrease
    greatest_increase = ['date', 0]
    greatest_decrease = ['date',0]

    net_change = int(first[1])
    cumulative_change = 0

    # Iterate through rows in CSV
    for row in csvreader:
        # Count the number of Months
        number_of_months += 1
        # Grab the quantity from Profit/Loss column
        monthly_result = int(row[1])
        
        #Calculate the 
        change = (monthly_result - previous_result)

        # Accumulate the transactions
        net_change += monthly_result

        # Calculate the total change - from previous result to this month and store
        cumulative_change += change

        #Keep track of this change to calculate the next cumulative change
        previous_result = monthly_result

        # Troubleshooting to verify Change logic
        # print(f"Month: {row[0]} P/L: {row[1]} Previous: {previous_result} Change: {change}")

        #Store the largest increase and decrease to the profit
        if change > int(greatest_increase[1]):
            greatest_increase = [row[0],change]
        
        if change < int(greatest_decrease[1]):
            greatest_decrease = [row[0],change]

#Output our Findings
output_string = "\nFinancial Analysis"
output_string += "\n-------------------------"
output_string += f"\nNumber of Months: {number_of_months}"
output_string += f"\nTotal: ${net_change}"
output_string += f"\nAverage Change: $ {round((cumulative_change/(number_of_months - 1)),2):.2f}"
output_string += f"\nGreatest Profit Increase: {greatest_increase[0]} ($ {int(greatest_increase[1]):.2f})"
output_string += f"\nGreatest Profit Decrease: {greatest_decrease[0]} ($ {int(greatest_decrease[1]):.2f})\n"

print(output_string)

output_file = os.path.join('Results', 'budget_results.txt')

with open(output_file, 'w') as f:
    f.write(output_string)