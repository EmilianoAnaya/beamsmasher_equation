import flet as ft
from components.Buttons import Button
from components.Blanks import Blank
from components.Rows import Row
from components.Variables import Variable
from constants import Symbol, Number,BACKGROUND_IMAGE

class Beamsmasher_Equation():
    def __init__(self):
        self.variables = [0,0,0] #Cada posición inidica las variables X, Y y Z correspondientes
        self.chars = ["X","Y","Z"]
        self.index = 0
    
    def reset_data(self, e):
        self.index = 0
        self.variables = [0]*3
        Button.hover_index_color = 0
        self.first_ans.value = "--"
        self.second_ans.value = "--"
        self.third_ans.value = "--"
        for i, var in enumerate(self.list_variables):
            var.set_variable(self.chars[i])
        self.update_answers()

    def set_index(self, index):
        self.index = index
        Button.hover_index_color = index

    def update_answers(self):
        self.first_ans.update()
        self.second_ans.update()
        self.third_ans.update()
    
    def update_variable(self, value):
        self.variables[self.index] = value
        self.first_ans.value = f"{2*(self.variables[0]) + 11:02}"
        self.second_ans.value = f"{(2*(self.variables[2]) + self.variables[1]) - 5:02}"
        self.third_ans.value = f"{abs((self.variables[1] + self.variables[2]) - self.variables[0]):02}"
        self.list_variables[self.index].set_variable(value)
        self.update_answers()
        self.index += 1
        if self.index > 2:
            self.index = 0
    
    def main(self, page=ft.Page):
        self.page = page
        self.page.title = "Beamsmasher Equation"
        self.page.window.width = 550
        self.page.window.height = 670
        self.page.window.resizable = False
        self.page.window.maximizable = False
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        # Simbolos
        self.symbol_zero = Button(0,Symbol.ZERO.value, self.update_variable)
        self.symbol_eleven = Button(11,Symbol.ELEVEN.value, self.update_variable)
        self.symbol_ten = Button(10,Symbol.TEN.value, self.update_variable)
        self.symbol_twenty_two = Button(22,Symbol.TWENTY_TWO.value, self.update_variable)
        self.symbol_twenty_one = Button(21,Symbol.TWENTY_ONE.value, self.update_variable)
        self.symbol_twenty = Button(20,Symbol.TWENTY.value, self.update_variable)

        # Blanks y Números
        self.Blank = Blank()
        self.number_zero = Blank(Number.ZERO.value)
        self.number_one = Blank(Number.ONE.value)
        self.number_two = Blank(Number.TWO.value)

        # Variables
        self.x_variable = Variable("X", ft.Colors.RED, 0, self.set_index)
        self.y_variable = Variable("Y", ft.Colors.BLUE, 1, self.set_index)
        self.z_variable = Variable("Z", ft.Colors.YELLOW, 2, self.set_index)
        self.list_variables = [self.x_variable, self.y_variable, self.z_variable]

        # Answers
        self.first_ans = ft.Text(value="--",size=50)
        self.second_ans = ft.Text(value="--",size=50)
        self.third_ans = ft.Text(value="--",size=50)

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
                content=ft.Row(
                    controls=[
                        self.x_variable,
                        self.y_variable,
                        self.z_variable,
                    ],
                    spacing=50,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                height=120
            ),
            ft.Container(
                content=ft.Row(
                    controls=[
                        self.first_ans,
                        self.second_ans,
                        self.third_ans,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=30,
                ),
                width=280,
                height=80,
                border_radius=30,
            ),
            ft.ElevatedButton(
                text="Reset",
                color=ft.Colors.AMBER,
                bgcolor=ft.Colors.WHITE12,
                on_click=self.reset_data
            ),
        )
        self.page.update()

app = Beamsmasher_Equation()
ft.app(target=app.main)