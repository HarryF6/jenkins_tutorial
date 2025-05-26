# Saludo personalizado
nombre = input("¿Cómo te llamas? ")
print(f"Hola, {nombre}!")

# Pregunta por la edad
edad = int(input("¿Cuántos años tienes? "))

# Calcula el año en que cumplirá 100
from datetime import datetime
año_actual = datetime.now().year
año_100 = año_actual + (100 - edad)

print(f"{nombre}, cumplirás 100 años en el año {año_100}.")

