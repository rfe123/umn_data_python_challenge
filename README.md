# umn_data_python_challenge
PyBank Instructions
    In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will be given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".

    Your task is to create a Python script that analyzes the records to calculate each of the following values:

    The total number of months included in the dataset

    The net total amount of "Profit/Losses" over the entire period

    The changes in "Profit/Losses" over the entire period, and then the average of those changes

    The greatest increase in profits (date and amount) over the entire period

    The greatest decrease in profits (date and amount) over the entire period

Summary
    To summarize this data, I start by loading it from CSV into a CSV Reader.
    
    Iterating through the rows, I count the number of months represented, and add the profit/loss value to the total "net_change".

    To identify each period change, I subtract the profit/loss result from the previous month's result, and store this change in another totalizer, cumulative_change.

    If this change is larger than the "greatest_increase" stored so far, replace the greatest_increase, including also the month. If this change is less than the "greatest_decrease", similarly store it for greatest_decrease.

    Finally, display the results in Terminal and output to file.

Result

PyPoll Instructions
    In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.

    You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:

    The total number of votes cast
    A complete list of candidates who received votes
    The percentage of votes each candidate won
    The total number of votes each candidate won
    The winner of the election based on popular vote

Summary
    Start by loading the CSV file, and store the header indices.

    Looping through the rows, count the number of ballots cast.
    If the candidate name has been found, count this vote for that candidate. If not, add the name to the list and count this first vote.

    Using List Comprehension - store the percentage of each candidate's vote count compared to the total votes.

    Print results per the Module Challenge format