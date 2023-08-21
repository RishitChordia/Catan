import tkinter as tk

class BoardCanvas(tk.Canvas):
    def __init__(self):
        self.board = [] # array of array of hexes
        
        
        # some function to convert self.board into hex images with number tokens on self canvas