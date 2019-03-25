from turtle import *

#choose color and size
color('pink','sky blue')
bgcolor("white")
size = 300

#Higher speed
speed("fastest")
hideturtle()

#Ensure snowflake is located at the center
penup()
backward(size/1.732)
left(30)
pendown()

begin_fill()

def snowflake(side_length, levels):
    if levels > 0:
        for i in [60, -120, 60, 0]:
            snowflake(side_length/3, levels-1)
            left(i)
    else:
        forward(side_length)

end_fill()

snowflake(100, 5)
