import time
import tkinter as tk


def getorigin(eventorigin):
    global x, y
    x = eventorigin.x
    y = eventorigin.y
    print(x, y)
    print(root.geometry())
    time.sleep(5)
    canvas.config(width=250, height=250)
    canvas.delete("all")


root = tk.Tk()
root.bind("<Button 1>", getorigin)


canvas = tk.Canvas(
    root, width=500, height=500, highlightthickness=5, highlightbackground="black"
)
canvas.pack()
img = tk.PhotoImage(file="./assets/resource_hexes/brick.png")
canvas.create_image(0, 0, image=img)
# canvas.create_image(250, 300, image=img)
# canvas.create_image(300, 300, image=img)
root.mainloop()

time.sleep(5)
canvas.config(width=250, height=250)
canvas.delete("all")
