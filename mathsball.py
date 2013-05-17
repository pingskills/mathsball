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

class Ball:
    def __init__(self, canvas, direction, color):
        self.canvas = canvas
        self.id = canvas.create_oval(380, 280, 420, 320
                                   , outline = "black"
                                   , fill    = "blue"
                                   , width   =2)
        self.direction = direction


    def move(self):
        self.canvas.move(self.id, self.direction, 0)
        pos = self.canvas.coords(self.id)
        if self.direction == -1 and pos[0] <= 100:
            return 'goal'
        elif self.direction == 1 and pos[2] >= 700:
            return 'goal'
        else:
            return 'play'

    def changeDirection(self):
        if self.direction == 1:
            self.direction = -1
        else:
            self.direction = 1

class Player:
    def __init__(self, player_name):
        self.player_name = player_name
        self.goals = 0
        self.wins = 0

class GameState:
    def __init__(self, gamestate):
        self.gamestate = gamestate
    

def drawField(canvas):
    canvas.create_rectangle(100, 100, 700, 500, fill='green')
    canvas.create_rectangle(100, 250, 150, 350)
    canvas.create_rectangle(650, 250, 700, 350)
    canvas.create_rectangle(100, 175, 200, 425)
    canvas.create_rectangle(600, 175, 700, 425)
    canvas.create_line(400,100, 400, 500)
    canvas.create_arc(360,260,440, 340, extent=359, style=ARC)
    tk.update()

def splashScreen(canvas):
    mathsText = canvas.create_text(400, 200
                                   , text='Maths Ball'
                                   , fill='blue'
                                   , font=('Times', 100))
    tk.update()
    time.sleep(1)
    canvas.itemconfig(mathsText, fill='red')
    tk.update()
    time.sleep(1)
    canvas.itemconfig(mathsText, fill='green')
    tk.update()
    time.sleep(1)
    canvas.itemconfig(mathsText, fill='blue')
    tk.update()
    time.sleep(1)
    canvas.delete(mathsText)

def showMenu(canvas):
    menuText = canvas.create_text(400, 200
                                   , text='x->exit, any key->start'
                                   , fill='blue'
                                   , font=('Times', 50))
    tk.update()


def getQuestion():
   num1 = random.randint(1, 12)
   num2 = random.randint(1, 12)
   ans = num1 * num2
   questionString = str(num1) + ' * ' + str(num2)
   questionText = canvas.create_text(400, 50
                                     , text=questionString
                                     , fill='blue'
                                     , font=('Times', 50))
   tk.update()
   return (ans, questionText)

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

def showStats(player1, player2):
    player1Message = player1.player_name + ' you won ' + str(player1.wins) + ' games'
    player1Text = canvas.create_text(400, 200
                                     , text=player1Message
                                     , fill='blue'
                                     , font=('Times', 25))
    player2Message = player2.player_name + ' you won ' + str(player2.wins) + ' games'
    player2Text = canvas.create_text(400, 400
                                     , text=player2Message
                                     , fill='green'
                                     , font=('Times', 25))
    tk.update()
    time.sleep(10)
    canvas.delete(player1Text)
    canvas.delete(player2Text)

def checkKeys(event):
    global game, ans, answer_char, questionText, op1, op2, op3, op4
    if game.gamestate == 'play':
        if ((ball.direction == -1 and
            (event.keysym == 'q'
                or event.keysym == 'a'
                or event.keysym == 'z'
                or event.keysym == 'x')) or
            (ball.direction == 1 and
            (event.keysym == 'o'
                or event.keysym == 'k'
                or event.keysym == 'm'
                or event.keysym == 'n'))):
            canvas.delete(questionText)
            canvas.delete(op1)
            canvas.delete(op2)
            canvas.delete(op3)
            canvas.delete(op4)
            if event.keysym == answer_char:
                ball.changeDirection()
                ans, questionText = getQuestion()
                answer_char, op1, op2, op3, op4 = showOptions()
            else:
                game.gamestate = 'goal'
    elif game.gamestate == 'menu':
        if event.keysym == 'x' or event.keysym == 'X':
            game.gamestate = 'exit'
        else:
            game.gamestate = 'play'

def showOptions():
    ans_option_int = random.randint(1, 4)
    if ball.direction == -1:
        ypos = 50
    else:
        ypos = 750
        
    num1 = ans
    if ball.direction == -1:
        option_char = 'q'
    else:
        option_char = 'o'
    if ans_option_int == 1:
        answer_char = option_char
        ansText = option_char + ': ' + str(ans)
    else:
        while num1 == ans:
            num1 = (ans - 6) + random.randint(1, 11)
        ansText = option_char + ': ' + str(num1)
    op1 = canvas.create_text(ypos, 100, text=ansText, fill='green', font=('Times', 25))

    num2 = ans
    if ball.direction == -1:
        option_char = 'a'
    else:
        option_char = 'k'
    if ans_option_int == 2:
        answer_char = option_char
        ansText = option_char + ': ' + str(ans)
    else:
        while num2 == ans or num2 == num1:
            num2 = (ans - 6) + random.randint(1, 11)
        ansText = option_char + ': ' + str(num2)
    op2 = canvas.create_text(ypos, 200, text=ansText, fill='green', font=('Times', 25))

    num3 = ans
    if ball.direction == -1:
        option_char = 'z'
    else:
        option_char = 'm'
    if ans_option_int == 3:
        answer_char = option_char
        ansText = option_char + ': ' + str(ans)
    else:
        while num3 == ans or num3 == num1 or num3 == num2:
            num3 = (ans - 6) + random.randint(1, 11)
        ansText = option_char + ': ' + str(num3)
    op3 = canvas.create_text(ypos, 300, text=ansText, fill='green', font=('Times', 25))

    num4 = ans
    if ball.direction == -1:
        option_char = 'x'
    else:
        option_char = 'n'
    if ans_option_int == 4:
        answer_char = option_char
        ansText = option_char + ': ' + str(ans)
    else:
        while num4 == ans or num4 == num1 or num4 == num2 or num4 == num3:
            num4 = (ans - 6) + random.randint(1, 11)
        ansText = option_char + ': ' + str(num4)
    op4 = canvas.create_text(ypos, 400, text=ansText, fill='green', font=('Times', 25))

    return (answer_char, op1, op2, op3, op4)
        
 
# Main Program
tk = Tk()
tk.title("Maths Ball")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=800, height=600, bd=0, highlightthickness=0)
canvas.pack()
splashScreen(canvas)

game = GameState('menu')
canvas.bind_all('<Key>', checkKeys)
showMenu(canvas)
while game.gamestate == 'menu':
    tk.update()
canvas.delete(ALL)

player1 = Player('Jeff')
player2 = Player('Josh')
direction = -1

# Main Loop
while game.gamestate != 'exit':
    while player1.goals < 3 and player2.goals < 3:
        drawField(canvas)
        ball = Ball(canvas, direction, 'blue')
        ans, questionText = getQuestion()
        (answer_char, op1, op2, op3, op4) = showOptions()
        while game.gamestate != 'goal':
            game.gamestate = ball.move()
            tk.update_idletasks()
            tk.update()
            time.sleep(0.01)
        canvas.delete(ALL)
        showGoal(canvas)
        if ball.direction == -1:
            player2.goals += 1
            canvas.move(ball.id, 280, 0)
            direction = 1
        elif ball.direction == 1:
            player1.goals += 1
            canvas.move(ball.id, -280, 0)
            direction = -1
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
    while game.gamestate == 'menu':
        tk.update()
    canvas.delete(ALL)
    
showStats(player1, player2)
tk.destroy()
