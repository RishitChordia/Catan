import random
import tkinter as tk
from hex import Hex
from resource_type import Resource
from PIL import Image, ImageTk

class BoardCanvas(tk.Canvas):



    def set_board(self, board):
        self.board = board
        self.rows = len(board)
        self.columns = max(len(i) for i in board)
        
    
    def get_hex_size(self):
        canvas_width = self.winfo_width()
        canvas_height = self.winfo_height()
        max_image_width = canvas_width / self.columns
        max_image_height = 0
        if self.rows%2 == 1:
            max_image_height = 2*canvas_height / ((3*(self.rows-1)/2) + 2)
        else:
            max_image_height = 2*canvas_height / ((3*(self.rows)/2) + 1/2)
        
        self.hex_width = min(max_image_width, max_image_height)
        
    
    def get_hex_icons(self):
        self.hex_icons = dict()
        for resource in Resource:
            img= (Image.open("./assets/resource_hexes/" + resource.value + ".png"))
            resized_image= img.resize((86, 100), Image.ANTIALIAS)
            new_image= ImageTk.PhotoImage(resized_image)
            self.hex_icons[resource] = new_image
            # self.hex_icons[resource] = tk.PhotoImage(file="./assets/resource_hexes/" + resource.value + ".png").subsample(3)
        
        
    def draw_board(self, board):
        self.set_board(board)
        self.get_hex_icons()
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
        for i in self.hex_icons:
            
            self.create_image(random.randint(0,400), random.randint(0,400), image=self.hex_icons[i])
        
        # difference between images in adj column = root3 * hexside
        # difference betweeen images in adj rows = 1.5 * hexside
        # desert shaded background for canvas = #fff7e2 = rgba(255,247,226,255)
    