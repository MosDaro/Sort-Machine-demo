from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

class Window:
    def __init__(self, root, window_size, window_title, window_logo, window_bg_color):
        root.geometry(str(window_size[0]) +"x" + str(window_size[1]))
        root.title(window_title)
        root.iconbitmap(window_logo)
        root.configure(bg=window_bg_color)

