name = "Ana"
text = f"Hola {name}"
edad = 17
print(text)

tex_if = f"Hola {name} eres {'mayor' if edad >= 18 else 'menor'} de edad"


print(tex_if)

bank_balance = 120000000000000
text = f"El saldo en tu banco es {bank_balance:,}"
print(text)


stock_price = 1.405
text = f"El valor del stock es {stock_price:.1f}"
print(text)


user_id = 1
text = f"Su id es: {user_id:05d}"
print(text)

product = "laptop"
price = 1000
text = f"producto: {product:<15} | precio: {price:>15}"
text = f"producto: {product:<15} | precio: {price:>15}"
print(f"{text}\n{text}")

from datetime import datetime

date = datetime(2024, 12, 5, 10, 10)
text = f"La fecha completa es: {date:%A %d de %B de %Y a las %H:%M}"
print(text)


tasa = 0.123456789
text = f"La tasa de interes es: {tasa:.2%}"
print(text)

numero = 0.00125
text = f"El numero en notación cientifica es: {numero:.2e}"
print(text)
