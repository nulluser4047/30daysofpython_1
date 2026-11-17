# Día 10 · Mi primer bucle while
# while vuelve a revisar la condición antes de cada vuelta.

step = 1  # El contador empieza en 1.
while step <= 5:  # Repito el bloque mientras el contador sea 5 o menos.
    print("Step", step)  # Muestro el valor de esta vuelta.
    step += 1  # Sumo 1 al contador. Es lo mismo que step = step + 1.

print("Finished.")  # Al llegar a 6, la condición da False y el programa sigue por acá.

steps_left = 3  # Ahora el contador va hacia atrás.
while steps_left > 0:  # El bucle sigue mientras queden pasos.
    print("Countdown", steps_left)  # Muestro cuántos pasos faltan.
    steps_left -= 1  # Resto 1 para acercarme a cero.

print("Liftoff!")  # Se muestra una vez, después de terminar la cuenta.

# Me acuerdo de actualizar el contador dentro del bucle para que pueda llegar al final.
