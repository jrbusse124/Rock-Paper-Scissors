import tkinter
import random
root = tkinter.Tk()
 
lbl = tkinter.Label(root)
lbl['text'] = "Please make a selection"
lbl['width'] = 30
lbl.grid(row=0, column=1)
 
options = ["rock", "paper", "scissors"]
 
 
def computerChoice():
    global comp
    comp = random.choice(options)
    return comp
 
compScore = 0
userScore = 0
ties = 0
 
computerScore = tkinter.Label(root)
computerScore['text'] = "Computer Score: " + str(compScore)
computerScore.grid(row=3, column=1)
 
userScoreLbl = tkinter.Label(root)
userScoreLbl['text'] = "Your Score: " + str(userScore)
userScoreLbl.grid(row=4, column=1)
 
tieLbl = tkinter.Label(root)
tieLbl['text'] = "Ties: " + str(ties)
tieLbl.grid(row=5, column=1)
 
def tie():
    global ties
    lbl['text'] = "YOU TIE: Computer chose " + comp;
    ties += 1;
    tieLbl = tkinter.Label(root)
    tieLbl['text'] = "Ties: " + str(ties)
    tieLbl.grid(row=5, column=1)
 
def userWin():
    global userScore
    lbl['text'] = "YOU WIN: Computer chose " + comp;
    userScore += 1;
    userScoreLbl = tkinter.Label(root)
    userScoreLbl['text'] = "Your Score: " + str(userScore)
    userScoreLbl.grid(row=4, column=1)
 
def compWin():
    global compScore
    lbl['text'] = "YOU LOSE: Computer chose " + comp;
    compScore += 1;
    computerScore = tkinter.Label(root)
    computerScore['text'] = "Computer Score: " + str(compScore)
    computerScore.grid(row=3, column=1)
 
def rock():
    computerChoice()
    if comp == "rock":
        tie()
    elif comp == "paper":
        compWin()
    else:
        userWin()
 
def paper():
    computerChoice()
    if comp == "paper":
        tie()
    elif comp == "scissors":
        compWin()
    else:
        userWin()
 
 
def scissors():
    computerChoice()
    if comp == "scissors":
        tie()
    elif comp == "rock":
        compWin()
    else:
        userWin()
 
 
rockbtn = tkinter.Button(root)
rockbtn['text'] = "Rock"
rockbtn['width'] = 15
rockbtn['height'] = 7
rockbtn['highlightbackground'] = "gray"
rockbtn['command'] = rock
rockbtn.grid(row=1, column=0)
 
paperbtn = tkinter.Button(root)
paperbtn['text'] = "Paper"
paperbtn['width'] = 15
paperbtn['height'] = 7
paperbtn['highlightbackground'] = "white"
paperbtn['command'] = paper
paperbtn.grid(row=1, column=1)
 
scissorsbtn = tkinter.Button(root)
scissorsbtn['text'] = "Scissors"
scissorsbtn['width'] = 15
scissorsbtn['height'] = 7
scissorsbtn['highlightbackground'] = "blue"
scissorsbtn['command'] = scissors
scissorsbtn.grid(row=1, column=2)
 
 
root.mainloop()
