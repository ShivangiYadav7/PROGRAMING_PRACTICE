#Number_gussing_game

guesse=0
secret_number=7
while guesse!=secret_number:
    guesse=int(input("Enter the scret number:"))
    if guesse==secret_number:
        print("Congratulation: you guessed correct number")
    else:
        print("Incorrect number please try again")    