from flask import Flask, jsonify, send_file
from flask_cors import CORS
import requests
from io import BytesIO

app = Flask(__name__)
CORS(app)  # Habilitar CORS para permitir solicitudes desde el dashboard

# Ruta al archivo de Dropbox
DROPBOX_URL = "https://www.dropbox.com/scl/fi/b9tkioj9jqn3784dx669z/Diciembre-Reportes.txt?rlkey=nj2k7po73atgxkzn8mnfjqwix&e=1&st=x67mgytu&dl=1"

@app.route('/fetch-file', methods=['GET'])
def fetch_file():
    try:
        # Descargar el archivo desde Dropbox
        response = requests.get(DROPBOX_URL)
        response.raise_for_status()
        file_content = response.content
        return send_file(BytesIO(file_content), as_attachment=False, mimetype='text/plain', download_name='Diciembre-Reportes.txt')
    except requests.RequestException as e:
        return jsonify({'error': f'Error al descargar el archivo: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
