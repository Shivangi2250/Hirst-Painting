# import colorgram
# colors = colorgram.extract('image.jpg', 12)
# rgb_colors=[]
#
# for color in colors:
#     r= color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     rgbcolors=(r,g,b)
#     rgb_colors.append(rgbcolors)
# print(rgb_colors)
import turtle as t
from turtle import Screen
import random

tinny=t.Turtle()
tinny.shape("turtle")
tinny.hideturtle()
tinny.speed(0)
t.colormode(255)
tinny.penup()
tinny.setheading(200)
tinny.forward(400)
tinny.setheading(0)




color_list=[
     (26, 108, 164),
    (193, 38, 81), (237, 161, 50), (234, 215, 86),
    (223, 137, 176), (143, 108, 57), (103, 197, 219), (21, 57, 132)
]
def random_color():
    color=random.choice(color_list)
    return color
def tinny_move():
    for i in range(20):
        if i%2==0:
            tinny.forward(30)
        else:
            tinny.dot(20,random_color())
            tinny.forward(30)
def hirst_painting():
    for l in range(5):
        tinny_move()
        tinny.left(90)
        tinny.forward(50)
        tinny.left(90)
        tinny_move()
        tinny.right(90)
        tinny.forward(50)
        tinny.right(90)

hirst_painting()






screen=Screen()
screen.exitonclick()

