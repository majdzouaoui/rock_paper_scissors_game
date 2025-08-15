import random 
import sys
user_wins = 0
computer_wins = 0
types = ["rock" , "paper" , "scissors", "end"]
while True:
    user_input = input("put your choise (rock , paper or scissors and end to exit) : ").lower()
    if user_input == "end":
        break
    elif user_input not in types:
        continue
    rval = random.randint(0,2)
    computer_input = types[rval]
    print("computer picked :",computer_input)
    if user_input == "rock" and computer_input == "scissors":
        print("you win")
        user_wins += 1
    elif user_input == "paper" and computer_input == "rock":
        print("you win")
        user_wins += 1
    elif user_input == "scissors" and computer_input == "paper":
        print("you win")
        user_wins += 1
    elif user_input == computer_input:
        print("no one wins")
    else :
        print("you lost") 
        computer_wins += 1
print(f"you win {user_wins} times and lost {computer_wins} times")    
print("goodbye") 
    
    
    
    
    
    