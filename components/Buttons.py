import flet as ft
from constants import CHILD_CONTAINER_SIZE

class Button(ft.Container):
    hover_color = [ft.Colors.RED, ft.Colors.BLUE, ft.Colors.YELLOW]
    border_color = [1]*3
    hover_index_color = 0

    def __init__(self, value, img, on_click_callback):
        super().__init__()
        self.content = ft.Image(
            src=img,
        )
        self.value = value
        self.width = CHILD_CONTAINER_SIZE
        self.height = CHILD_CONTAINER_SIZE
        self.on_hover = self.show_border
        self.on_click = lambda e: self.handle_click(e, on_click_callback)

    def show_border(self,e):
        if e.data == "true":
            self.border = ft.border.all(5, Button.hover_color[Button.hover_index_color])
        else:
            self.border = ft.border.all(2, ft.Colors.TRANSPARENT)
        self.update()
    
    def handle_click(self, e, on_click_callback):
        on_click_callback(self.value)
        Button.hover_index_color +=1
        if Button.hover_index_color>2:
            Button.hover_index_color = 0