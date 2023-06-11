import random
import tkinter
from tkinter import *


def point_on_rectangle(pt1, pt2):
    return random.randint(pt1[0], pt2[0]), random.randint(pt1[1], pt2[1])


def create_circle(x, y, r, can: tkinter.Canvas):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return can.create_oval(x0, y0, x1, y1, fill='white')


def main():
    point_count = 0
    __SPEED = 5  # drawing speed - time in ms between iterations
    points = [(200, 100), (600, 500)]  # rectangle top left and bottom right points
    attractors = [(200, 100), (400, 100), (600, 100), (200, 300), (600, 300), (200, 500), (400, 500), (600, 500)]

    def draw_point():
        nonlocal x
        nonlocal y
        nonlocal point_count
        canvas.delete("count")
        attractor = random.choice(attractors)
        new_point = ((x + 2 * attractor[0]) / 3, (y + 2 * attractor[1]) / 3)
        create_circle(new_point[0], new_point[1], 1, canvas)
        canvas.create_text(400, 550, text=f"Number of points: {point_count}",
                           fill="white", font='Helvetica 10', tags="count")
        x = new_point[0]
        y = new_point[1]
        point_count += 1
        root.after(__SPEED, draw_point)

    root = Tk()
    root.title("Fractal shit")

    canvas = Canvas(root, width=800, height=600, bg="black")
    canvas.create_rectangle(points, fill='black', outline='white')

    x, y = point_on_rectangle(*points)  # set a random starting point
    create_circle(x, y, 1, canvas)

    canvas.pack()
    draw_point()
    root.mainloop()


main()
