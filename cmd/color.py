import os
import colorama

class Colors:
    def __init__(self):
        if os.name == "nt":
            colorama.init()
    def print_color(self, color: str):
        print(color, end="")
    def get_color(self, type: str, color: str):
        return getattr(getattr(colorama, type), color.upper())