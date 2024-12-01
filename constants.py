from enum import Enum

BACKGROUND_IMAGE = "resources/background_beamsmasher.jpg"

# Ruta de los simbolos posibles
class Symbol(Enum):
    ZERO = "resources/symbols-01.jpg"
    ELEVEN = "resources/symbols-03.jpg"
    TEN = "resources/symbols-02.jpg"
    TWENTY = "resources/symbols-04.jpg"
    TWENTY_ONE = "resources/symbols-05.jpg"
    TWENTY_TWO = "resources/symbols-06.jpg"

# Ruta de los numeros
class Number(Enum):
    ZERO = "resources/number_zero.jpg"
    ONE = "resources/number_one.jpg"
    TWO = "resources/number_two.jpg"

# Tamaños de los contenedores
CHILD_CONTAINER_SIZE:int = 80
VARIABLES_CONTAINER_WIDTH = 100
VARIABLES_CONTAINER_HEIGHT = 80
