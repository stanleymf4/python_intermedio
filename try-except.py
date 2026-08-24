class DivisionError(Exception):
    """Error en operación"""


try:
    a = int(input("Digita un numero: "))
    b = int(input("Digita otro numero: "))
    if b == 2:
        raise DivisionError("No se puede dividir entre 2")
    resultado = a / b
    print(f"El resultado de la division es: {resultado}")
except ValueError:
    print("Error: Debes ingresar un número válido.")
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
except Exception as e:
    print(f"Error: {e}")
finally:
    print("print desde finally")
