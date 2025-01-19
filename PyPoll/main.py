import csv
import os
from collections import Counter
# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources/election_data.csv")  # Input file path
file_to_output = os.path.join("analysis/election_analysis.txt")  # Output file path

# Initialize variables to track the election data
votes=[] # Track the total number of votes cast
names=[] # Track the names of the candidate

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
    # Increment the total vote count for each row and names
        votes.append(row[0])
        names.append(row[2]) # Get the candidate's name from the row

# count votes.
votes_counter = Counter(votes)
names_counts = Counter(names)
total_votes = sum(names_counts.values())

#count total votes & print
total_votes = len(votes)
print(f"Total votes: {total_votes}")

# calculate percentage votes per candidate & print
for name, count in names_counts.items():
    percentage =(count/total_votes)*100
    print(f'{name}:{percentage:.3f}% {count}')

# find highest vote count to determine winner and print
winner = max(names_counts, key=names_counts.get)
print(f"The winner is: {winner}")

# Write the results to a text file. Including lay-out and header text.
with open(file_to_output, "w") as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("----------------------------\n")
    txt_file.write(f"Total votes: {total_votes}\n")

    for name, count in names_counts.items():
        percentage =(count/total_votes)*100
        txt_file.write(f'{name}:{percentage:.3f}% {count}\n')
 
    txt_file.write("----------------------------\n")
    txt_file.write(f"The winner is: {winner}\n")
    txt_file.write("----------------------------\n")
    

