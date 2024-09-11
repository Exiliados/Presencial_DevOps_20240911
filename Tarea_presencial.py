from flask import Flask, jsonify, request

app = Flask(__name__)

#Ejercicio 1
def palindromo(cadena):
   return cadena == cadena[::-1]

@app.route('/Ejercicio1', methods=['POST'])
def Ejercicio1():
    datos = request.get_json()

    #Hay que pasarle un json con el campo cadena y el string a procesar en el valor
    if 'cadena' not in datos:
        return jsonify({'error': 'Falta el parámetro "cadena".'}), 400

    cadena = datos['cadena']

    cadena_procesada = palindromo(cadena)
    return jsonify(cadena_procesada)

#Ejercicio 2
def invertir(cadena):
    return cadena[::-1]

@app.route('/Ejercicio2', methods=['POST'])
def Ejercicio2():
    datos = request.get_json()
    if 'cadena' not in datos:
        return jsonify({'error': 'Falta el parámetro "cadena".'}), 400
    
    return jsonify(invertir(datos['cadena']))

#Ejercicio 3
def coincidencia(frase, palabra):
    palabras = frase.split()
    contador = 0

    for i in palabras:
        if palabra == i:
            contador +=1
    return contador

@app.route('/Ejercicio3', methods=['POST'])
def Ejercicio3():
    datos = request.get_json()
    frase = datos['frase']
    palabra = datos['palabra']
    cantidadCoincidencias = coincidencia(frase,palabra)
    
    return jsonify(cantidadCoincidencias)


if __name__ == '__main__':
    app.run(debug=True)