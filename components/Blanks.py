import flet as ft
from constants import CHILD_CONTAINER_SIZE

class Blank(ft.Container):
    def __init__(self, img=None):
        super().__init__()
        if img:
            self.content = ft.Image(
                src=img,
            )
        self.bgcolor = ft.colors.TRANSPARENT
        self.width = CHILD_CONTAINER_SIZE
        self.height = CHILD_CONTAINER_SIZE