# Import CSV File
import os
import csv

PyPollcsv = "election_data.csv"

# Create and open file

with open(PyPollcsv, 'r') as csvfile:
	election_data = csv.reader(csvfile, delimiter = ",")
	header = next(election_data)

	# Calculate votes for each candidate and determine Highest votes

	Vote_count = 0
	Highest_votes = 0
	Candidate = {}

	for row in election_data:
		Vote_count += 1
		Candidate[row[2]] = Candidate.get(row[2], 0) + 1

# Print output

print()
print(f"Election Results")
print(f"--------------------")
print(f"Total Votes: {Vote_count}")

for Candidate, vote in Candidate.items():
	print(f"{Candidate}: {vote / Vote_count * 100:.3f}% ({vote})")
	if vote > Highest_votes:
		vote = Highest_votes
		winner = Candidate

# Declare the Winner!!!

print(f"------------------")
print(f"Winner!!!: {winner}")
