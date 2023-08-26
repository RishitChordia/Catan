import time
import tkinter as tk
from board_canvas import BoardCanvas
from catan_board import CatanBoard
from PIL import ImageGrab

from resource_type import Resource


def getorigin(eventorigin):
    global count
    # global x, y
    # x = eventorigin.x
    # y = eventorigin.y
    # print(x, y)
    # print(root.geometry())
    # time.sleep(5)
    # canvas.config(width=250, height=250)
    # canvas.delete("all")
    x = root.winfo_rootx() + canvas.winfo_x()
    y = root.winfo_rooty() + canvas.winfo_y()
    x1 = x + canvas.winfo_width()
    y1 = y + canvas.winfo_height()
    ImageGrab.grab(bbox=(1.5 * x, 1.5 * y, 1.5 * x1, 1.5 * y1)).save(
        "./catan_boards/random_boards/board" + str(count) + ".png"
    )
    count += 1
    canvas.delete("all")
    canvas.draw_board(CatanBoard().get_balanced_board())
    # canvas.draw_board(CatanBoard([3,4,5,6,5,4,3], {12: 2, 11: 3, 10: 3, 9: 3, 8: 3, 6: 3, 5: 3, 4: 3, 3: 3, 2: 2}, resource_counts={
    #         Resource.SHEEP: 6,
    #         Resource.WOOD: 6,
    #         Resource.BRICK: 5,
    #         Resource.HAY: 6,
    #         Resource.ORE: 5,
    #         Resource.DESERT: 2,
    #     }).get_balanced_board())
    

global count
count = 1
root = tk.Tk()
root.bind("<Button 1>", getorigin)

canvas = BoardCanvas(
    root,
    width=1000,
    height=1000,
    highlightthickness=5,
    highlightbackground="black",
    background="#fff7e2",
)
canvas.pack()
canvas.update()
canvas.draw_board(CatanBoard().get_balanced_board())
# canvas.draw_board(CatanBoard([3,4,5,6,5,4,3], {12: 2, 11: 3, 10: 3, 9: 3, 8: 3, 6: 3, 5: 3, 4: 3, 3: 3, 2: 2}, resource_counts={
#             Resource.SHEEP: 6,
#             Resource.WOOD: 6,
#             Resource.BRICK: 5,
#             Resource.HAY: 6,
#             Resource.ORE: 5,
#             Resource.DESERT: 2,
#         }).get_balanced_board())

root.attributes("-fullscreen", True)
root.mainloop()
