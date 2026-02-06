import os
import time
import json
import websocket

# !!! REEMPLAZA ESTO CON TU ACCESSTOKEN REAL !!!
ACCESS_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkJseG'

def run_grass_websocket():
    # URL del servicio WebSocket de Grass
    ws_url = "wss://proxy.wynd.network:443/ws?access_token=" + ACCESS_TOKEN
    
    def on_message(ws, message):
        data = json.loads(message)
        if data.get("action") == "AUTH_SUCCESS":
            print("✅ Conectado y autenticado correctamente. ¡Ganando puntos!")
            # Puedes enviar acciones adicionales aquí si es necesario
    
    def on_error(ws, error):
        print(f"❌ Error en la conexión: {error}")
    
    def on_close(ws, close_status_code, close_msg):
        print(f"🚪 Conexión cerrada. Status: {close_status_code} Msg: {close_msg}")
        # Intentar reconectar automáticamente después de un tiempo
        time.sleep(10)
        run_grass_websocket()
    
    def on_open(ws):
        print("🤝 Conexión WebSocket abierta. Esperando autenticación...")
        # Enviar mensaje de autenticación si es necesario, aunque el token ya va en la URL
    
    ws = websocket.WebSocketApp(ws_url,
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.run_forever()

if __name__ == "__main__":
    print("Iniciando bot...")
    run_grass_websocket()

