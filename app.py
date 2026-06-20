import os
import socket
import random
import time
from flask import Flask

app = Flask(__name__)
SERVER_NAME = os.getenv("SERVER_NAME", "SERVER WEB")

@app.route('/api/v1/status')
def status():
    # Simulasi latensi
    delay_ms = random.randint(50, 150)
    time.sleep(delay_ms / 1000.0)
    
    # Penentuan warna background
    if SERVER_NAME == "SERVER 1":
        color = "#3498db" # Biru
    elif SERVER_NAME == "SERVER 2":
        color = "#9b59b6" # Ungu
    else:
        color = "#2ecc71" # Hijau
        
    ip_address = socket.gethostbyname(socket.gethostname())
    
    html = f"""
    <html>
    <head><title>{SERVER_NAME}</title></head>
    <body style="background-color: #1a1a1a; color: white; font-family: sans-serif; text-align: center; padding: 50px;">
        <div style="border-top: 5px solid {color}; padding: 30px; background-color: #2c3e50; display: inline-block; border-radius: 10px;">
            <h1 style="color: {color};">{SERVER_NAME}</h1>
            <hr>
            <p><b>IP Address:</b> {ip_address}</p>
            <p><b>Waktu Proses (Delay):</b> {delay_ms}ms</p>
            <br>
            <p style="font-size: 12px; color: #bdc3c7;">Fikran - 105841119623</p>
        </div>
    </body>
    </html>
    """
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)