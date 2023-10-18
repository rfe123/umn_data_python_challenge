# In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.
# You will be given a set of poll data called election_data.csv. 
# The dataset is composed of three columns: "Voter ID", "County", and "Candidate". 

import os
import csv

# Your task is to create a Python script that analyzes the votes and calculates each of the following values:
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote

election_data = os.path.join('Starter_Code','PyPoll','Resources','election_data.csv')

with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheaders = next(csvreader)
    # print(csvheaders)
    # ['Ballot ID', 'County', 'Candidate']
    #store the index of column headers for readability
    id = csvheaders.index('Ballot ID')
    county = csvheaders.index('County')
    candidate = csvheaders.index('Candidate')

    # Initialize Variables - ballot counter, and lists for each candidate and # of votes 
    ballots_count = 0
    candidates = []
    count_per_candidate = []

    for row in csvreader:
        #Count the number of ballots cast
        ballots_count += 1

        if row[candidate] in candidates:
            # If this candidate has votes already, count this one for the candidate.
            candidate_id = candidates.index(row[candidate])
            count_per_candidate[candidate_id] += 1
        else:
            # If this candidate hasn't received votes, add them to the list.
            candidates.append(row[candidate])
            count_per_candidate.append(1)
        
    header = ['Candidate', 'Total Votes', 'Percentage of Vote']

    #Calculate the percent for each candidate
    percentage = [round((x / ballots_count) * 100,2) for x in count_per_candidate]

    #find the index of the largest vote count
    winning_index = count_per_candidate.index(max(count_per_candidate))
    
    #Zip the results to more easily print
    election_results = zip(candidates, count_per_candidate, percentage)
    [print(candidate) for candidate in election_results]

    #Print the name of the winning candidate
    print(f"The winner is: {candidates[winning_index]}!")
