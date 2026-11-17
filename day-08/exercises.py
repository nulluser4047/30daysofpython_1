# Día 08 · Comparaciones
# Comparar dos valores me da una respuesta de tipo bool, True o False.

points = 8  # Puntaje que uso para probar las comparaciones.
goal = 10  # Puntaje que quiero alcanzar.

print("Equal?", points == goal)  # == pregunta si los valores son iguales.
print("Different?", points != goal)  # != pregunta si son distintos.
print("Below the goal?", points < goal)  # < pregunta si el primero es menor.
print("Above the goal?", points > goal)  # > pregunta si el primero es mayor.
print("At most the goal?", points <= goal)  # <= incluye los valores menores y el igual.
print("At least the goal?", points >= goal)  # >= incluye los valores mayores y el igual.

reached_goal = points >= goal  # Puedo guardar el resultado de una comparación en una variable.
print("Goal reached?", reached_goal)  # Como 8 está por debajo de 10, muestra False.

print("Inside the range?", 0 <= points <= 10)  # Compruebo un rango entre 0 y 10, con ambos extremos.
print("Same word?", "python" == "Python")  # En el texto, las mayúsculas cuentan. Acá da False.
