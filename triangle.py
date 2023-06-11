import tkinter
import random
from tkinter import *


def point_on_triangle2(pt1, pt2, pt3):
    """
    Random point on the triangle with vertices pt1, pt2 and pt3.
    """
    x, y = random.random(), random.random()
    q = abs(x - y)
    s, t, u = q, 0.5 * (x + y - q), 1 - 0.5 * (q + x + y)
    return (
        s * pt1[0] + t * pt2[0] + u * pt3[0],
        s * pt1[1] + t * pt2[1] + u * pt3[1],
    )


def create_circle(x, y, r, can: tkinter.Canvas):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return can.create_oval(x0, y0, x1, y1, fill='white')


def main():
    point_count = 0
    dimensions = (800, 700)  # window size in pixels
    points = [(dimensions[0]/2, 10), (10, dimensions[1]-100), (dimensions[0]-10, dimensions[1]-100)]  # triangle vertices
    text_location = (160, 50)  # number of points field location
    input_location = (dimensions[0]/2, dimensions[1]/2-50)
    __SPEED = 5
    running = True

    def draw_point():
        if not running:
            return
        nonlocal x
        nonlocal y
        nonlocal point_count
        canvas.delete("count")
        vertex = random.choice(points)
        midpoint = ((vertex[0]+x)/2, (vertex[1]+y)/2)  # midpoint between a random vertex and the current point
        create_circle(midpoint[0], midpoint[1], 1, canvas)
        canvas.create_text(text_location, text=f"Number of points: {point_count}",
                           fill="white", font='Helvetica 15', tags="count")
        x, y = midpoint
        point_count += 1
        root.after(__SPEED, draw_point)

    def remove_temp_text(e):
        textbox.delete(0, "end")

    def start(e):
        canvas.create_window(dimensions[0]-200, 40, window=pause_button, tags="pause_button")
        canvas.create_window(dimensions[0]-200, 80, window=quit_button, tags="quit_button")
        pause_button.bind("<Button-1>", pause)
        quit_button.bind("<Button-1>", quit_program)

        nonlocal __SPEED
        try:
            __SPEED = int(textbox.get())
            canvas.delete("textbox", "start_button")
            draw_point()
        except Exception as e:
            root.quit()
            print("EXCEPTION: " + str(e))

    def pause(e):
        nonlocal running
        running = not running
        if running:
            pause_button.configure(text="Pause")
        else:
            pause_button.configure(text="Continue")
        draw_point()

    def quit_program(e):
        exit()

    root = Tk()
    root.title("Fractal shit")

    canvas = Canvas(root, width=dimensions[0], height=dimensions[1], bg="black")
    canvas.pack()
    canvas.create_polygon(*points, fill='black', outline='white')  # draw the triangle

    x, y = point_on_triangle2(*points)
    create_circle(x, y, 1, canvas)  # set random starting point

    textbox = Entry(canvas)
    start_button = Button(canvas, text="Start")
    pause_button = Button(canvas, text="Pause")
    quit_button = Button(canvas, text="Quit")
    textbox.insert(0, "Set desired speed...")
    canvas.create_window(input_location, window=textbox, tags="textbox")
    canvas.create_window(input_location[0], input_location[1]+30, window=start_button, tags="start_button")
    textbox.bind("<FocusIn>", remove_temp_text)
    start_button.bind("<Button-1>", start)

    canvas.pack()
    root.mainloop()  # magic begins here


main()
