# Día 03 · Tipos de datos y conversiones
# type() me dice qué tipo de dato tiene un valor.

star_count = 12  # int es un número entero.
brightness = 0.75  # float representa un número con decimales. Uso el punto decimal.
galaxy_name = "Andromeda"  # str es una cadena de texto.
is_spiral = True  # bool es un valor lógico. True y False llevan mayúscula al comienzo.

print(type(star_count))  # Muestra int.
print(type(brightness))  # Muestra float.
print(type(galaxy_name))  # Muestra str.
print(type(is_spiral))  # Muestra bool.

text_number = "12"  # Las comillas hacen que 12 sea texto.
whole_number = int(text_number)  # int() convierte ese texto en un número entero.
decimal_number = float("2.5")  # float() convierte el texto en un número con decimales.
number_label = str(whole_number)  # str() convierte el número a texto.

print(whole_number + 1)  # Ahora puedo sumar 1 al número entero que obtuve.
print(decimal_number * 2)  # También puedo hacer cuentas con los decimales.
print("Stars = " + number_label)  # Uso + para unir dos textos.
