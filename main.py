# simple bong python 3
# cridit @tokyoedtech
# part 1

import turtle

wn = turtle.Screen()
wn.title('pong by gizmo')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

# score
score_a = 0
score_b = 0

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('red')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('blue')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(+350, 0)
# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = .8
ball.dy = -.8


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('green')
pen.up()
pen.hideturtle()
pen.goto(0 , 260)
pen.write('Player A: 0 Player B: 0 ', align='center' , font=('Courier', 24, 'normal'))




# function
def paddele_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
def paddele_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddele_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
def paddele_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# keybored binding
wn.listen()
wn.onkeypress(paddele_a_up, 'w')
wn.onkeypress(paddele_a_down, 's')
wn.onkeypress(paddele_b_up, 'Up')
wn.onkeypress(paddele_b_down, 'Down')

# Main game loop
while True:
    wn.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -.9
        # winsound.PlaySound('' , winsound.SND_ASYNC)

    if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -.9
    # winsound.PlaySound('' , winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -.9
        score_a += 1
        pen.clear()
        pen.write('Player A: {} Player B: {} ' .format(score_a, score_b), align='center', font=('Courier', 24, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -.9
        score_b += 1
        pen.clear()
        pen.write('Player A: {} Player B: {} '.format(score_a, score_b), align='center', font=('Courier', 24, 'normal'))


    # paddle and ball collisions
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50):
        ball.setx(340)
        ball.dx *= -1
        # winsound.PlaySound('' , winsound.SND_ASYNC)

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1
        # winsound.PlaySound('' , winsound.SND_ASYNC)