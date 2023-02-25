import tkinter as tk
root = tk.Tk()
root.title("DRAWING CIRCLES")

canvas = tk.Canvas(root, width=500, height=500)
size = tk.Entry(root)
color = tk.Entry(root)

def draw(event):
    circle_size = int(size.get())
    circle_color = color.get()
    x = event.x
    y = event.y
    canvas.create_oval(x - circle_size, y - circle_size, x + circle_size, y + circle_size, fill=circle_color)

canvas.bind("<Button-1>", draw)
canvas.pack()
size.pack()
color.pack()
root.mainloop()
