import turtle
import random

screen=turtle.Screen()
raceon=False

screen.setup(height=500,width=700)
answer=turtle.textinput(title="heyy make a bet" ,prompt= "WHICH TURTLE WILL WIN")

tortois=[]
position=[190,125,60,-5,-70,-135]
paint=["red","green","blue","yellow","orange","black"]
for i in range(6):
    rocky=turtle.Turtle("turtle")
    rocky.penup()
    rocky.goto(x=-340,y=position[i])
    rocky.color(paint[i])
    tortois.append(rocky)

if answer:
    raceon=True
while raceon:
    for rocky in tortois:
        if rocky.xcor() >= 320:
            raceon=False
            color=rocky.pencolor()
            if color==answer:
                print("you won!!!")
                break
            else:
                print(f"you loose {color} won")
                break
        randomdis=random.randint(1,20)
        rocky.forward(randomdis)
            







screen.exitonclick()