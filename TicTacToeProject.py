from tkinter import *
import random
import time

#Function to switch players if there is no winner
def NextTurn(row, column):
    
    global Player
    global SetTime
    global TimeLimit
    global Count

    if Buttons[row][column]['text'] == "" and CheckWinner() is False:

        if Player == Players[0]:

            Buttons[row][column]['text'] = Player

            if CheckWinner() is False:
                Player = Players[1]
                WhosTurn.config(text = Players[1] + " To Move")
                SetTime = TimeLimit
                CountDown.config(text = "Time: " + str(round(SetTime,2)))
                Count = -1
                ComputerTurn()
            elif CheckWinner() is True:
                WhosTurn.config(text = Players[0] + " Wins!")
                Count = 0
            elif CheckWinner() == "Tie":
                WhosTurn.config(text = "Tie!")
                Count = 0

#Function for the computer to make a move
def ComputerTurn():

    global Player
    global SetTime
    global TimeLimit
    global Count

    if Player == Players[1]:
        while Player == Players[1]:
            row = random.randint(0,2)
            column = random.randint(0,2)
            if Buttons[row][column]['text'] == "":
                Buttons[row][column]['text'] = Player
                break
        if CheckWinner() is False:
            Player = Players[0]
            WhosTurn.config(text = Players[0] + " To Move")
            SetTime = TimeLimit
            CountDown.config(text = "Time: " + str(round(SetTime,2)))
            Count = -1
        elif CheckWinner() is True:
            WhosTurn.config(text = Players[1] + " Wins!")
            Count = 0
        elif CheckWinner() == "Tie":
            WhosTurn.config(text = "Tie!")
            Count = 0

#Function to skip a players turn
def SkipTurn():
    global Player
    global SetTime
    global TimeLimit
    SetTime = TimeLimit

    if CheckWinner() is False:
        if Player == Players[0]:
            Player = Players[1]
            ComputerTurn()
            CountDown.after(100,Timer)
        else:
            Player = Players[0]
            WhosTurn.config(text = Players[0] + " To Move")
            CountDown.config(text = "Time: " + str(round(SetTime,2)))
            CountDown.after(100,Timer)

#Function to check if there is a winner
def CheckWinner():
    
    for row in range(3):
        if Buttons[row][0]['text'] == Buttons[row][1]['text'] == Buttons[row][2]['text'] != "":
            Buttons[row][0].config(bg = "white", fg = "black")
            Buttons[row][1].config(bg = "white", fg = "black")
            Buttons[row][2].config(bg = "white", fg = "black")
            return True
    
    for column in range(3):
        if Buttons[0][column]['text'] == Buttons[1][column]['text'] == Buttons[2][column]['text'] != "":
            Buttons[0][column].config(bg = "white", fg = "black")
            Buttons[1][column].config(bg = "white", fg = "black")
            Buttons[2][column].config(bg = "white", fg = "black")
            return True

    if Buttons[0][0]['text'] == Buttons[1][1]['text'] == Buttons[2][2]['text'] != "":
        Buttons[0][0].config(bg = "white", fg = "black")
        Buttons[1][1].config(bg = "white", fg = "black")
        Buttons[2][2].config(bg = "white", fg = "black")
        return True

    elif Buttons[0][2]['text'] == Buttons[1][1]['text'] == Buttons[2][0]['text'] != "":
        Buttons[0][2].config(bg = "white", fg = "black")
        Buttons[1][1].config(bg = "white", fg = "black")
        Buttons[2][0].config(bg = "white", fg = "black")
        return True
    
    elif EmptySpaces() is False:

        for row in range(3):
            for column in range(3):
                Buttons[row][column].config(bg = "white", fg = "black")
        return "Tie"
    
    else: 
        return False

#Function to check if any possible moves remain
def EmptySpaces():

    spaces = 9

    for row in range(3):
        for column in range(3):
            if Buttons[row][column]['text'] != "":
                spaces -= 1
    
    if spaces == 0: 
        return False
    else: 
        return True

#Function to start a new game
def NewGame():
    global Player
    global SetTime
    global Count
    Count = Count + 1

    if Count == 1:
        SetTime = TimeLimit
        Timer()
    elif CheckWinner() is True or CheckWinner() == "Tie":
        Timer()

    Player = random.choice(Players)
    WhosTurn.config(text = Player + " To Move")

    for row in range(3):
        for column in range(3):
            Buttons[row][column].config(text = "", bg = "black", fg = "white")
        
    ComputerTurn()

#Function to restart timer 
def RestartTimer():
    global Count 
    global SetTime 

    Count = 1
    SetTime = TimeLimit
    CountDown.config(text = "Time: " + str(round(SetTime,2)))
    CountDown.after(100, Timer)
    pass

#Function for time keeping 
def Timer():
    global SetTime
    global TimeLimit
    global Count

    if SetTime > 0 and Count == 1:
        SetTime -= 0.1
        CountDown.config(text = "Time: " + str(round(abs(SetTime),2)))
        CountDown.after(100, Timer)
    elif SetTime < 0:
        SkipTurn()
    elif Count > 1: 
        RestartTimer()
    elif Count < 0: 
        Count = 1
        CountDown.after(100, Timer)

#Function to switch between frames
def showframe(frame):
    frame.tkraise()

window = Tk()
window.title("Tic Tac Toe")
window.config(bg = "black")
Players = ["X","O"]
Player = random.choice(Players)
Buttons = [[0,0,0],[0,0,0],[0,0,0]]

#Constants used throughout code for timer 
TimeLimit = 1.0
SetTime = TimeLimit
Count = 0

#Setting up the start screen with a title and start button
StartScreen = Frame(window)
StartScreen.config(bg = "black")
StartScreen.grid(row = 0, column = 0, sticky = "nesw")

Title = Label(StartScreen, text = "Tic Tac Toe", font = ('gotham', 40), fg = "white")
Title.place(relx = 0.5, rely = 0.25, anchor = CENTER)
Title.config(bg = "black")

StartButton =  Button(StartScreen, text = "Start", font = ('gotham', 20), command = lambda:[showframe(GameScreen), NewGame()], fg = "white")
StartButton.place(relx = 0.5, rely = 0.65, anchor = CENTER)
StartButton.config(bg = "black")

#Setting up the game screen 
GameScreen = Frame(window)
GameScreen.grid(row = 0, column = 0, sticky = "nesw")

SmallTitle = Label(GameScreen, text = "Tic-Tac-Toe", font = ('gotham', 20), fg = "White")
SmallTitle.grid(row = 0, column = 4, stick = "nesw")
SmallTitle.config(bg = "black")

#Label showing which player needs to make a move
WhosTurn = Label(GameScreen, text = Player + " To Move", font = ('gotham', 30), fg = "white")
WhosTurn.grid(row = 0, column = 0, columnspan = 3, stick = "nesw")
WhosTurn.config(bg = "black")

#Label showing the amount of time left in a players turn
CountDown = Label(GameScreen, text = "Time: " + str(SetTime), font = ('gotham', 20), fg = "white")
CountDown.grid(row = 1, column = 4, stick = "nesw")
CountDown.config(bg = "black")

#Button to start a new game
RestartGame = Button(GameScreen, text = "Restart", font=("gotham", 20), fg = "white", command = lambda:[NewGame()])
RestartGame.grid(row = 2, column = 4, sticky = "nesw")
RestartGame.config(bg = "black")

#Button back to start screen 
MainMenu = Button(GameScreen, text = "Main Menu", font = ('gotham', 20), fg = "white", command = lambda:[showframe(StartScreen)])
MainMenu.grid(row = 3, column = 4, sticky = "nesw")
MainMenu.config(bg = "black")

#3X3 game board
for row in range(3):
    for column in range(3):
        Buttons[row][column] = Button(GameScreen, text = "", font = ("gotham",30), fg = "white", bg = "black", width = 5, height = 2, command = lambda row = row, column = column: NextTurn(row, column))
        Buttons[row][column].grid(row = row + 1, column = column)

showframe(StartScreen)

mainloop()