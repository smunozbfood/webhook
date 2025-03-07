from pyngrok import ngrok

ngrok.set_auth_token("2twdNg8aUXmK10fRZFldyzr2uCC_2Bp35KpF3vmcyzJMp38KS")  # Reemplaza con tu token
from flask import Flask, request, jsonify
from pyngrok import ngrok

# Iniciar Flask
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    # Imprimir los datos recibidos
    print('Datos recibidos desde Buk:', data)
    # Procesar la información recibida (por ejemplo, guardar en base de datos, etc.)
    if 'empleados' in data:
        for empleado in data['empleados']:
            print(f"Empleado: {empleado['nombre']} - ID: {empleado['id']}")

    # Devolver los mismos datos que recibiste (o una respuesta personalizada)
    return jsonify(data), 200

# Crear túnel con ngrok
public_url = ngrok.connect(5000)
print('La URL pública es:', public_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
