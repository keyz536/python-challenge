import os
import csv

csvpath = os.path.join('/Users/christianattard/python-challenge/PyBank/budget_data4.csv')

with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    header = next(csvreader)
    month_count = 0
    total = 0
    total_list = []
    difference_list = []

    for row in csvreader:
        ProfitLoss = int(row[1])
        total += ProfitLoss
        month_count += 1
        total_list.append(ProfitLoss)

    print(f"Financial Analysis")
    print(f"------------------")
    print(f"Total Months: {str(month_count)}")
    print(f"Total: ${str(total)}")
    
    for num in range(1,len(total_list)):
        difference_list.append(total_list[num]-total_list[num-1])
        average = round(sum(difference_list)/len(difference_list))
        difference_max = max(difference_list)
        difference_min = min(difference_list)

    print(f"Average Change: ${str(average)}")
    print(f"Greatest Increase: (${round(difference_max)})")
    print(f"Greatest Decrease: (${round(difference_min)})")

output_path = os.path.join('/Users/christianattard/python-challenge/PyBank/budget_data.txt')
with open(output_path, 'w') as textfile:
    textwriter = csv.writer(textfile)

    print(f"Financial Analysis", file = textfile)
    print(f"------------------", file = textfile)
    print(f"Total Months: {str(month_count)}", file = textfile)
    print(f"Total: ${str(total)}", file = textfile)
    print(f"Average Change: ${str(average)}", file = textfile)
    print(f"Greatest Increase: (${round(difference_max)})", file = textfile)
    print(f"Greatest Decrease: (${round(difference_min)})", file = textfile)