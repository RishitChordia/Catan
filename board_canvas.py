import math
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
        if self.rows % 2 == 1:
            max_image_height = 2 * canvas_height / ((3 * (self.rows - 1) / 2) + 2)
        else:
            max_image_height = 2 * canvas_height / ((3 * (self.rows) / 2) + 1 / 2)
        self.hex_width = min(max_image_width, max_image_height * math.sqrt(3) / 2)
        self.hex_height = int(self.hex_width * 2 / math.sqrt(3))
        self.hex_width = int(self.hex_width)


    def get_token_size(self):
        self.token_size = self.hex_height // 7


    def get_hex_icons(self):
        self.hex_icons = dict()
        self.get_hex_size()
        self.get_token_size()
        for resource in Resource:
            img = Image.open("./assets/resource_hexes/" + resource.value + ".png")
            resized_image = img.resize(
                (self.hex_width, self.hex_height), Image.ANTIALIAS
            )
            new_image = ImageTk.PhotoImage(resized_image)
            self.hex_icons[resource] = new_image


    def draw_hex_row(self, row_index, x, y):
        for hex in self.board[row_index]:
            self.create_image(x, y, image=self.hex_icons[hex.resource_type])

            if hex.number_token:
                self.create_oval(
                x - self.token_size,
                y - self.token_size,
                x + self.token_size,
                y + self.token_size,
                fill= "#FFE9B3"
                )
                self.create_text(x, y, text= hex.number_token)
            x += self.hex_width


    def draw_hexes(self):
        start_top = self.hex_height // 2
        width_center = self.winfo_width() // 2
        # Needs logic here to keep half border between top and bottom margins but fine for now
        for index, row in enumerate(self.board):
            start_left = width_center - int(self.hex_width * ((len(row) - 1) / 2))
            self.draw_hex_row(index, start_left, start_top)
            start_top += self.hex_height * 3 // 4


    def draw_board(self, board):
        self.set_board(board)
        self.get_hex_icons()
        self.draw_hexes()
