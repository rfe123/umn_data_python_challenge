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

    csvheader = next(csvreader)
    print(csvheader)
    print("-------------------------")

    for row in csvreader:
        print(row)