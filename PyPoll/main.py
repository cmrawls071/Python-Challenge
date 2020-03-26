import csv

# make a list to hold candidate names
candidates = []

# open Budget_data CSV file 
with open('election_data.csv', mode= 'r') as election:
    csvreader = csv.reader(election, delimiter = ",")

    # skip header row
    next(csvreader, None)

    # find the total number of votes cast by counting each row in the file (less the header, which was skipped above)
    votes = len(list(csvreader))
    # print(votes)

with open('election_data.csv', mode= 'r') as election:
    csvreader = csv.reader(election, delimiter = ",")

    # skip header row
    next(csvreader, None)    

    # loop through the Candidate column (column 3) and add any unique instance of a candidate's name to the Candidates list
    for lines in csvreader:
        if lines[2] not in candidates:
            candidates.append(lines[2])
    
    # double check the number of candidates found
    # for cand in candidates:
    #     print(cand)

with open('election_data.csv', mode= 'r') as election:
    csvreader = csv.reader(election, delimiter = ",")

    # skip header row
    next(csvreader, None)

    # find the total number of votes each candidate won
    # set values to hold the total number of votes per candidate
    cand1 = 0
    cand2 = 0
    cand3 = 0
    cand4 = 0
    
    # loop through the Candidate column (column 3) and add up the number of times their name appears in the column
    for lines in csvreader:
        if str(lines[2]) == str(candidates[0]):
            cand1 = cand1 + 1
        elif str(lines[2]) == str(candidates[1]):
            cand2 = cand2 + 1
        elif str(lines[2]) == str(candidates[2]):
            cand3 = cand3 + 1
        elif str(lines[2]) == str(candidates[3]):
            cand4 = cand4 + 1


    # find the percentage of votes each candidate won
    cand1_percent = round(float(cand1/votes)*100,2)
    cand2_percent = round(float(cand2/votes)*100,2)
    cand3_percent = round(float(cand3/votes)*100,2)
    cand4_percent = round(float(cand4/votes)*100,2)

cand_totals = [cand1_percent, cand2_percent, cand3_percent, cand4_percent]

with open('election_data.csv', mode= 'r') as election:
    csvreader = csv.reader(election, delimiter = ",")

    # skip header row
    next(csvreader, None)

    # The winner of the election based on popular vote.
    if max(cand_totals) == cand1_percent:
        winner = candidates[0]
    elif max(cand_totals) == cand2_percent:
        winner = candidates[1]
    elif max(cand_totals) == cand3_percent:
        winner = candidates[2]
    elif max(cand_totals) == cand4_percent:
        winner = candidates[3]


    print("Election Results")
    print("--------------------------")
    print(f"Total Votes: {votes}")
    print("--------------------------")
    print(f"{candidates[0]}: {cand1_percent}% ({cand1})")
    print(f"{candidates[1]}: {cand2_percent}% ({cand2})")
    print(f"{candidates[2]}: {cand3_percent}% ({cand3})")
    print(f"{candidates[3]}: {cand4_percent}% ({cand4})")
    print("--------------------------")
    print(f"Winner: {winner}")
    print("--------------------------")


with open("election_results.txt", "w") as text_file:
  textwriter = text_file.write(str("Election Results" '\n'
        f"--------------------------" '\n'
        f"Total Votes: {votes}" '\n'
        f"--------------------------" '\n'
        f"{candidates[0]}: {cand1_percent}% ({cand1})" '\n'
        f"{candidates[1]}: {cand2_percent}% ({cand2})" '\n'
        f"{candidates[2]}: {cand3_percent}% ({cand3})" '\n'
        f"{candidates[3]}: {cand4_percent}% ({cand4})" '\n'
        f"--------------------------" '\n'
        f"Winner: {winner}" '\n'
        f"--------------------------")
    )