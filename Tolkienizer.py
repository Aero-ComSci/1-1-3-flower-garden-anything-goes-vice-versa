import turtle as t
import random
numberfound=False
while numberfound==False:
    prompt = input("Enter Prompt: ")
    for i in prompt:
        if i in "123456789":
            num=int(i)
            print(f"Found number: {num}")
            numberfound=True
            print(numberfound)
            break
        if numberfound:
            break
        else:
            print("Enter a number dunderhead")
t.speed(10)
def tulip (x, y):
    t.penup()
    t.goto(x+5, y)
    t.pendown()
    t.setheading(90)
    t.forward(200)
    t.setheading(0)
    for i in range(15):
        t.forward(i)
        t.left(i)
    t.forward(30)
    for i in range (20):
        t.forward(3)
        t.right(1)
    t.left(140)
    for i in range(5):
        t.forward(15.3)
        t.right(90)
        t.forward(15.3)
        t.left(90)
    t.teleport(x-5,y)
    t.setheading(90)
    t.forward(200)
    t.setheading(180)
    for i in range(15):
        t.forward(i)
        t.right(i)
    t.forward(30)
    for i in range (20):
        t.forward(3)
        t.left(1)
    t.penup()
    t.hideturtle()

def rose(x1, y1):
    t.fillcolor("red")
    t.teleport(x1, y1)
    t.begin_fill()
    for i in range(500):
        t.forward(i/100)
        t.right(5)
    t.right(10)
    t.forward(5)
    t.end_fill()
def arc(size):
    for i in range(size):
        t.forward(i)
        t.right(1)
rose(0, 0)

x=-600
y=0
num=int(num)
for i in range(num):
    tulip(x, y)
    x+=150
    y+=random.randrange(-20, 20)
wn = t.Screen()
wn.mainloop()
