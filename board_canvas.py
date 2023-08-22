import tkinter as tk
from hex import Hex
# from PIL import Image, ImageTk

class BoardCanvas(tk.Canvas):



    def set_board(self, board):
        self.board = board
        self.rows = len(board)
        self.columns = max(len(i) for i in board)
        self.photo = tk.PhotoImage(file="./assets/resource_hexes/brick.png").subsample(3)
        
        
    def draw_board(self, board):
        self.set_board(board)
        canvas_width = self.winfo_width()
        canvas_height = self.winfo_height()
        image_height, image_width = 370, 321
        image_scaling = min(canvas_height/((self.rows+0.5)*image_height) , canvas_width/image_width)
        print(image_height, image_width, image_scaling)
        mid_row = self.rows//2
        mid_column = self.columns//2
        # img= (Image.open("./assets/resource_hexes/brick.png"))

        # img = tk.PhotoImage(file="./assets/resource_hexes/brick.png")
        # new_img = img.resize((50,50), Image.ANTIALIAS)
        # final_img = ImageTk.PhotoImage(new_img)
        self.create_image(50, 50, image=self.photo)
        
        # difference between images in adj column = root3 * hexside
        # difference betweeen images in adj rows = 1.5 * hexside
        # desert shaded background for canvas = #fff7e2 = rgba(255,247,226,255)
    