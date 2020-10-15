import os
import csv

wrestlingcsv = os.path.join('..', 'Resources', 'WWE-Data-2016.csv')

def printpercentage(wrestlerdata):
    name = str(wrestlerdata[0])
    wins = int(wrestlerdata[1])
    losses = int(wrestlerdata[2])
    draws = int(wrestlerdata[3])
    totalmatches = wins + losses + draws
    winpercentage = (wins / totalmatches) * 100
    losspercentage = (losses / totalmatches) * 100
    drawpercentage = (draws / totalmatches) * 100
    if losspercentage < 50:
        wrestler = "Superstar"
    else:
        wrestler = "Jobber"
    print(f'Statstics for {name}: ')
    print(f'Win percentage: {winpercentage}')
    print(f'Loss percentage: {losspercentage}')
    print(f'Draw percentage: {drawpercentage}')
    print(f'{name} is a {wrestler}')
     
with open(wrestlingcsv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    nametocheck = input("What wrestler do you want to look for? ")
    for row in csvreader:
        if(nametocheck == row[0]):
            printpercentage(row)