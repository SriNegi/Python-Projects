# Guess number 
import random
number_guess=random.randint(1,50)
attempt=0
user_guess=0

print("Welcome to the Number Guessing Game! ")
print("Guess a number between 1 and 50")

while user_guess != number_guess:
    user_guess=int(input())
    attempt +=1
    if user_guess>number_guess:
        print("Too High Try Again")
    elif user_guess<number_guess:
         print("Too Low Try Again")
    else :
        print(f"Congratulations you have guessed the number correct in {attempt} attempts")
