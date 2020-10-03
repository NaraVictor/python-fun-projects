# program to draw a star with dynamic color n length

from turtle import *

def draw_star(length, color):
    angle = 140
    fillcolor(color)
    begin_fill()

    for side in range(5):
        forward(length)
        right(angle)
        forward(length)
        right(72 - angle)
    end_fill()
    mainloop()


print('Input parameters to draw your star')
length, color = int(input('Length of star: ')), input('Color of star: ')
draw_star(length, color)