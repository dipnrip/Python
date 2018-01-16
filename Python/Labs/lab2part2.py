from random import *
end = 1
choice = ["rock","paper","scissor"]
computer = choice[randint(0,2)]
print("Any deviation from the available choices will result in termination.")
while end > 0:
    user = input("rock,paper,scissor: ")
    if user == computer:
        print("Tie")
    elif user == "rock":
        if computer == "paper":
            print("Computer wins")
        else:
            print("You win")
    elif user == "paper":
        if computer == "scissors":
            print("You lose")
        else:
            print("You win")
    elif user == "scissor":
        if computer == "rock":
            print("You lose")
        else:
            print("You win")
    else:
        end = -1
        print("Good bye")
    computer = choice[randint(0,2)]
