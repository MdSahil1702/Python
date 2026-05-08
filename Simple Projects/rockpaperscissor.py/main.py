import random
print("===========WELCOME TO ROCK PAPER SCISSOR GAME===========")


user_select= int(input("Select 1.Rock\n 2.Paper\n 3.Scissor\n"))
user_select=converToString(user_select)
computer_select= random.choice(["Rock","Paper","Scissor"])



    
def converToString(userinput):
    if userinput==1:
        return "Rock"
    elif userinput==2:
        return "Paper"
    return "Scissor"

