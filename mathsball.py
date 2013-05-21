## This code Copyright (C) 2013 to Jeff Plumb
##
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.


import time
import random
from tkinter import *

P1GOAL = -1
P2GOAL = 1

class Ball:
    def __init__(self, canvas, direction, color):
        self.canvas = canvas
        self.id = canvas.create_oval(380, 280, 420, 320
                                   , outline = "black"
                                   , fill    = "blue"
                                   , width   = 2)
        self.direction = direction


    def move(self):
        self.canvas.move(self.id, self.direction, 0)
        pos = self.canvas.coords(self.id)
        if self.direction == P1GOAL and pos[0] <= 100:
            return 'goal'
        elif self.direction == P2GOAL and pos[2] >= 700:
            return 'goal'
        else:
            return 'play'

    def changeDirection(self):
        if self.direction == P1GOAL:
            self.direction = P2GOAL
        else:
            self.direction = P1GOAL

class Player:
    def __init__(self, player_name, type, level):
        self.player_name = player_name
        self.type = type
        self.updateLevel(level)
        self.goals = 0
        self.wins = 0
        self.correct = 0
        self.incorrect = 0

    def updateLevel(self, level):
        self.level = level
        if level == "Padawan":
           self.delay = 0.03
           self.answercycleodds = 150
           self.answerwrongpct = 10
        elif level == "Jedi Knight":
           self.delay = 0.02
           self.answercycleodds = 100
           self.answerwrongpct = 5
        elif level == "Jedi Master":
           self.delay = 0.01
           self.answercycleodds = 50
           self.answerwrongpct = 1
        else:
            self.delay = 0.03
        
    def computerAnswer(self):
        rnd = random.randint(1, self.answercycleodds)
        if rnd == 1:
            x = random.randint(1, 100)
            if x <= self.answerwrongpct:
                self.incorrect += 1
                game.gamestate = 'goal'
            else:
                self.correct += 1
                ball.changeDirection()
                question.clearOptions()
                question.getQuestion()
                question.showOptions()

class GameState:
    def __init__(self, gamestate):
        self.gamestate = gamestate
    
class playerOptions:
    def __init__(self, canvas, game):
        canvas.delete(ALL)
        self.p1name = Entry(tk)
        self.p1name.pack(side = "left")
        self.p1nametext = StringVar()
        self.p1nametext.set(player1.player_name)
        self.p1name["textvariable"] = self.p1nametext

        self.p1typeVar = StringVar()
        self.p1typeVar.set(player1.type)
        self.p1typeOptionMenu = OptionMenu(tk, self.p1typeVar, "Human", "Computer")
        self.p1typeOptionMenu.pack(side = "left")

        self.p1levelVar = StringVar()
        self.p1levelVar.set(player1.level)
        self.p1levelOptionMenu = OptionMenu(tk, self.p1levelVar, "Padawan", "Jedi Knight", "Jedi Master")
        self.p1levelOptionMenu.pack(side = "left")

        self.p2name = Entry(tk)
        self.p2name.pack(side = "left")
        self.p2nametext = StringVar()
        self.p2nametext.set(player2.player_name)
        self.p2name["textvariable"] = self.p2nametext

        self.p2typeVar = StringVar()
        self.p2typeVar.set(player2.type)
        self.p2typeOptionMenu = OptionMenu(tk, self.p2typeVar, "Human", "Computer")
        self.p2typeOptionMenu.pack(side = "left")

        self.p2levelVar = StringVar()
        self.p2levelVar.set(player2.level)
        self.p2levelOptionMenu = OptionMenu(tk, self.p2levelVar, "Padawan", "Jedi Knight", "Jedi Master")
        self.p2levelOptionMenu.pack(side = "left")

        self.saveBut = Button(tk, text="Start Game", command=self.setOptions, width=10)
        self.saveBut.pack(side = "left")
    def getSelection(self):
        while game.gamestate == "options":
            tk.update()
        self.p1name.destroy()
        self.p2name.destroy()
        self.p1typeOptionMenu.destroy()
        self.p2typeOptionMenu.destroy()
        self.p1levelOptionMenu.destroy()
        self.p2levelOptionMenu.destroy()
        self.saveBut.destroy()

    def setOptions(self):
        player1.player_name = self.p1nametext.get()
        player2.player_name = self.p2nametext.get()
        player1.type = self.p1typeVar.get()
        player2.type = self.p2typeVar.get()
        player1.updateLevel(self.p1levelVar.get())
        player2.updateLevel(self.p2levelVar.get())
        game.gamestate = "play"

def drawField(canvas):
    canvas.create_rectangle(100, 100, 700, 500, fill='green')
    canvas.create_rectangle(100, 250, 150, 350)
    canvas.create_rectangle(650, 250, 700, 350)
    canvas.create_rectangle(100, 175, 200, 425)
    canvas.create_rectangle(600, 175, 700, 425)
    canvas.create_line(400,100, 400, 500)
    canvas.create_arc(360,260,440, 340, extent=359, style=ARC)
    scoreTextStr = player1.player_name + "(" + player1.level + "): " + str(player1.goals) + " " + player2.player_name + "(" + player2.level + "): " + str(player2.goals) 
    scoreText = canvas.create_text(400, 550
                                   , text=scoreTextStr
                                   , fill='blue'
                                   , font=('Times', 20))
    tk.update()

def splashScreen(canvas):
    mathsText = canvas.create_text(400, 200
                                   , text='Maths Ball'
                                   , fill='blue'
                                   , font=('Times', 100))
    tk.update()
    time.sleep(0.1)
    canvas.itemconfig(mathsText, fill='red')
    tk.update()
    time.sleep(0.1)
    canvas.itemconfig(mathsText, fill='green')
    tk.update()
    time.sleep(0.1)
    canvas.itemconfig(mathsText, fill='blue')
    tk.update()
    time.sleep(0.1)
    canvas.delete(mathsText)

def showMenu(canvas):
    canvas.delete(ALL)
    menuText = canvas.create_text(400, 200
                                   , text='x->exit, any key->start'
                                   , fill='blue'
                                   , font=('Times', 50))
    while game.gamestate == "menu":
        tk.update()


class Question:
    def __init__(self, canvas):
        self.canvas = canvas
        
    def getQuestion(self):
        self.num1 = random.randint(1, 12)
        self.num2 = random.randint(1, 12)
        self.ans = self.num1 * self.num2
        self.questionString = str(self.num1) + ' * ' + str(self.num2)
        self.questionText = self.canvas.create_text(400, 50
                                     , text=self.questionString
                                     , fill='blue'
                                     , font=('Times', 50))
        tk.update()

    def showOptions(self):
        ans_option_int = random.randint(1, 4)
        if ball.direction == P1GOAL:
            ypos = 50
        else:
            ypos = 750
        
        ans1 = self.ans
        if ball.direction == P1GOAL:
            option_char = 'q'
        else:
            option_char = 'o'
        if ans_option_int == 1:
            self.answer_char = option_char
            ansText = option_char + ': ' + str(self.ans)
        else:
            while ans1 == self.ans:
                ans1 = (self.ans - 6) + random.randint(1, 11)
            ansText = option_char + ': ' + str(ans1)
        self.op1 = self.canvas.create_text(ypos, 100, text=ansText, fill='green', font=('Times', 25))

        ans2 = self.ans
        if ball.direction == P1GOAL:
            option_char = 'a'
        else:
            option_char = 'k'
        if ans_option_int == 2:
            self.answer_char = option_char
            ansText = option_char + ': ' + str(self.ans)
        else:
            while ans2 == self.ans or ans2 == ans1:
                ans2 = (self.ans - 6) + random.randint(1, 11)
            ansText = option_char + ': ' + str(ans2)
        self.op2 = self.canvas.create_text(ypos, 200, text=ansText, fill='green', font=('Times', 25))

        ans3 = self.ans
        if ball.direction == P1GOAL:
            option_char = 'z'
        else:
            option_char = 'm'
        if ans_option_int == 3:
            self.answer_char = option_char
            ansText = option_char + ': ' + str(self.ans)
        else:
            while ans3 == self.ans or ans3 == ans1 or ans3 == ans2:
                ans3 = (self.ans - 6) + random.randint(1, 11)
            ansText = option_char + ': ' + str(ans3)
        self.op3 = self.canvas.create_text(ypos, 300, text=ansText, fill='green', font=('Times', 25))

        ans4 = self.ans
        if ball.direction == P1GOAL:
            option_char = 'x'
        else:
            option_char = 'n'
        if ans_option_int == 4:
            self.answer_char = option_char
            ansText = option_char + ': ' + str(self.ans)
        else:
            while ans4 == self.ans or ans4 == ans1 or ans4 == ans3 or ans4 == ans3:
                ans4 = (self.ans - 6) + random.randint(1, 11)
            ansText = option_char + ': ' + str(ans4)
        self.op4 = self.canvas.create_text(ypos, 400, text=ansText, fill='green', font=('Times', 25))

    def clearOptions(self):
        self.canvas.delete(self.questionText)
        self.canvas.delete(self.op1)
        self.canvas.delete(self.op2)
        self.canvas.delete(self.op3)
        self.canvas.delete(self.op4)

def showGoal(canvas):
    goalText = canvas.create_text(400, 200
                                  , text='Goal'
                                  , fill='blue'
                                  , font=('Times', 100))
    tk.update()
    time.sleep(1)
    canvas.itemconfig(goalText, fill='red')
    tk.update()
    time.sleep(1)
    canvas.itemconfig(goalText, fill='green')
    tk.update()
    time.sleep(1)
    canvas.itemconfig(goalText, fill='blue')
    tk.update()
    time.sleep(1)
    canvas.delete(goalText)

def winningScreen(player):
    winningMessage = 'Congratulations ' + player.player_name + '! You Win!'
    winningText = canvas.create_text(400, 200,
                                     text=winningMessage
                                     , fill='blue'
                                     , font=('Times', 50))
    tk.update()
    time.sleep(1)
    canvas.itemconfig(winningText, fill='red')
    tk.update()
    time.sleep(1)
    canvas.itemconfig(winningText, fill='green')
    tk.update()
    time.sleep(1)
    canvas.itemconfig(winningText, fill='blue')
    tk.update()
    time.sleep(1)
    canvas.delete(winningText)

def showStats(canvas, player1, player2):
    canvas.delete(ALL)
    player1Message = player1.player_name + ' you won ' + str(player1.wins) + ' games'
    player1Text = canvas.create_text(400, 200
                                     , text=player1Message
                                     , fill='blue'
                                     , font=('Times', 25))
    player1Stats = 'You got ' + str(player1.correct) + ' questions correct and ' + str(player1.incorrect) + ' wrong'
    player1StatsText = canvas.create_text(400, 250
                                     , text=player1Stats
                                     , fill='blue'
                                     , font=('Times', 20))
    player2Message = player2.player_name + ' you won ' + str(player2.wins) + ' games'
    player2Text = canvas.create_text(400, 400
                                     , text=player2Message
                                     , fill='green'
                                     , font=('Times', 25))
    player2Stats = 'You got ' + str(player2.correct) + ' questions correct and ' + str(player2.incorrect) + ' wrong'
    player2StatsText = canvas.create_text(400, 450
                                     , text=player2Stats
                                     , fill='green'
                                     , font=('Times', 20))
    tk.update()
    time.sleep(10)
    canvas.delete(player1Text)
    canvas.delete(player2Text)

def checkKeys(event):
    if game.gamestate == 'play':
        if ((ball.direction == P1GOAL and
             player1.type == 'Human' and
            (event.keysym == 'q'
                or event.keysym == 'a'
                or event.keysym == 'z'
                or event.keysym == 'x')) or
            (ball.direction == P2GOAL and
             player2.type == 'Human' and
            (event.keysym == 'o'
                or event.keysym == 'k'
                or event.keysym == 'm'
                or event.keysym == 'n'))):
            question.clearOptions()
            if event.keysym == question.answer_char:
                if ball.direction == P1GOAL:
                    player1.correct += 1
                else:
                    player2.correct += 1
                ball.changeDirection()
                question.getQuestion()
                question.showOptions()
            else:
                if ball.direction == P1GOAL:
                    player1.incorrect += 1
                else:
                    player2.incorrect += 1
                game.gamestate = 'goal'
    elif game.gamestate == 'menu':
        if event.keysym == 'x' or event.keysym == 'X':
            game.gamestate = 'exit'
        else:
            game.gamestate = 'play'

        
 
# Main Program
tk = Tk()
tk.title("Maths Ball")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=800, height=600, bd=0, highlightthickness=0)
canvas.pack()
splashScreen(canvas)

game = GameState("options")
question = Question(canvas)

player1 = Player('Josh', 'Human', 'Padawan')
player2 = Player('Darth Vader', 'Computer', 'Padawan')
po = playerOptions(canvas, game)
po.getSelection()

canvas.bind_all('<Key>', checkKeys)

# Main Loop
while game.gamestate != 'exit':
    if game.gamestate == 'menu':
        showMenu(canvas)
    if game.gamestate == 'play':
        canvas.delete(ALL)
        while player1.goals < 3 and player2.goals < 3:
            drawField(canvas)
            ball = Ball(canvas, P1GOAL, 'blue')
            question.getQuestion()
            question.showOptions()
            while game.gamestate != 'goal':
                game.gamestate = ball.move()
                tk.update_idletasks()
                tk.update()
                if ball.direction == P1GOAL:
                    time.sleep(player1.delay)
                    if player1.type == 'Computer':
                        player1.computerAnswer()
                else:
                    time.sleep(player2.delay)
                    if player2.type == 'Computer':
                        player2.computerAnswer()
            canvas.delete(ALL)
            showGoal(canvas)
            if ball.direction == P1GOAL:
                player2.goals += 1
                canvas.move(ball.id, 280, 0)
                ball.changeDirection()
            elif ball.direction == P2GOAL:
                player1.goals += 1
                canvas.move(ball.id, -280, 0)
                ball.changeDirection()
            game.gamestate = 'play'
        if player1.goals == 3:
             player1.wins += 1
             winningScreen(player1)
        elif player2.goals == 3:
             player2.wins += 1
             winningScreen(player2)
        player1.goals = 0
        player2.goals = 0
        game.gamestate = 'menu'

    showMenu(canvas)
    
showStats(canvas, player1, player2)
tk.destroy()
