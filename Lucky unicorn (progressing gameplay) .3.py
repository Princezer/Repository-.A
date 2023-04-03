#Varibles
confirm = "n"
Tokens = ["Unicorn", "Donkey", "Donkey", "Horse", "Horse", "Zebra",
              "Zebra"]
Cash = 0

#imports
import random

# welcome to game / instructions

print("Welcome to Lucky Unicorn :)\n"
        "In this game you will pay a certain amount and recive a "
        "token.\n"
        "That token will be a unicorn, a horse, a zebra, "
        "or a donkey.\n"
        "depending on what token you get, you will get anywhere "
        "between $0 and $5 back.\n"
        "each token costs 1$ each and you can play with up to $10 "
        "dollars at a time.\n"
        "good luck :)")

# how much do you want to play with? / confirm play

while confirm != "y":
    initial_payment = int(input("\nHow much would you like to pay with?: "))
    Cash = Cash + initial_payment
    print (Cash)

    while initial_payment > 10 or initial_payment < 1:
        initial_payment = int(input("\nSorry\nthe number you put in is not a "
                                    "valid payment price\n"
                                    "remember, it must be less then $10\n\n"
                                    "How much would you like to play with?: "))

    confirm = input(f"\nYou have said that you want to play with "
                    f"${initial_payment}\n"
                    f"please confirm that you want to play with $"
                    f"{initial_payment}\n"
                    f"enter Y for yes and N for no: ").lower()

#main script

#generate token

print (f"="*40)
Generate_token = input(f"You have ${initial_payment} left\n"
       f"would you like to buy a token?\n" 
       f"press Y to generate Token\n" 
       f"press anything else to end and leave with your money\n\n"
               f"Play?: ").upper()

while Generate_token == "Y" and Cash >= 1:
    Cash = Cash-1

    for item in range(1):
        token = random.choice(Tokens)
    print(token, end="\t")

    print(f"Congrats!\n"
          f"Your Token is a {token}")
    if token == "Unicorn":
        print("This means YOU WIN 5$")
        Cash = Cash+5

    elif token == "Donkey":
        print("This means YOU WIN NOTHING")

    else:
        print("This means YOU WIN 50c")
        Cash = Cash+0.5

    Generate_token = "stopped"

