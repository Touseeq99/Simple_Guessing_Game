# Guessing__game
import random

num = int(input("Guess The Number = "))
jackpot = random.randint(0, 250000)
counter = 0
while True:
    counter = counter + 1
    if num == jackpot:
        print("Enter Number is Correct")
        break
    elif num > jackpot:
        print("Guess Lower")
        num = int(input("Guess The Number = "))
    
    elif num < jackpot:
        print("Guess Higher")
        num = int(input("Guess The Number = "))
    
    else:
        print("Out Of bound")

print("You took ", counter, "too Guess")

