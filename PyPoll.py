print('')
# The data we need to retrieve

# Dependencies
import csv
import os

# Variable to load the file from a path.

file_to_load = os.path.join('Resources', 'election_results.csv')

#Variable to save the file to a path.

file_to_save = os.path.join('analysis','election_analysis.txt')

# 1. The total number of votes cast 
# 2. List of all candidate names.
# 3. Dictionary for the count for each candidate.

candidate_options = []
total_votes = 0
candidate_votes = {}


# Opening the file to read:

with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Header row from the CSV File.
    header = next(file_reader)
    
    # Print every row in the CSV file:

    for row in file_reader:
        
        # 1.1 Adding the total vote count
        total_votes += 1

        # 2.1 Print the candidate name from each row.
        candidate_name = row[2]

        # 2.2 Add a unique candidate name to the candidate list.
        if candidate_name not in candidate_options:
            
            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0

        # counting up the votes for each candidate
        candidate_votes[candidate_name] += 1

# Winning Candidate and Winning Count Tracker.

win_candidate = ""
win_count = 0
win_percent = 0

# Looping to retrieve the candidates, votes, and percentage.
for candidate_name in candidate_votes:

    votes = candidate_votes[candidate_name]
    
    votes_percentage = (float(votes) / float(total_votes)) * 100

    print(f" {candidate_name}: {votes_percentage:.1f}% ({votes}).")
    print('') 

    # Comparing the candidates and select the one with the highest vote count.
    if votes > win_count:
        win_count = votes
        win_percent = votes_percentage
        win_candidate = candidate_name
    the_winner = (
        f"----------------------------------------\n"
        f"Winner: {win_candidate}\n"
        f"Winning Vote Count: {win_count:,} votes\n"
        f"Winning Percentage: {win_percent:1f}%\n"
        f"----------------------------------------\n"
    )    
print(the_winner)
print('')
