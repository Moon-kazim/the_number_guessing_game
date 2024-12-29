import random
import art
    
easy_level = 10
hard_level = 5

def level():
    level = input("Choose a difficulty. Type 'easy' or 'hard'! \n".lower())
    if level == "easy":
        print("You have total 10 life!")
        print("")
        return easy_level
    elif level == "hard":
        print("You have total 5 life!")
        print("")
        return hard_level
    else:
        return "INVALID ENTRY!!!"
    
def compare(user_guess, random_number, life):
    if user_guess == random_number:
        print(f"You got it! The answer is {user_guess}")
    elif user_guess > random_number:
        print("TOO high")
        return life-1
    elif user_guess < random_number:
        print("TOO low")
        return life-1

def game():
    print("welcome to Guess The number game!".title())
    print(art.logo)
    print("")
    print("I'm thinking of a number between 1 and 100.")
    numbers = list(range(1, 101))
    numb = random.choice(numbers)
    print(numb)  
    turns = level()
    
    guess= 0

    while guess !=numb:

        print(f"Your {turns} turns remaining to guess the number")

        guess = int(input("Make a guess: "))
        turns = compare(user_guess=guess, random_number=numb, life=turns)
        
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return 
        elif guess != numb:
            print("Guess again.")

game()