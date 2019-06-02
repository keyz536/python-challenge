import os
import csv

csvpath = os.path.join('/Users/christianattard/python-challenge/PyPoll/election_data.csv')

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    header = next(csvreader)
    voter_count = 0
    CorreyVotes = 0
    KhanVotes = 0
    LiVotes = 0
    TooleyVotes = 0
    
    for row in csvreader:
        voter_count += 1
        if row[2] == 'Correy':
            CorreyVotes += 1
        elif row[2] == 'Khan':
            KhanVotes += 1
        elif row[2] == 'Li':
            LiVotes += 1
        elif row [2] == "O'Tooley":
            TooleyVotes += 1

    CorreyVotesPercent = float(CorreyVotes / voter_count * 100)
    KhanVotesPercent = float(KhanVotes / voter_count * 100)
    LiVotesPercent = float(LiVotes / voter_count * 100)
    TooleyVotesPercent = float(TooleyVotes / voter_count * 100)

    if CorreyVotesPercent > KhanVotesPercent and LiVotesPercent and TooleyVotesPercent:
        winner = "Correy"
    elif KhanVotesPercent > CorreyVotesPercent and LiVotesPercent and TooleyVotesPercent:
        winner = "Khan"
    elif LiVotesPercent > CorreyVotesPercent and KhanVotesPercent and TooleyVotesPercent:
        winner = "Li"
    else:
        winner = "O'Tooley"

    print(f"Election Results")
    print(f"--------------------------------")
    print(f"Total Votes: {str(voter_count)}")
    print(f"--------------------------------")
    print(f"Khan: {round(KhanVotesPercent)}% ({KhanVotes})")
    print(f"Correy: {round(CorreyVotesPercent)}% ({CorreyVotes})")
    print(f"Li: {round(LiVotesPercent)}% ({LiVotes})")
    print(f"O'Tooley: {round(TooleyVotesPercent)}% ({TooleyVotes})")
    print(f"--------------------------------")
    print(f"Winner: {winner}")
    print(f"--------------------------------")
    
output_path = os.path.join('/Users/christianattard/python-challenge/PyPoll/election_data.txt')
with open(output_path, 'w') as textfile:
    textwriter = csv.writer(textfile)

    print(f"Election Results", file = textfile)
    print(f"--------------------------------", file = textfile)
    print(f"Total Votes: {str(voter_count)}", file = textfile)
    print(f"--------------------------------", file = textfile)
    print(f"Khan: {round(KhanVotesPercent)}% ({KhanVotes})", file = textfile)
    print(f"Correy: {round(CorreyVotesPercent)}% ({CorreyVotes})", file = textfile)
    print(f"Li: {round(LiVotesPercent)}% ({LiVotes})", file = textfile)
    print(f"O'Tooley: {round(TooleyVotesPercent)}% ({TooleyVotes})", file = textfile)
    print(f"--------------------------------", file = textfile)
    print(f"Winner: {winner}", file = textfile)
    print(f"--------------------------------", file = textfile)