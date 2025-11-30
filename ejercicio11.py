from datetime import datetime, date, timedelta

# Mostrar la fecha y hora actual
ahora = datetime.now()
print(f"Ahora: {ahora}")
hoy = date.today()
print(f"Hoy: {hoy}")

# Formatos de fecha
ahora = datetime.now()
print(f"Español: {ahora.strftime('%d/%m/%Y')}")
print(f"ISO: {ahora.strftime('%Y-%m-%d')}")
print(f"Hora: {ahora.strftime('%H:%M:%S')}")

# Función para calcular la edad
def calcular_edad(fecha_nacimiento):
    hoy = date.today()
    edad = hoy.year - fecha_nacimiento.year
    if (hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1  # Ajuste si aún no ha cumplido años este año
    return edad

nacimiento = date(1990, 5, 15)
edad = calcular_edad(nacimiento)
print(f"Edad: {edad} años")

# Función para agregar recordatorios
recordatorios = []

def agregar_recordatorio(mensaje, dias):
    fecha = datetime.now() + timedelta(days=dias)
    recordatorio = {
        "mensaje": mensaje,
        "fecha": fecha
    }
    recordatorios.append(recordatorio)
    print(f"Recordatorio agregado")

agregar_recordatorio("Reunión importante", 1)

# Medir el tiempo de ejecución de una función
import time

def medir_tiempo(funcion):
    def wrapper():
        inicio = time.time()
        resultado = funcion()
        fin = time.time()
        tiempo = fin - inicio
        print(f"Tardó {tiempo:.4f} segundos")
        return resultado
    return wrapper

@medir_tiempo
def operacion_lenta():
    total = sum(range(1000000))
    return total

resultado = operacion_lenta()
