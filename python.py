import random 

number = random.randint(1,100)
attempts = 0


while True:    
    guess = int(input("Guess a number between 1 and 100:"))
    attempts = attempts + 1
    
    if guess == number:
        print("Correct! You win!")
        print("Your attempts:",attempts)
        break 
    elif guess > number:
        print("Too high! try a smaller number.")
    else:
        print("Too low! try a bigger number.")
    
    