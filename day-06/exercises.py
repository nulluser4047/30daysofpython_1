# Día 06 · Cadenas de texto
# Una cadena guarda caracteres. Los índices empiezan a contar desde 0.

galaxy = "Andromeda"  # Guardo el nombre como texto.
print(len(galaxy))  # len() cuenta cuántos caracteres tiene la cadena.
print(galaxy[0])  # [0] toma la primera letra, A.
print(galaxy[-1])  # [-1] toma la última letra, a.
print(galaxy[:3])  # Tomo desde el inicio hasta antes de la posición 3. Sale And.

print(galaxy.lower())  # lower() devuelve el texto en minúscula.
print(galaxy.upper())  # upper() devuelve el texto en mayúscula.
raw_label = "  M31  "  # Este texto tiene espacios al principio y al final.
clean_label = raw_label.strip()  # strip() saca los espacios de los extremos.
print(galaxy + " (" + clean_label + ")")  # Con + uno las partes para formar el rótulo.

observations = 3  # Guardo un número para usarlo dentro de un mensaje.
print(f"I wrote {observations} notes on {galaxy}.")  # La f permite insertar valores entre llaves.
brightness = 0.756  # Uso este valor para practicar el formato de un decimal.
print(f"Brightness = {brightness:.2f}")  # :.2f muestra el número con dos decimales.
