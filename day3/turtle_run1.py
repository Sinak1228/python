import turtle as t

wn = t.Screen()
wn.bgcolor("black")
wn.title("Turlte Run Ver.1")

def turn_right():
    t.setheading(0)
    t.forward(30)

def turn_left():
    t.setheading(180)
    t.forward(30)

def turn_up():
    t.setheading(90)
    t.forward(30)

def turn_down():
    t.setheading(270)
    t.forward(30)

def reset():
  t.clear()

t.shape("turtle")
t.color("white")
t.speed(0)
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
t.onkeypress(reset, "R")
t.listen()
