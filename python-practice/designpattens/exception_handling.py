while True:
    try:
        num = int(input("Enter a number"))
        break
    except ValueError:
        print("You didn't enter a number")
    except:
        print("A unknown error occurred")
print("Thanks for entering a number")


# Cas2e
secrets_number = 7
while True:
    try:
        num = int(input("Guess a number between 1 to 10 "))
        if secrets_number == num:
            print("You Guessed it!! ")
            break
    except ValueError:
        print("Please enter only number ")


