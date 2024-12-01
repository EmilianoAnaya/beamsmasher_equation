import flet as ft
from components.Blanks import Blank
from constants import VARIABLES_CONTAINER_WIDTH, VARIABLES_CONTAINER_HEIGHT

class Variable(ft.Container):
    def __init__(self, variable:str, color:ft.Colors, index:int, click_callback=None):
        super().__init__()
        self.index = index
        self.var_text = ft.Text(
            value=variable,
            size=50,
            text_align=ft.TextAlign.CENTER,
            color=ft.Colors.BLACK,
        )
        self.content = ft.Column(
            controls=[
                ft.Container(
                    content=self.var_text,
                    width=VARIABLES_CONTAINER_WIDTH,
                    height=VARIABLES_CONTAINER_HEIGHT,
                    bgcolor=color,
                    border_radius=40
                ),
                ft.Button(
                    text=f"Set",
                    color=ft.Colors.AMBER,
                    bgcolor=ft.Colors.WHITE12,
                    on_click=lambda e: self.handle_click(e, click_callback)
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

    def set_variable(self, value):
        self.var_text.value = value
        self.update()

    def handle_click(self, e, click_callback):
        click_callback(self.index)
