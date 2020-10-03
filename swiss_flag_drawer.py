# drawing the swiss national flag

from turtle import *

def smart_drawer(size, angle, _color, toggle_size):
    color(_color)
    fillcolor(_color)
    begin_fill()

    for index, line in enumerate(range(5)):
        right(angle)
        if index == 2:
            if toggle_size == True:
                forward(size*3)
                continue
        forward(size)

    end_fill()
    


def draw_swiss_flag():
    forward(30)
    bgcolor('red')

    smart_drawer(100, 90, 'white', True)
    goto(-70,100)
    smart_drawer(-100, -90, 'white', True)

    mainloop()


if __name__ == '__main__':
    draw_swiss_flag()