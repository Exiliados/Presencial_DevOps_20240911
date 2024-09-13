from flask import Flask, jsonify, request
import statistics


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

#Ejercicio 11
def sumar_borde(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])

    if filas <= 1 or columnas <= 1:
        return sum(sum(fila) for fila in matriz)

    suma = 0
    # Primera fila
    suma += sum(matriz[0])
    # Última fila
    suma += sum(matriz[-1])
    # Columnas intermedias (excluyendo primera y última fila)
    for i in range(1, filas - 1):
        suma += matriz[i][0] + matriz[i][-1]

    return suma

@app.route('/Ejercicio11', methods=['POST'])
def Ejercicio11():
    data = request.get_json()

    if 'matriz' not in data:
        return jsonify({'error': 'Falta el parámetro "matriz".'})

    matriz = data['matriz']
    suma_borde = sumar_borde(matriz)

    return jsonify({'suma_borde': suma_borde})


#Ejercicio 12
def suma_esquinas(matriz):
  filas = len(matriz)
  columnas = len(matriz[0])

  if filas <= 1 or columnas <= 1:
      return sum(sum(fila) for fila in matriz)

  suma = 0
  suma += matriz[0][0] 
  suma += matriz[0][-1] 
  suma += matriz[-1][0] 
  suma += matriz[-1][-1]

  return suma

@app.route('/Ejercicio12', methods=['POST'])
def Ejercicio12():
    data = request.get_json()

    if 'matriz' not in data:
        return jsonify({'error': 'Falta el parámetro "matriz".'})

    matriz = data['matriz']

    # Validar que la matriz sea rectangular
    if not all(len(fila) == len(matriz[0]) for fila in matriz):
        return jsonify({'error': 'La matriz debe ser rectangular.'})

    suma_esquinas_resultado = suma_esquinas(matriz)

    return jsonify({'suma_esquinas': suma_esquinas_resultado})

#Ejercicio 13
def silla(matriz):
    puntos_silla = []

    for i in range(len(matriz)):  # Iterar sobre las filas
        for j in range(len(matriz[i])):  # Iterar sobre las columnas

            es_minimo_fila = matriz[i][j] == min(matriz[i])  # ¿Es el mínimo de su fila?
            es_maximo_columna = matriz[i][j] == max([fila[j] for fila in matriz])  # ¿Es el máximo de su columna?

            if es_minimo_fila and es_maximo_columna:
                puntos_silla.append((i, j))

    return puntos_silla

@app.route('/Ejercicio13', methods=['POST'])
def Ejercicio13():
    data = request.get_json()

    if 'matriz' not in data:
        return jsonify({'error': 'Falta el parámetro "matriz".'})

    matriz = data['matriz']

    # Validar que la matriz sea rectangular
    if not all(len(fila) == len(matriz[0]) for fila in matriz):
        return jsonify({'error': 'La matriz debe ser rectangular.'})

    puntos_silla_resultado = silla(matriz)

    return jsonify({'puntos_silla': puntos_silla_resultado})


#Ejercicio 14
from flask import Flask, request, jsonify

app = Flask(__name__)

def traspuesta(matriz):
  filas = len(matriz)
  columnas = len(matriz[0])

  # Crear una nueva matriz con dimensiones intercambiadas
  matriz_traspuesta = [[0 for _ in range(filas)] for _ in range(columnas)]

  # Llenar la matriz traspuesta
  for i in range(filas):
      for j in range(columnas):
          matriz_traspuesta[j][i] = matriz[i][j]

  return matriz_traspuesta

@app.route('/Ejercicio14', methods=['POST'])
def Ejercicio14():
    data = request.get_json()

    if 'matriz' not in data:
        return jsonify({'error': 'Falta el parámetro "matriz".'})

    matriz = data['matriz']

    # Validar que la matriz sea rectangular
    if not all(len(fila) == len(matriz[0]) for fila in matriz):
        return jsonify({'error': 'La matriz debe ser rectangular.'})

    matriz_traspuesta = traspuesta(matriz)

    return jsonify({'matriz_traspuesta': matriz_traspuesta})


#Ejercicio 15
def dp_suma(matriz):
  filas = len(matriz)
  columnas = len(matriz[0])

  if filas != columnas:
      return "Error: La matriz no es cuadrada."

  suma = 0
  for i in range(filas):
      for j in range(i + 1, columnas):  # Iterar solo por encima de la diagonal
          suma += matriz[i][j]

  return suma

@app.route('/Ejercicio15', methods=['POST'])
def Ejercicio15():
    data = request.get_json()

    if 'matriz' not in data:
        return jsonify({'error': 'Falta el parámetro "matriz".'})

    matriz = data['matriz']

    resultado_dp_suma = dp_suma(matriz)

    if isinstance(resultado_dp_suma, str):  # Manejar el caso de error
        return jsonify({'error': resultado_dp_suma})
    else:
        return jsonify({'dp_suma': resultado_dp_suma})

#Ejercicio 16
def contar_subcadena(cadena, subcadena):
    contador = 0
    inicio = 0

    while inicio < len(cadena):
        posicion = cadena.find(subcadena, inicio)  # Buscar la subcadena desde la posición 'inicio'
        if posicion == -1:  # Si no se encuentra, terminar el bucle
            break
        contador += 1
        inicio = posicion + 1  # Actualizar la posición de inicio para la siguiente búsqueda

    return contador

@app.route('/Ejercicio16', methods=['POST'])
def Ejercicio16():
    data = request.get_json()

    if 'cadena' not in data or 'subcadena' not in data:
        return jsonify({'error': 'Faltan parámetros. Se requiere "cadena" y "subcadena".'})

    cadena = data['cadena']
    subcadena = data['subcadena']

    num_ocurrencias = contar_subcadena(cadena, subcadena)

    return jsonify({'cadena': cadena, 'subcadena': subcadena, 'num_ocurrencias': num_ocurrencias})

#Ejercicio 17
def es_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False

    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6

    return True

@app.route('/Ejercicio17', methods=['POST'])
def Ejercicio17():
    data = request.get_json()

    if 'numero' not in data:
        return jsonify({'error': 'Falta el parámetro "numero".'})

    try:
        numero = int(data['numero'])
    except ValueError:
        return jsonify({'error': 'El parámetro "numero" debe ser un número entero.'})

    es_primo_resultado = es_primo(numero)

    return jsonify({'numero': numero, 'es_primo': es_primo_resultado})

#Ejercicio 18
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

@app.route('/Ejercicio18', methods=['POST'])
def Ejercicio18():
    data = request.get_json()

    if 'numero' not in data:
        return jsonify({'error': 'Falta el parámetro "numero".'})
    
    try:
        numero = int(data['numero'])
        if numero < 0:
            raise ValueError("El número debe ser no negativo.")
    except ValueError as e:
        return jsonify({'error': str(e)})

    resultado_factorial = factorial(numero)

    return jsonify({'numero': numero, 'factorial': resultado_factorial})

#Ejercicio 19
def ordenar_por_longitud(arreglo):
    return sorted(arreglo, key=len)

@app.route('/Ejercicio19', methods=['POST'])
def Ejercicio19():
    data = request.get_json()

    if 'arreglo' not in data:
        return jsonify({'error': 'Falta el parámetro "arreglo".'})

    arreglo = data['arreglo']

    # Validar que el arreglo contenga solo cadenas
    if not all(isinstance(elemento, str) for elemento in arreglo):
        return jsonify({'error': 'El arreglo debe contener solo cadenas.'})

    arreglo_ordenado = ordenar_por_longitud(arreglo)

    return jsonify({'arreglo_ordenado': arreglo_ordenado})

#Ejercicio 20
def estadistica(numeros):
  media = statistics.mean(numeros)
  desviacion_estandar = statistics.stdev(numeros)

  return {'media': media, 'desviacion_estandar': desviacion_estandar}

@app.route('/Ejercicio20', methods=['POST'])
def Ejercicio20():
    data = request.get_json()

    if 'numeros' not in data:
        return jsonify({'error': 'Falta el parámetro "numeros".'})

    numeros = data['numeros']

    # Validar que el arreglo contenga solo números
    if not all(isinstance(elemento, (int, float)) for elemento in numeros):
        return jsonify({'error': 'El arreglo debe contener solo números.'})

    resultado_estadistica = estadistica(numeros)

    return jsonify(resultado_estadistica)



if __name__ == '__main__':
    app.run(debug=True)