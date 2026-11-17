# Día 04 · Operaciones aritméticas
# Guardo los números en variables para poder probar otras cuentas cambiando los valores.

first_number = 17  # Primer valor de los ejemplos.
second_number = 5  # Segundo valor. También lo uso como divisor.

print("Sum =", first_number + second_number)  # Sumo los dos valores.
print("Difference =", first_number - second_number)  # Resto el segundo al primero.
print("Product =", first_number * second_number)  # Multiplico los dos valores.
print("Division =", first_number / second_number)  # / da el cociente con decimales.

print("Whole groups =", first_number // second_number)  # // redondea el cociente hacia abajo.
print("Remainder =", first_number % second_number)  # % da el resto. De 17 sobran 2 al agrupar de a 5.
print("Power =", 2 ** 3)  # ** eleva un número a una potencia. Acá es 2 al cubo.

average = (8 + 6 + 10) / 3  # Primero sumo los tres valores y después divido entre 3.
print("Average =", average)  # Muestro el promedio.
print(round(10 / 3, 2))  # round() redondea el resultado a dos decimales en este ejemplo.
