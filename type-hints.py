"""Typing con Python"""

variable = 42
print(f"variable: {variable} del tipo {type(variable)}")

variable = "texto de prueba"
print(f"variable: {variable} del tipo {type(variable)}")

otra_variable: int = 44
print(f"otra_variable: {otra_variable} del tipo {type(otra_variable)}")


def suma_clara(a: int, b: int) -> int:
    return a + b


print(suma_clara(10, 10))
