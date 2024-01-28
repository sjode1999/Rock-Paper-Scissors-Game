import random
import sys
import time


print("Hello Welcome to Rock, Paper, Scissors Game.")


def player_choice():
    while True:
        user_choice = input("Make a selection: Rock, Paper, Scissors: ")
        if user_choice in ["Rock", "Paper", "Scissors"]:
            return user_choice
        else:
            print("Please Enter a Valid Seleciton")
            continue

def opponent_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a TIE!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        return "YOU WIN"
    else:
        return "LOSER!"

def game():
    user_choice = player_choice()
    computer_choice = opponent_choice()

    print("Rock")
    time.sleep(0.5)
    print("Paper")
    time.sleep(0.5)
    print("Scissors")
    time.sleep(0.5)
    print("GO!!!")
    time.sleep(0.5)

    print(f"You Chose {user_choice}.")
    print(f"Your opponent Chose {computer_choice}.")


    results = winner(user_choice, computer_choice)
    print(results)


if __name__ == "__main__":
    while True:
        game()
        another_attempt = input('Would you like to try again (Y/N): ')
        if another_attempt.upper() == 'N':
            print("Thanks for playing")
            sys.exit()
        elif another_attempt.upper() == 'Y':
            continue
        else:
            print("Invalid Selection!!! Try Again")








