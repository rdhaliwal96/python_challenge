
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')
output_file = "Resources/results.txt"
 
total_votes = 0
candidates = {}
candidates_percent = {}
winner_count = 0
winner = ""


with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader, None)
    for row in csvreader:
       
        total_votes += 1
       # created a key to return all values in dictionary
        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

       
        for key, value in candidates.items():
            candidates_percent[key] = round((value/total_votes) * 100, 1)
 
        for key in candidates.keys():
            if candidates[key] > winner_count:
                winner = key
                winner_count = candidates[key]


# found that \n makes a new line of string
with open(output_file, 'w') as file:
    file.write("Election Results \n")
    file.write("------------------------------------- \n")
    file.write("Total Votes: " + str(total_votes) + "\n")
    file.write("------------------------------------- \n")
    for key, value in candidates.items():
        file.write(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ") \n")
    file.write("------------------------------------- \n")
    file.write("Winner: " + winner + "\n")
    file.write("------------------------------------- \n")
        