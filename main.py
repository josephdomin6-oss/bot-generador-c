import time
import requests

print("✅ Bot de generación de capital iniciado...")

# Aquí el bot simula actividad para que el servidor no se apague
def mantener_conexion():
    print("🌐 Conexión activa. Acumulando puntos de red...")

while True:
    mantener_conexion()
    time.sleep(300) # Se ejecuta cada 5 minutos
