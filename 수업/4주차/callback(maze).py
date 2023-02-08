import turtle

def turn_left():
    t.left(10)
    t.forward(10)

def turn_right():
    t.right(10)
    t.forward(10)

def turn_up():
    t.left(90)
    t.forward(10)

def turn_down():
    t.right(90)
    t.forward(10)

def draw_maze(x,y):
    for i in range(2):
        t.penup()
        if i == 1:
            t.goto(x+100,y+100)
        else:
            t.goto(x,y)

        t.pendown()
        t.forward(300)
        t.right(90)
        t.forward(300)
        t.left(90)
        t.forward(300)

t = turtle.Turtle()
screen = turtle.Screen()
t.shape("turtle")

t.speed(0)
draw_maze(-300,200)
t.penup()
t.goto(-300,250)
screen.onkey(turn_left,"Left") # callback 함수
screen.onkey(turn_right,"Right") # callback 함수
screen.onkey(turn_up,"Up") # callback 함수
screen.onkey(turn_down,"Down") # callback 함수

t.speed(1)
t.pendown()
screen.listen() # 기다리다
screen.mainloop() # 반목문 계속 돌기
