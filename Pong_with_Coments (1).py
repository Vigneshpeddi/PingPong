#Week 10 Day 2 Vignesh Peddi Henry Cheng Adithya Dasarathi
#PONG

import turtle#We are importing the module turtle.
import os#We are importing the module os
print("V.H.A Corp. Copyright 2019")#We are outputtimg this statement 
print("Pong!")#We are also outputting this statement
print("\nWhat is Pong?")#Same as above
print("Pong was formerly A popular game created by the Atari Company in 1972. Pong has two options, a single player, and multiplayer gamemode. ")#Same as above
print("\nHow to Play Pong")
print("The main purpose of this game is to hit a ball around the screen; and avoid your opponent from repeling the ball. To win, the opponent you must acheive 10 points.")
shopkins = input("\n Play[Y/n]: ")#To ask if the user wants to play
shopkins2 = input("Do you Know how to play[Y/n]: ")#asking if the user knows how to play
if shopkins2 ==  "n":#The if statement will tell the user the controls if the answer is n
    print("Player A Controls: W and S\nPlayer B Controls: Up and Down arrows")
if shopkins == "Y":#If the user says Y the program will go straight through difficulty.
    answer = input("Choose Difficulty: Easy Hard Normal:  ")
    shopkins3 = 1
wn = turtle.Screen()#Creating a screen 
wn.title("Pong by Vignesh the Chicken God and Henry the Penguin God and Adithya the Tiger God")#We are making a title for the screen
wn.bgcolor("black")#The color for screen
wn.setup(width=800, height=600)#The measurement of the screen
wn.tracer(0)#trace affects
# Score
score_a = 0#The score displays on the screen
score_b = 0
# Paddle A
paddle_a = turtle.Turtle()#We are making the paddle
paddle_a.speed(0)
paddle_a.shape("square")#It is square 
paddle_a.color("white")#THe color is white
paddle_a.shapesize(stretch_wid=5, stretch_len=1)#The size of the paddle 
paddle_a.penup()#created paddle a 
paddle_a.goto(-350, 0)#Tell the paddle to go to the coordinate 
# Paddle B
paddle_b = turtle.Turtle()#Same as above
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)
# Ball
ball = turtle.Turtle()#We are making the ball
ball.speed(0)
ball.shape("circle")#The shape of the ball
ball.color("white")#The color of the ball
ball.penup()#created the ball
ball.goto(0, 0)#The coordinates it goes to
if answer == "Easy":#The speed of the ball depending on the difficulty
    ball.dx = .3
    ball.dy = -.3
elif answer == "Hard":
    ball.dx = .9
    ball.dy = -.9
elif answer == "Normal":
    ball.dx = .6
    ball.dy = -.6
# Pen
pen = turtle.Turtle()#Created the pen aka place to write text
pen.speed(0)
pen.color("white")#The color of text
pen.penup()#created the text
pen.hideturtle()#To hide the pen
pen.goto(0, 260)#coordinate
pen.write(" Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))
# Function
wn = turtle.Screen()
def paddle_a_up():#The paddle a moves up
	y = paddle_a.ycor()
	y += 20
	paddle_a.sety(y)
def paddle_a_down():#paddle a moves down
	y = paddle_a.ycor()
	y -= 20
	paddle_a.sety(y)#to set the y coordinate 
def paddle_b_up():#paddle b moves up
	y = paddle_b.ycor()
	y += 20
	paddle_b.sety(y)
def paddle_b_down():#paddle b moves down
	y = paddle_b.ycor()
	y -= 20
	paddle_b.sety(y)
# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
# Main game loop
while shopkins3 == 1:#This loops the ball after it is scored to go to the center and where to go  
    wn.update()	
	# Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
	# Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")
    if score_a == 10:
        pen.goto(0, 130)
        pen.write("Game Over, Player A wins", align  = "center", font = ("Courier", 24, "italic"))
        ball.goto(0, 0)
        break
    elif score_b == 10:
        pen.goto(0, 130 )
        pen.write("Game Over, Player B wins", align = "center", font = ("Courier", 24, "italic"))
        ball.goto(0, 0)
        break
    else:
        None
   
