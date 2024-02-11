from random import randint

# Guess The Number Game
highEnd = 100
compGuess = randint(0,highEnd)
global luck
# Guess The Number
def guess():
    return int(input(f'Enter Your Guess Between 0 - {highEnd}: '))

# Comparison Guess And Number
def compareGuess(userGuess,compGuess):
    luck = 5
    while luck != 0:
        if luck == 0:
            print("Out of luck.")
            break
        if userGuess == compGuess:
            print("You win congralutitons.")
            break
        elif compGuess > int(userGuess):
            userGuess = int(input("Try Again, Your Guess Must Be Higher: "))
            luck -= 1
        elif compGuess < int(userGuess):
            userGuess = int(input("Try Again, Your Guess Must Be Lower: "))
            luck -= 1

print(compGuess)
compareGuess(guess() , compGuess)