import os
import time
import requests

# Reemplaza 'TU_ACCESS_TOKEN_AQUI' con el valor de tu accessToken copiado
ACCESS_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkJseG' 

print("✅ Bot de Grass iniciado con Access Token...")

def mantener_conexion():
    # Enviar una señal a Grass para decirles que estás activo
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    # Esta es una URL de ejemplo, la URL real es parte del WebSocket de Grass
    response = requests.get("https://app.getgrass.io", headers=headers)
    if response.status_code == 200:
        print("🌐 Conexión activa. Acumulando puntos de red...")
    else:
        print(f"❌ Error de conexión: {response.status_code}")

# El bot se mantendrá activo cada 15 minutos
while True:
    mantener_conexion()
    time.sleep(900)
