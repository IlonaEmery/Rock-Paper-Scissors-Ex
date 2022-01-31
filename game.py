import random



#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#




# ASK FOR USER INPUT
u = input("Please choose one of: Rock, Paper, Scissors?")

print("user chose:",u)

# VALIDATIONS
options = ["rock", "paper", "scissors"]
if u not in options :
    print ("Please choose between rock, paper or scissors")
    exit ()
    
# COMPUTER CHOICE
computer_choice = random.choice(options)
print("computer_choice: ", computer_choice)

# DETERMINE THE WINNER


# FINAL RESULT