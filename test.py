import time
import tkinter as tk
from board_canvas import BoardCanvas
from catan_board import CatanBoard

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


canvas = BoardCanvas(
    root, width=500, height=500, highlightthickness=5, highlightbackground="black"
)
canvas.draw_board(CatanBoard().get_random_board())
canvas.pack()

root.mainloop()
