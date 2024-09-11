from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/Ejercicio1', methods=['POST'])
def Ejercicio1():
    datos = request.get_json()

    if 'cadena' not in datos:
        return jsonify({'error': 'Falta el parámetro "cadena".'}), 400

    cadena = datos['cadena']

    cadena_procesada = False
    cadena_procesada = (cadena == cadena[::-1])
    return jsonify(cadena_procesada)

if __name__ == '__main__':
    app.run(debug=True)