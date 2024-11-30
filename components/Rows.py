import flet as ft

class Row(ft.Row):
    def __init__(self, data: list):
        super().__init__()
        self.controls = data
        self.spacing = 60