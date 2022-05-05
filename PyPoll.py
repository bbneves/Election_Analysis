print('')
# The data we need to retrieve

# Dependencies
import csv
import os

# Variable to load the file from a path.

file1read = os.path.join('Resources', 'election_results.csv')

#Variable to save the file to a path.

file2save = os.path.join('analysis','election_analysis.txt')

# Opening the file to read:

with open(file1read, 'r') as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Header row from the CSV File.
    header = next(file_reader)
    print(header)

    # 1. The total number of votes cast.

    # 2. S complete list of candidates who received votes.

    # 3. The percentage of votes easch candidate won

    # 4. The total number of votes each candidate won.

    # 5. The winner of the election based on popular vote.
