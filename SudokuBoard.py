import pygame, sys
class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

    def set_cell_value(self, value):
        pass

    def set_sketched_value(self, value):
        # stuff for sketching the value inside
        pass

    def draw(self):
        # reference draw_chips() function in main_gui.py
        # reference oop_main.py file
        pass
