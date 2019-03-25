import turtle
import random

colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow", "brown"]


class Present:
    def __init__(self, price=0, start=(0,0), color = None,
                 width=None, height=None):
        self.price = price
        self.start = start
        self.color = random.choice(colors)
        self.width = random.choice(range(10, 150))
        self.height = random.choice(range(10, 150))
        if color:
            self.color = color
        if width:
            self.width = width
        if height:
            self.height = height

        # setup Turtle
        self.turtle = turtle.Turtle(visible=False)
        self.turtle.hideturtle()

    def set_start(self, start=None):
        self.start = start

    def __str__(self):
        return 'Present: ' + \
            "type={0} price={1} color={2}, " \
            "start=({3},{4})".format(
                self.__class__.__name__,
                self.price,
                self.color,
                self.start[0],
                self.start[1]
            )

    def __repr__(self):
        return self.__str__()

    def start_drawing(self):
        self.turtle.reset()
        self.turtle.penup()
        self.turtle.goto(self.start[0], self.start[1])
        self.turtle.pendown()

        self.turtle.begin_fill()

    def end_drawing(self):
        self.turtle.end_fill()
        self.turtle.hideturtle()

class House(Present):
    def draw(self):
        self.start_drawing()
        self.turtle.color(self.color)

class Chocolate(Present):
    def draw(self):
        self.start_drawing()
        self.turtle.color(self.color)

        for i in range(2):
            self.turtle.fd(self.width)
            self.turtle.left(90)
            self.turtle.fd(self.height)
            self.turtle.left(90)

        self.end_drawing()


class HolidayCard:
    def __init__(self, img_file = "bag.jpg"):
        self.presents = []
        self.turtle = turtle.Turtle()
        turtle.tracer(0,0)
        if img_file:
            turtle.bgpic(img_file)
        else:
            turtle.bgcolor(random.choice(colors))


        turtle.onscreenclick(self.mouse_click)
        self.turtle.hideturtle()

    def add_present(self, present):
        self.presents.append(present)

    def mouse_click(self, mouse_x, mouse_y):
        x = mouse_x
        y = mouse_y

        present = random.choice(self.presents)
        present.set_start((x, y))
        present.draw()


if __name__ == '__main__':
    card = HolidayCard()
    card.add_present(Chocolate((0, 0),"yellow"))
    card.add_present(Chocolate((0, 0),"brown",50,50))
    card.add_present(Chocolate((0, 0),"green",100,50))
    card.add_present(Chocolate((0, 0),"blue"))
    card.add_present(Chocolate((0, 0), "gold"))

    for p in card.presents:
        print(p)

    turtle.done()