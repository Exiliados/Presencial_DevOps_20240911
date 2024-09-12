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

#Ejercicio 4
def maximin(arreglo):
    if not arreglo:
        return None, []
    
    # Encontrar el valor máximo
    maximo = max(arreglo)
    
    # Encontrar las posiciones en las que aparece el valor máximo
    posiciones = [i for i, num in enumerate(arreglo) if num == maximo]
    
    return maximo, posiciones

@app.route('/Ejercicio4', methods=['POST'])
def Ejercicio4():
    data = request.get_json()
    arreglo = data.get('arreglo', [])
    
    if not arreglo:
        return jsonify({"error": "No se proporcionó un arreglo válido"}), 400
    
    maximo, posiciones = maximin(arreglo)
    return jsonify({"maximo": maximo, "posiciones": posiciones})

#Ejercicio 5
def posearch(arreglo, valor):
    if not arreglo:
        return None

    # Inicializamos el valor más cercano con el primer elemento del arreglo
    mas_cercano = arreglo[0]
    posicion_cercano = 0

    # Buscamos el valor más cercano
    for i, num in enumerate(arreglo):
        if abs(num - valor) < abs(mas_cercano - valor):
            mas_cercano = num
            posicion_cercano = i
    
    return mas_cercano, posicion_cercano

@app.route('/Ejercicio5', methods=['POST'])
def Ejercicio5():
    data = request.get_json()
    arreglo = data.get('arreglo', [])
    valor = data.get('valor', None)
    
    if arreglo and valor is not None:
        mas_cercano, posicion_cercano = posearch(arreglo, valor)
        return jsonify({"valor_cercano": mas_cercano, "posicion": posicion_cercano})
    else:
        return jsonify({"error": "Falta el arreglo o el valor"}), 400

#Ejercicio 6
def histograma(arreglo):
    # Generar el histograma visual
    histograma_visual = {num: '*' * num for num in arreglo}
    return histograma_visual

@app.route('/Ejercicio6', methods=['POST'])
def Ejercicio6():
    data = request.get_json()
    arreglo = data.get('arreglo', [])
    
    if arreglo:
        histograma_visual = histograma(arreglo)
        return jsonify(histograma_visual)
    else:
        return jsonify({"error": "No se proporcionó un arreglo válido"}), 400

#Ejercicio 7
def intercala(arreglo1, arreglo2):
    # Usamos dos punteros para recorrer ambos arreglos
    i, j = 0, 0
    arreglo_intercalado = []
    
    # Mientras haya elementos en ambos arreglos
    while i < len(arreglo1) and j < len(arreglo2):
        if arreglo1[i] < arreglo2[j]:
            arreglo_intercalado.append(arreglo1[i])
            i += 1
        else:
            arreglo_intercalado.append(arreglo2[j])
            j += 1
    
    # Agregar los elementos restantes del primer arreglo
    while i < len(arreglo1):
        arreglo_intercalado.append(arreglo1[i])
        i += 1
    
    # Agregar los elementos restantes del segundo arreglo
    while j < len(arreglo2):
        arreglo_intercalado.append(arreglo2[j])
        j += 1
    
    return arreglo_intercalado

@app.route('/Ejercicio7', methods=['POST'])
def Ejercicio7():
    data = request.get_json()
    arreglo1 = data.get('arreglo1', [])
    arreglo2 = data.get('arreglo2', [])
    
    if arreglo1 is not None and arreglo2 is not None:
        arreglo_intercalado = intercala(arreglo1, arreglo2)
        return jsonify({"arreglo_intercalado": arreglo_intercalado})
    else:
        return jsonify({"error": "No se proporcionaron ambos arreglos"}), 400

#Ejercicio 8
def fibo(n):
    # Lista para almacenar la serie de Fibonacci
    serie = []
    a, b = 0, 1
    while a <= n:
        serie.append(a)
        a, b = b, a + b
    # Añadir el siguiente número de Fibonacci si es mayor a n
    if a > n:
        serie.append(a)
    return serie

@app.route('/Ejercicio8', methods=['POST'])
def Ejercicio8():
    data = request.get_json()
    n = data.get('n', 0)
    
    if isinstance(n, int) and n >= 0:
        serie_fibonacci = fibo(n)
        return jsonify({"serie_fibonacci": serie_fibonacci})
    else:
        return jsonify({"error": "El valor de 'n' debe ser un número entero no negativo"}), 400

#Ejercicio 9
def es_cuadrada(matriz):
    # Verifica si la matriz tiene el mismo número de filas y columnas
    if not matriz or not isinstance(matriz, list):
        return False
    num_filas = len(matriz)
    for fila in matriz:
        if not isinstance(fila, list) or len(fila) != num_filas:
            return False
    return True

@app.route('/Ejercicio9', methods=['POST'])
def Ejercicio9():
    data = request.get_json()
    matriz = data.get('matriz', [])
    
    if isinstance(matriz, list):
        es_cuadrada_matriz = es_cuadrada(matriz)
        return jsonify({"es_cuadrada": es_cuadrada_matriz})
    else:
        return jsonify({"error": "El valor de 'matriz' debe ser una lista"}), 400

#Ejercicio 10
def traza(matriz, izquierda_a_derecha):
    if not matriz or not isinstance(matriz, list) or not all(isinstance(fila, list) for fila in matriz):
        return "La matriz no es válida"
    
    num_filas = len(matriz)
    if not all(len(fila) == num_filas for fila in matriz):
        return "La matriz no es cuadrada"
    
    suma = 0
    if izquierda_a_derecha:
        for i in range(num_filas):
            suma += matriz[i][i]
    else:
        for i in range(num_filas):
            suma += matriz[i][num_filas - 1 - i]
    
    return suma

@app.route('/Ejercicio10', methods=['POST'])
def Ejercicio10():
    data = request.get_json()
    matriz = data.get('matriz', [])
    izquierda_a_derecha = data.get('izquierda_a_derecha', True)
    
    if isinstance(matriz, list) and isinstance(izquierda_a_derecha, bool):
        resultado = traza(matriz, izquierda_a_derecha)
        if isinstance(resultado, int):
            return jsonify({"traza": resultado})
        else:
            return jsonify({"error": resultado}), 400
    else:
        return jsonify({"error": "Datos de entrada no válidos"}), 400


if __name__ == '__main__':
    app.run(debug=True)