# Día 07 · Miniproyecto de calculadora de compras
# Junto input(), variables, operaciones y f-strings para calcular un total con descuento.
# Para probar, ingreso 12.50 de precio, 2 artículos y 10 de descuento.

unit_price = float(input("Price per item? "))  # Leo el precio de un artículo. Escribo los decimales con punto.
quantity = int(input("How many items? "))  # La cantidad de artículos se ingresa como un entero.
discount_percent = float(input("Discount percent? "))  # Escribo 10 para un descuento del 10 %.

subtotal = unit_price * quantity  # Multiplico el precio unitario por la cantidad.
discount_rate = discount_percent / 100  # Paso el porcentaje a decimal. 10 % se vuelve 0.10.
discount_amount = subtotal * discount_rate  # Calculo cuánto dinero representa el descuento.
total = subtotal - discount_amount  # Le resto el descuento al subtotal para llegar al total.

print(f"Subtotal = {subtotal:.2f}")  # Muestro el subtotal con dos decimales.
print(f"Discount = {discount_amount:.2f}")  # Muestro el monto que se descuenta.
print(f"Total = {total:.2f}")  # El valor final es el total a pagar.
