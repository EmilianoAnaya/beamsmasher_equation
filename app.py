import flet as ft
from components.Buttons import Button
from components.Blanks import Blank
from components.Rows import Row
from constants import Symbol, Number,BACKGROUND_IMAGE

class Beamsmasher_Equation():
    def __init__(self):
        self.variables = [0,0,0] #Cada posición inidica las variables X,Y y Z correspondientes
        self.index = 0
    
    def update_variable(self, value):
        self.variables[self.index] = value
        self.index += 1
        if self.index > 2:
            self.index = 0
        print(self.variables)
    
    def main(self, page=ft.Page):
        self.page = page
        self.page.title = "Beamsmasher Equation"
        self.page.window.width = 700
        self.page.window.height = 600
        self.page.window.resizable = False
        # self.page.bgcolor = ft.colors.TRANSPARENT
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.symbol_zero = Button(0,Symbol.ZERO.value, self.update_variable)
        self.symbol_eleven = Button(11,Symbol.ELEVEN.value, self.update_variable)
        self.symbol_ten = Button(10,Symbol.TEN.value, self.update_variable)
        self.symbol_twenty_two = Button(22,Symbol.TWENTY_TWO.value, self.update_variable)
        self.symbol_twenty_one = Button(21,Symbol.TWENTY_ONE.value, self.update_variable)
        self.symbol_twenty = Button(20,Symbol.TWENTY.value, self.update_variable)

        self.Blank = Blank()
        self.number_zero = Blank(Number.ZERO.value)
        self.number_one = Blank(Number.ONE.value)
        self.number_two = Blank(Number.TWO.value)

        self.page.add(
            ft.Container(
                ft.Stack(
                    [
                        ft.Image(
                            src=BACKGROUND_IMAGE,
                            
                        ),
                        ft.Column(
                            controls=[
                                Row([self.number_zero,self.Blank,self.Blank,self.symbol_zero]),
                                Row([self.number_one,self.Blank,self.symbol_eleven,self.symbol_ten]),
                                Row([self.number_two,self.symbol_twenty_two,self.symbol_twenty_one,self.symbol_twenty]),
                                Row([self.Blank, self.number_two, self.number_one, self.number_zero]),
                            ],
                        ),
                    ],
                ),
                width=500,
                height=350,
            ),
            ft.Container(
                bgcolor=ft.colors.WHITE,
                width=500,
                height=600
            )
        )
        self.page.update()

app = Beamsmasher_Equation()
ft.app(target=app.main)