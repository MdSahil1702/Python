import random

def converToString(userinput):
    if userinput==1:
        return "rock"
    elif userinput==2:
        return "paper"
    return "scissor"


def win_loss(user,computer):
    if user=="rock" and computer=="paper":
        print("Computer Win!!")
    elif user=="paper" and computer=="Scissor":
        print("Computer Win!!")
    elif user=="scissor" and computer == "rock":
        print("Computer Win!!!")
    elif user==computer:
        print("Match Tie!!")
    else:
        print("You Win!!")




print("===========WELCOME TO ROCK PAPER SCISSOR GAME===========")



   
    
    

while 1:
    
    try:
        user_select= int(input("Select\n 1.Rock\n 2.Paper\n 3.Scissor\n 4.Exit\n"))
        if user_select==4:
            print("Exiting from the game\n")
            break
        user=converToString(user_select)
        computer_select= random.choice(["rock","paper","scissor"])
        win_loss(user,computer_select)
    
    except ValueError:
        print("You have entered an invalid number please enter the number between 1-4")
