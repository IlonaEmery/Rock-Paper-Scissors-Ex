from random import choice



#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#



# ASK FOR USER INPUT
user_choice = input("Please choose one of: Rock, Paper, Scissors?")

print("user chose:",user_choice)

# VALIDATIONS
options = ["rock", "paper", "scissors"]
if user_choice not in options :
    print ("Please choose between rock, paper or scissors")
    exit ()
    
# COMPUTER CHOICE
# computer_choice=random.choice(options)
computer_choice = choice(options)
print("computer_choice: ", computer_choice)

# DETERMINE THE WINNER
#option a) nested IF statements
# taken from Eugenie on Slack

if user_choice == computer_choice:
    print("Both players played", user_choice, "It's a tie!")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("Paper covers rock. You won!")
    else:
        print("Scissors cuts paper. You lost! It's ok.")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("Scissors cuts paper. You won!")
    else:
        print("Rock crushes scissors. You lost! It's ok.")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("Rock crushes scissors. You won!")
    else:
        print("Paper covers rock You lost! It's ok.")


# FINAL RESULT
print("Thank you for playing! See you soon.")

