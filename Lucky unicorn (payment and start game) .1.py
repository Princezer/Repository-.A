# welcome to game
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

# how much do you want to play with?

initial_payment = int(input("\nHow much would you like to pay with?: "))

while initial_payment > 10 or initial_payment < 1:
    initial_payment = int(input("\nSorry\nthe number you put in is not a "
                                "valid payment price\n"
                                "remember, it must be less then $10\n\n"
                                "How much would you like to play with?: "))

print (f"{initial_payment}")