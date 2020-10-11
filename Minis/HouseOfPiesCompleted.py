pieorder = "Yes"
piechoice = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
pielist = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun", "Blueberry", "Buko", "Burek", "Tamale", "Steak"]

print("Welcome to the House of Pies! Here are our pie flavors:")

while pieorder == "Yes":
    print("--------------------------------------------")
    print("[1] Pecan, [2] Apple Crisp, [3] Bean, [4] Banoffee, [5] Black Bun, [6] Blueberry, [7] Buko, [8] Burek, [9] Tamale, [10] Steak")
    
    piepick = input("Which pie would you like to select? ")
    pickindex = int(piepick) - 1
    piechoice[pickindex] += 1

    print("--------------------------------------------")
    print("Great! We'll have your " + pielist[int(piepick) - 1] + " pie right out!")
    
    pieorder = input("Would you like to select another pie: Yes or No? ")

print("--------------------------------------------")
print("You've purchased: ")

for pieindex in range(len(pielist)):
    piecount = str(piechoice[pieindex])
    piename = str(pielist[pieindex])

    print(piecount + " " + piename)    