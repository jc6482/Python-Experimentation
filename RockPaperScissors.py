#Juan Carlos Ramirez
#A Rock Paper Scissors game created with Python

import numpy

def resultFromUserInput(input,choices):
    if choices.__contains__(input):
        return choices[numpy.random.randint(0,high=choices.__len__())]
    else:
        return input



choices = ["rock","scissors","paper"]
playerPoints = 0
compPoints = 0
while(True):

    userInput = raw_input("Rock/Paper/Scissors/Quit?: ").lower()
    computerChoice = resultFromUserInput(userInput, choices)

    if computerChoice == "quit":
        quit()
    elif choices.__contains__(computerChoice):
        if choices.index(userInput) == choices.index(computerChoice):
            print "It's a tie!"
        elif choices.index(userInput) == (choices.index(computerChoice) - 1) % 3:
            print "User Wins"
            playerPoints += 1
        else:
            print "Computer Wins"
            compPoints += 1

        print "Player: " + playerPoints.__str__() + " vs. Computer: " + compPoints.__str__()
    else:
        print "That's not an option"

