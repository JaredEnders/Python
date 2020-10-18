import os
import csv

loadedfile = os.path.join("Resources", "budget_data.csv")
outputfile = os.path.join("Analysis", "budgetanalysis.txt")
                           
Totalmonths = 0
Monthchange = []
Netchangelist = []
Greatestincrease = ["", 0]
Greatestdecrease = ["", 999999999]
Netprofit = 0

with open(loadedfile) as financial:
    csvreader = csv.reader(financial)
    header = next(csvreader)
    firstrow = next(csvreader)
    Totalmonths += 1
    Netprofit += int(firstrow[1])
    Previousnet = int(firstrow[1])
    
    for row in csvreader:
        Totalmonths += 1
        Netprofit += int(row[1])
        Netchange = int(row[1]) - Previousnet
        Previousnet = int(row[1])
        Netchangelist += [Netchange]
        Monthchange += [row[0]]
        
        if Netchange > Greatestincrease[1]:
            Greatestincrease[0] = row[0]
            Greatestincrease[1] = Netchange
        
        if Netchange < Greatestdecrease[1]:
            Greatestdecrease[0] = row[0]
            Greatestdecrease[1] = Netchange
            
Averagechange = sum(Netchangelist) / len(Netchangelist)

output = (
    f"Financial Analysis\n"
    f"-----------------------\n"
    f"Total Months: {Totalmonths}\n"
    f"Total: ${Netprofit}\n"
    f"Average Change: ${Averagechange}\n"
    f"Greatest Increase in Profits: {Greatestincrease[0]} (${Greatestincrease[1]})\n"
    f"Greatest Decrease in Profits: {Greatestdecrease[0]} (${Greatestdecrease[1]})\n")

print(output)

with open(outputfile, "w") as txt_file:
    txt_file.write(output)