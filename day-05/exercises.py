# Día 05 · Leer datos con input()
# Para probar este archivo, ingreso Ada, 20 y 2.5 cuando la terminal me los pide.

name = input("What's your name? ")  # Muestra una pregunta y espera hasta que presiono Enter.
print("Hello,", name)  # Uso el texto ingresado para armar el saludo.

minutes_text = input("How many minutes did you study? ")  # input() siempre devuelve texto.
print(type(minutes_text))  # Si escribo 20, acá veo que su tipo es str.
minutes = int(minutes_text)  # Convierto ese texto en un entero para hacer cuentas.
next_goal = minutes + 10  # Calculo una meta de diez minutos más.
print("Next goal =", next_goal)  # Muestro el resultado de la suma.

hours = float(input("How many hours did you study this week? "))  # Para 2.5 uso float() y punto decimal.
print("Half the time =", hours / 2)  # Una vez convertido, puedo dividir el número.
