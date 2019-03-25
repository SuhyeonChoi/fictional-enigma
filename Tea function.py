from turtle import *

reset()


def sv_tree(size, iteration):
    if iteration == 1:
        return
    forward(size)

    left(30)
    forward(size / 2)
    backward(size / 2)
    sv_tree(size / 2, iteration -1)
    right(30)

    right(30)
    forward(size/2)
    backward(size/2)
    sv_tree(size / 2, iteration -1)
    left(30)
    
    backward(size)

def main():
    home()
    clear()
    sv_tree(128,6)

main()
