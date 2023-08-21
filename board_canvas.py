import tkinter as tk
from hex import Hex

class BoardCanvas(tk.Canvas):



    def set_board(self, board):
        self.board = board
        self.rows = len(board)
        self.columns = max(i for i in board)
        
        
    def draw_board(self, board):
        self.set_board(board)
        canvas_width = self.winfo_width()
        canvas_height = self.winfo_height()
        image_height, image_width = 370, 321
        