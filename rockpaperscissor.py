import random

player = input("rock, paper, scissor: ")

opponent =["rock","paper", "scissor"]
opponent = random.choice(opponent)
print("opponent: "+ opponent)

if player == "rock" and opponent=="scissor":
    print("You won")
elif player == "scissor" and opponent=="paper":
    print("You won")
elif player == "paper" and opponent=="rock":
    print("You won")
elif player == "rock" and opponent=="paper":
    print("You lost")
elif player == "paper" and opponent=="scissor":
    print("You lost")
elif player == "scissor" and opponent=="rock":
    print("You lost")
else: print("Draw")
