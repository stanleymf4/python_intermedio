numeros = [1, 2, 3, 4, 5]

cuadrados = []

for num in numeros:
    cuadrados.append(num**2)

print(numeros)
print(cuadrados)


def cuadarado(num):
    return num**2


cuadrados_map = list(map(cuadarado, numeros))
print("******************************")
print(cuadrados_map)
