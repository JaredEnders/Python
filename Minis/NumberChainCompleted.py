game = "Yes"

while game == "Yes":
    number = int(input("How many numbers? "))
    for x in range(number):
        print(x)

    game = input("Would you like to continue? Yes or No? ")
    