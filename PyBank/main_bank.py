import os
import csv

csvpath = os.path.join('budget_data.csv')

# open Budget_data CSV file 
with open(csvpath) as budget:
    csvreader = csv.reader(budget, delimiter = ",")

    # skip header row
    next(csvreader, None)

    # The total number of months included in the dataset
    months = len(list(csvreader))

# open Budget_data CSV file 
with open(csvpath) as budget:
    csvreader = csv.reader(budget, delimiter = ",")

    # skip header row
    next(csvreader, None)

    # The net total amount of "Profit/Losses" over the entire period
    total = 0
    for lines in csvreader:
        total = total + int(lines[1])

    # # The average of the changes in "Profit/Losses" over the entire period
    avg = round(total/months,2)

# open Budget_data CSV file 
with open(csvpath) as budget:
    csvreader = csv.reader(budget, delimiter = ",")

    # skip header row
    next(csvreader, None)

    # The greatest increase in profits (date and amount) over the entire period
    increase = 0
    for lines in csvreader:
        if int(lines[1]) > increase:
            increase = int(lines[1])
            increase_date = lines[0]


# open Budget_data CSV file 
with open(csvpath) as budget:
    csvreader = csv.reader(budget, delimiter = ",")

    # skip header row
    next(csvreader, None)

    # The greatest decrease in losses (date and amount) over the entire period
    decrease = 0
    for lines in csvreader:
        if int(lines[1]) < decrease:
            decrease = int(lines[1])
            decrease_date = lines[0]


    print("Financial Analysis")
    print("--------------------------")
    print(f"Total Months: {months}")
    print(f"Total: ${total}")
    print(f"Average  Change: ${avg}")
    print(f"Greatest Increase in Profits: {increase_date} (${increase})")
    print(f"Greatest Decrease in Profits: {decrease_date} (${decrease})")

# export to text file

# Set variable for output file
output_file = os.path.join("financial_analysis.txt")

with open(output_file, "w") as text_file:
    textwriter = text_file.write(str("Financial Analysis" '\n'
        f"--------------------------" '\n'
        f"Total Months: {months}" '\n'
        f"Total: ${total}" '\n'
        f"Average  Change: ${avg}" '\n'
        f"Greatest Increase in Profits: {increase_date} (${increase})" '\n'
        f"Greatest Decrease in Profits: {decrease_date} (${decrease})")
    )