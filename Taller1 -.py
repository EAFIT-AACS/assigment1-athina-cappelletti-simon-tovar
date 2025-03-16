import sys  # Importa el módulo sys, aunque no se usa en el código.
from collections import defaultdict  # Importa defaultdict para manejar transiciones sin inicializarlas manualmente.

def leer_automata():
    """Lee el autómata desde la entrada estándar."""
    while True:
        try:
            # Solicita el número de estados del autómata y lo convierte en entero.
            n = int(input("Ingrese el número de estados del autómata: ").strip())  
            if n <= 0:  # Verifica que el número de estados sea positivo.
                raise ValueError  # Lanza un error si el número no es válido.
            break  # Sale del bucle si la entrada es válida.
        except ValueError:
            print("Error: Debe ingresar un número entero positivo.")  # Muestra un mensaje de error.

    # Solicita los símbolos del alfabeto y los almacena en una lista.
    alfabeto = input("Ingrese los símbolos del alfabeto separados por espacios: ").strip().split()
    transiciones = {}  # Diccionario para almacenar las transiciones del autómata.

    while True:
        try:
            # Solicita los estados finales y los convierte en un conjunto de enteros.
            estados_finales = set(map(int, input("Ingrese los estados finales separados por espacios: ").strip().split()))
            break  # Sale del bucle si la entrada es válida.
        except ValueError:
            print("Error: Debe ingresar números enteros separados por espacios.")  # Mensaje de error si la entrada es inválida.

    print("Ingrese las transiciones en el formato: estado símbolo1 destino1 símbolo2 destino2 ...")
    for _ in range(n):  # Itera sobre cada estado del autómata.
        while True:
            try:
                # Lee la línea de entrada con el estado y sus transiciones.
                partes = input("Estado y sus transiciones: ").strip().split()
                estado = int(partes[0])  # Extrae el número del estado.
                transiciones[estado] = {}  # Inicializa el diccionario de transiciones para ese estado.
                if (len(partes) - 1) % 2 != 0:  # Verifica que haya un número par de elementos después del estado.
                    raise ValueError  # Lanza un error si el formato es incorrecto.
                for i in range(1, len(partes), 2):  # Itera sobre las transiciones en pares (símbolo, destino).
                    simbolo = partes[i]
                    destino = int(partes[i + 1])
                    transiciones[estado][simbolo] = destino  # Guarda la transición en el diccionario.
                break  # Sale del bucle si la entrada es válida.
            except (ValueError, IndexError):  # Captura errores de conversión o acceso fuera de índice.
                print("Error: Formato incorrecto. Asegúrese de ingresar el estado seguido de sus transiciones en pares (símbolo, destino).")
    
    return n, alfabeto, transiciones, estados_finales  # Devuelve los datos del autómata.

def obtener_estados_accesibles(n, transiciones):
    """Obtiene los estados accesibles desde el estado inicial (0)."""
    accesibles = set()  # Conjunto de estados accesibles.
    pendientes = {0}  # Conjunto de estados por explorar, comenzando desde el estado inicial (0).

    while pendientes:  # Mientras haya estados pendientes de explorar.
        estado = pendientes.pop()  # Obtiene y elimina un estado del conjunto de pendientes.
        if estado in accesibles:  # Si el estado ya fue visitado, lo ignora.
            continue
        accesibles.add(estado)  # Marca el estado como accesible.
        # Añade a pendientes los estados a los que se puede llegar desde el estado actual.
        for destino in transiciones.get(estado, {}).values():
            if destino not in accesibles:  # Solo añade estados no visitados.
                pendientes.add(destino)
    
    return accesibles  # Retorna el conjunto de estados accesibles.

def minimizar_afd(n, alfabeto, estados_finales, transiciones):
    """Minimiza el AFD dado y devuelve los pares de estados equivalentes."""
    accesibles = obtener_estados_accesibles(n, transiciones)  # Obtiene los estados accesibles.

    # Inicializa la partición de estados solo con estados accesibles.
    P = [estados_finales & accesibles, accesibles - estados_finales]
    W = [estados_finales & accesibles, accesibles - estados_finales]  # Cola de trabajo con los mismos grupos.

    while W:  # Mientras haya clases en la lista de trabajo.
        A = W.pop()  # Obtiene y elimina un conjunto de estados de la lista de trabajo.
        transiciones_inversas = defaultdict(set)  # Diccionario para almacenar transiciones inversas.

        for q in accesibles:  # Itera sobre los estados accesibles.
            for simbolo in alfabeto:  # Itera sobre cada símbolo del alfabeto.
                if simbolo in transiciones[q]:  # Verifica si hay una transición con ese símbolo.
                    destino = transiciones[q][simbolo]  # Obtiene el estado destino.
                    if destino in A:  # Si el destino pertenece al conjunto A.
                        transiciones_inversas[simbolo].add(q)  # Agrega el estado actual a la transición inversa.

        for simbolo, X in transiciones_inversas.items():  # Para cada conjunto de estados con la misma transición.
            for Y in P[:]:  # Itera sobre cada subconjunto de la partición.
                interseccion = X & Y  # Calcula la intersección de los estados con la partición.
                diferencia = Y - X  # Calcula la diferencia de estados.

                if interseccion and diferencia:  # Si el conjunto se divide en dos partes.
                    P.remove(Y)  # Remueve el conjunto original.
                    P.append(interseccion)  # Agrega la primera nueva partición.
                    P.append(diferencia)  # Agrega la segunda nueva partición.

                    if Y in W:  # Si el conjunto original estaba en la lista de trabajo.
                        W.remove(Y)  # Lo elimina.
                        W.append(interseccion)  # Agrega las nuevas particiones.
                        W.append(diferencia)
                    else:
                        # Agrega a la lista de trabajo el conjunto más pequeño para reducir iteraciones.
                        W.append(interseccion if len(interseccion) <= len(diferencia) else diferencia)

    pares_equivalentes = []  # Lista para almacenar pares de estados equivalentes.
    for grupo in P:  # Itera sobre cada grupo en la partición.
        grupo_ordenado = sorted(grupo)  # Ordena los estados dentro del grupo.
        for i in range(len(grupo_ordenado)):  # Recorre los estados ordenados.
            for j in range(i + 1, len(grupo_ordenado)):  # Compara cada par de estados dentro del grupo.
                pares_equivalentes.append((grupo_ordenado[i], grupo_ordenado[j]))  # Agrega el par a la lista.

    return pares_equivalentes  # Retorna la lista de estados equivalentes.

def principal():  
    """Función principal que gestiona la entrada y ejecución del programa."""
    while True:
        try:
            # Solicita el número de casos de prueba.
            c = int(input("Ingrese el número de casos de prueba: ").strip())  
            if c <= 0:  # Verifica que sea un número positivo.
                raise ValueError
            break
        except ValueError:
            print("Error: Debe ingresar un número entero positivo.")  # Muestra un mensaje de error.

    for i in range(1, c + 1):  # Ejecuta el código para cada caso de prueba.
        print(f"\nCaso de prueba {i}:")
        n, alfabeto, transiciones, estados_finales = leer_automata()  # Lee el autómata.
        estados_equivalentes = minimizar_afd(n, alfabeto, estados_finales, transiciones)  # Minimiza el AFD.

        print("\nEstados equivalentes después de la minimización:")
        if estados_equivalentes:
            print(" ".join(f"({x}, {y})" for x, y in sorted(estados_equivalentes)))  # Imprime los pares equivalentes.
        else:
            print("No hay estados equivalentes.")  
        print("---")

if __name__ == "__main__":
    principal()  # Ejecuta la función principal si el script se ejecuta directamente. 
