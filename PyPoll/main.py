# Assignment 3: Python Challenge 2 "PyPoll"

# Calculate:
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

#---------------------------
# Import the module
import os

# Module for reading CSV file
import csv

# Get the path to this script
scriptpath = os.path.dirname(__file__)

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

# Open csv file in read mode
with open(csvpath) as csvfile:
    poll_data = csv.reader(csvfile, delimiter=',')
        
# Set header
    csv_header = next(poll_data)
        
    # Initialize list to store data
    cand_l = []

    # Loop through file and add candidates to list
    for row in poll_data:
        cand_l.append(row[2])

    # Count all votes for each candidate
    votes_count = [[c, cand_l.count(c)] for c in set(cand_l)]

    # Sort list of votes per votes count in descending order
    votes_count = sorted(votes_count, key = lambda k: k[1], reverse = True)
    # Calculate total number of votes
    total_votes = len(cand_l)
    # Find the winner who is at the top of the sorted list
    winner = votes_count[0][0]

    # Print output analysis results on terminal
    # Export to text file election results
    # Set string variable for a line
    line = f"-------------------------\n"

    # Initialize variable for keeping votes results for all candidates
    out = ""
    # Calculate percent of votes for each candidate
    # Place vote results for candidates in string variable "out"
    for name, count in votes_count:
        percent_votes = (count / total_votes) * 100
        out = out + f"{name}: {percent_votes:.3f}% ({count})\n"

    # Generate output with election results
    analyis = (f"\nElection Results\n" \
        + line +
        f"Total Votes: {total_votes}\n" 
        + line
        + out 
        + line +
        f"Winner: {winner}\n"
        + line
            )

    # Display election results
    print (analyis)

    # Export election results to text file
    results = os.path.join("Analysis", "election_results.txt")
    with open(results, "w") as f:
        print(analyis, file=f)
