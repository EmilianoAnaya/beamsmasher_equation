import flet as ft

class Beamsmasher_Equation():
    def __init__(self):
        ...
    
    def main(self, page=ft.Page):
        self.page = page
        self.page.title = "Beamsmasher Equation"
        self.page.window.width = 800
        self.page.window.height = 500
        self.page.window.resizable = False
        self.page.bgcolor = ft.colors.TRANSPARENT 

        self.main_container = ft.Container(
            bgcolor=ft.colors.RED,
            width=100,
            height=100
        )

        self.page.add(
            ft.Container(
                content=ft.Row(
                        [
                        self.main_container,
                        ft.Container(
                            width=200,
                            height=200,
                            bgcolor=ft.colors.BLUE
                        )
                    ],
                    spacing=0,
                ),
                height=200,
                bgcolor=ft.colors.YELLOW,
            ),
            ft.Row(
                [
                    ft.Container(
                        width=200,
                        height=200,
                        bgcolor=ft.colors.BLUE
                    ),
                    self.main_container,
                ]
            )   
        )

        self.page.update()

app = Beamsmasher_Equation()
ft.app(target=app.main)