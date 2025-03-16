import random
print(r'''
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ' _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|        
''')
def game(user,com):
    if user < com:
        print("Too low.")
        return True
    elif user > com:
        print("Too high.")
        return True
    else:
        print(f"You got it! The answer was {com}.")
        return False
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
c_num = random.randint(1,100)
mode =input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if mode == "easy":
    print("You have 10 attempts remaining to guess the number.")
    chance  = 10
else:
    print("You have 5 attempts remaining to guess the number.")
    chance = 5
choice = chance
state = True
while chance > 0 and state == True:
    if choice == chance:
        u_guess = int(input("Make a guess: "))
    else:
        u_guess = int(input("Guess again: "))
    state = game(u_guess,c_num)
    chance -=  1
    if state:
        print(f"You have {chance} attempts remaining")
if state:
    print("You've run out of guesses. Refresh the page to run again.")
