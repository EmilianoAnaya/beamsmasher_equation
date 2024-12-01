import flet as ft
from constants import CHILD_CONTAINER_SIZE

class Blank(ft.Container):
    def __init__(self, img=None, size=CHILD_CONTAINER_SIZE):
        super().__init__()
        if img:
            self.content = ft.Image(
                src=img,
            )
        self.bgcolor = ft.Colors.TRANSPARENT
        self.width = size
        self.height = size