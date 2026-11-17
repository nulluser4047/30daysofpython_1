# Día 09 · Condicionales con if, elif y else
# Los dos puntos abren un bloque. Uso cuatro espacios para marcar las líneas que le pertenecen.

study_minutes = 25  # Minutos que usé para el ejemplo.
if study_minutes >= 20:  # Si llego a 20 minutos o más, Python ejecuta el bloque.
    print("Study goal reached.")  # Está dentro del bloque del if por la sangría.

score = 8  # Puedo probar con 9, 7 y 4 para ver las tres salidas.
if score >= 9:  # Primero reviso el caso del puntaje más alto.
    print("Excellent!")  # Se ejecuta con 9 puntos o más.
elif score >= 6:  # Se revisa esta condición cuando el if anterior dio False.
    print("You passed.")  # En este ejemplo, corresponde a puntajes de 6 a 8.
else:  # Entra acá cuando las condiciones anteriores dieron False.
    print("Keep practicing.")  # En este ejemplo, corresponde a puntajes menores que 6.
