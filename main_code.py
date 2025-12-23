from turtle import *

t=Turtle()
t.color('blue')
t.shape('circle')
t.width(5)
t.speed(0)

def red():
    t.color('red')
    t.width(5)

def green():
    t.color('green')
    t.width(5)

def blue():
    t.color('blue')
    t.width(5)

def eraser():
    t.width(20)
    t.color('white','grey')

def move(x,y):
    t.up()
    t.goto(x,y)
    t.down()

t.ondrag(t.goto)
scr = t.getscreen()
scr.onscreenclick(move)
scr.listen()

def move_right():
    t.goto(t.xcor() + 5, t.ycor())

def move_down():
    t.setheading(270)
    t.forward(10)

def move_left():
    t.setheading(180)
    t.forward(10)

def move_up():
    t.setheading(90)
    t.forward(10)    

scr.onkey(move_down, 'Down')
scr.onkey(move_up, 'Up')
scr.onkey(move_left, 'Left')
scr.onkey(move_right, 'Right')

scr.onkey(red,'r')
scr.onkey(green,'g')
scr.onkey(blue,'b')
scr.onkey(eraser,'BackSpace')
scr.onkey(t.begin_fill,'v')
scr.onkey(t.end_fill,'e')

mainloop()
