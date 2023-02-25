import tkinter as tk
import tkinter.colorchooser as colorchooser


root = tk.Tk()
root.title("DRAWING CIRCLES")

canvas = tk.Canvas(root, width=500, height=500)
size = tk.Entry(root)

color1 = '#F0F8FF'


def choose_color():
    global color1
    color_c = colorchooser.askcolor(title="CHOOSE COLOR")[1]
    if color_c:
        color1 = color_c
    canvas.focus_set()


def draw(event):
    circle_size = int(size.get())
    x = event.x
    y = event.y
    canvas.create_oval(x - circle_size, y - circle_size, x + circle_size, y + circle_size, fill=color1)


def draw2(event):
    circle_size = int(size.get())
    x = event.x
    y = event.y
    canvas.create_rectangle(x - circle_size / 2, y - circle_size / 2, x + circle_size / 2, y + circle_size / 2,
                            fill=color1)


def draw3(event):
    circle_size = int(size.get())
    x = event.x
    y = event.y
    canvas.create_polygon(x, y - circle_size, x - circle_size, y + circle_size, x + circle_size, y + circle_size,
                          fill=color1, outline='#000000')


def clear(event):
    canvas.delete("all")


color = tk.Button(root, text="CHOOSE COLOR", command=choose_color)
canvas.bind("<Button-1>", draw)
canvas.bind("<Button-2>", draw3)
canvas.bind("<Button-3>", draw2)
canvas.bind("<Key-r>", clear)
canvas.pack()
size.pack()
color.pack()
root.mainloop()
