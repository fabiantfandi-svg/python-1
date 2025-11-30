print("=== CALCULADORA INTERACTIVA ===")
nombre = input("¿Cuál es tu nombre? ")
print(f"¡Hola {nombre}! Vamos a hacer algunos cálculos.")
print("\nIngresa dos números para calcular:")
numero1 = float(input("Primer número: "))
numero2 = float(input("Segundo número: "))
print("\nOperaciones disponibles: +, -, *, /")
operacion = input("¿Qué operación quieres realizar? ")
if operacion == "+":
    resultado = numero1 + numero2
    simbolo = "+"
elif operacion == "-":
    resultado = numero1 - numero2
    simbolo = "-"
elif operacion == "*":
    resultado = numero1 * numero2
    simbolo = "×"
elif operacion == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
        simbolo = "÷"
    else:
        resultado = "Error: División por cero"
        simbolo = "÷"
else:
    resultado = "Operación no válida"
    simbolo = "?"

print(f"\n--- RESULTADO ---")
if isinstance(resultado, (int, float)):
    print(f"{nombre}, el resultado de {numero1} {simbolo} {numero2} = {resultado}")
else:
    print(f"{nombre}, {resultado}")