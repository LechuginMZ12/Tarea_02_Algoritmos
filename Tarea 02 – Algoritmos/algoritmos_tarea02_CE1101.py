import time
import random
import sys

# Aumenta el límite de recursión para manejar listas grandes
sys.setrecursionlimit(50000)

# ============================================================
# ALGORITMOS DE BÚSQUEDA
# ============================================================

def busqueda_lineal_iterativa(lista, objetivo):
    """
    Recorre la lista elemento por elemento de forma iterativa hasta encontrar el objetivo o agotar todos los elementos.
    Entradas: lista de elementos a recorrer.
    Salidas:  índice donde se encontró el objetivo, o -1 si no existe.
    Restricciones: la lista no debe estar vacía.
    """
    for i in range(len(lista)):          # Recorre cada posición de la lista
        if lista[i] == objetivo:          # Compara el elemento actual con el objetivo
            return i                      # Retorna el índice si lo encuentra
    return -1                             # Retorna -1 si no se encontró


def busqueda_lineal_recursiva(lista, objetivo, indice=0):
    """
    Recorre la lista de forma recursiva, comparando cada elemento con el objetivo hasta encontrarlo o llegar al final.
    Entradas: lista de elementos a recorrer.
    Salidas:  índice donde se encontró el objetivo, o -1 si no existe.
    Restricciones: la lista no debe estar vacía.
    """
    if indice >= len(lista):              # Caso base: se llegó al final sin encontrar
        return -1
    if lista[indice] == objetivo:         # Caso base: se encontró el objetivo
        return indice
    return busqueda_lineal_recursiva(lista, objetivo, indice + 1)  # Llamada recursiva


def busqueda_binaria_iterativa(lista, objetivo):
    """
    Busca un elemento en una lista ORDENADA dividiendo repetidamente el espacio de búsqueda a la mitad de forma iterativa.
    Entradas: lista ordenada de elementos.
    Salidas:  índice donde se encontró el objetivo, o -1 si no existe.
    Restricciones: la lista DEBE estar ordenada de menor a mayor.
    """
    izquierda = 0
    derecha = len(lista) - 1             # Define los límites inicial y final

    while izquierda <= derecha:           # Continúa mientras haya espacio de búsqueda
        medio = (izquierda + derecha) // 2  # Calcula el índice del punto medio
        if lista[medio] == objetivo:      # Encontró el objetivo en el centro
            return medio
        elif lista[medio] < objetivo:     # El objetivo está en la mitad derecha
            izquierda = medio + 1
        else:                             # El objetivo está en la mitad izquierda
            derecha = medio - 1
    return -1                             # No se encontró el objetivo


def busqueda_binaria_recursiva(lista, objetivo, izquierda=None, derecha=None):
    """
    Busca un elemento en una lista ORDENADA dividiendo recursivamente el espacio de búsqueda a la mitad.
    Entradas: lista ordenada de elementos.
    Salidas:  índice donde se encontró el objetivo, o -1 si no existe.
    Restricciones: la lista DEBE estar ordenada de menor a mayor.
    """
    # Inicializa los límites en la primera llamada
    if izquierda is None:
        izquierda = 0
    if derecha is None:
        derecha = len(lista) - 1

    if izquierda > derecha:              # Caso base: espacio de búsqueda agotado
        return -1

    medio = (izquierda + derecha) // 2   # Calcula el punto medio

    if lista[medio] == objetivo:          # Caso base: objetivo encontrado
        return medio
    elif lista[medio] < objetivo:         # Busca en la mitad derecha
        return busqueda_binaria_recursiva(lista, objetivo, medio + 1, derecha)
    else:                                 # Busca en la mitad izquierda
        return busqueda_binaria_recursiva(lista, objetivo, izquierda, medio - 1)


# ============================================================
# ALGORITMOS DE ORDENAMIENTO
# ============================================================

def ordenamiento_burbuja_iterativo(lista):
    """
    Ordena una lista comparando e intercambiando pares de elementos adyacentes de forma iterativa hasta que la lista quede completamente ordenada de menor a mayor.
    Entradas: lista de elementos comparables (números o strings).
    Salidas: nueva lista ordenada de menor a mayor.
    Restricciones: todos los elementos deben ser del mismo tipo y comparables entre sí.
    """
    lista = lista.copy()                  # Trabaja sobre una copia para no modificar la original
    n = len(lista)

    for i in range(n):                    # Itera n veces sobre la lista
        for j in range(0, n - i - 1):    # Cada pasada coloca el mayor al final
            if lista[j] > lista[j + 1]:  # Compara elementos adyacentes
                lista[j], lista[j + 1] = lista[j + 1], lista[j]  # Intercambia si está fuera de orden
    return lista


def _burbuja_recursiva_helper(lista, n):
    """
    Función auxiliar interna para el ordenamiento burbuja recursivo; realiza una pasada de la burbuja y se llama a sí misma reduciendo el tamaño del problema.
    Entradas: lista de elementos a ordenar.
    Salidas:  None.
    Restricciones: uso interno solamente.
    """
    if n <= 1:                            # Caso base: lista de un elemento ya está ordenada
        return
    for j in range(n - 1):               # Realiza una pasada de burbuja
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]
    _burbuja_recursiva_helper(lista, n - 1)  # Llamada recursiva con tamaño reducido


def ordenamiento_burbuja_recursivo(lista):
    """
    Ordena una lista usando el algoritmo de burbuja de forma recursiva, delegando cada pasada a una función auxiliar que reduce progresivamente el tamaño del problema.
    Entradas: lista de elementos comparables.
    Salidas: nueva lista ordenada de menor a mayor.
    Restricciones: todos los elementos deben ser del mismo tipo y comparables.
    """
    lista = lista.copy()                  # Trabaja sobre una copia
    _burbuja_recursiva_helper(lista, len(lista))
    return lista


def ordenamiento_seleccion_iterativo(lista):
    """
    Ordena una lista buscando iterativamente el elemento mínimo de la parte no ordenada y colocándolo en su posición correcta.
    Entradas: lista de elementos comparables.
    Salidas: nueva lista ordenada de menor a mayor.
    Restricciones: todos los elementos deben ser del mismo tipo y comparables entre sí.
    """
    lista = lista.copy()                  # Trabaja sobre una copia
    n = len(lista)

    for i in range(n):                    # Itera sobre cada posición de la lista
        indice_minimo = i                 # Asume que el mínimo es el elemento actual
        for j in range(i + 1, n):        # Busca el mínimo en la parte no ordenada
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j         # Actualiza el índice del mínimo encontrado
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]  # Coloca el mínimo en su lugar
    return lista


def _seleccion_recursiva_helper(lista, inicio, n):
    """
    Función auxiliar interna para el ordenamiento por selección recursivo; encuentra el mínimo desde 'inicio' y lo ubica correctamente, luego se llama a sí misma con el siguiente índice.
    Entradas: lista de elementos a ordenar.
    Salidas:  None.
    Restricciones: uso interno solamente.
    """
    if inicio >= n - 1:                   # Caso base: ya no hay más elementos por ordenar
        return
    indice_minimo = inicio
    for j in range(inicio + 1, n):        # Encuentra el índice del elemento mínimo
        if lista[j] < lista[indice_minimo]:
            indice_minimo = j
    lista[inicio], lista[indice_minimo] = lista[indice_minimo], lista[inicio]  # Ubica el mínimo
    _seleccion_recursiva_helper(lista, inicio + 1, n)  # Recurre sobre el resto


def ordenamiento_seleccion_recursivo(lista):
    """
    Ordena una lista mediante selección de forma recursiva, encontrando el mínimo de la sublista restante y colocándolo en su posición, reduciendo el problema en cada llamada.
    Entradas: lista de elementos comparables.
    Salidas: nueva lista ordenada de menor a mayor.
    Restricciones: todos los elementos deben ser del mismo tipo y comparables.
    """
    lista = lista.copy()                  # Trabaja sobre una copia
    _seleccion_recursiva_helper(lista, 0, len(lista))
    return lista


def ordenamiento_rapido_iterativo(lista):
    """
    Ordena una lista usando el algoritmo QuickSort de forma iterativa, empleando una pila explícita para simular la recursión y dividiendo la lista alrededor de un pivote.
    Entradas: lista de elementos comparables.
    Salidas:  nueva lista ordenada de menor a mayor.
    Restricciones: todos los elementos deben ser del mismo tipo y comparables.
    """
    lista = lista.copy()                  # Trabaja sobre una copia
    pila = [(0, len(lista) - 1)]          # Inicializa la pila con el rango completo

    while pila:                           # Procesa mientras haya rangos pendientes
        izquierda, derecha = pila.pop()   # Extrae el rango a procesar
        if izquierda >= derecha:
            continue

        # Partición: coloca el pivote en su posición correcta
        pivote = lista[derecha]           # Elige el último elemento como pivote
        i = izquierda - 1
        for j in range(izquierda, derecha):
            if lista[j] <= pivote:        # Si el elemento es menor o igual al pivote
                i += 1
                lista[i], lista[j] = lista[j], lista[i]  # Mueve elemento a la izquierda del pivote
        lista[i + 1], lista[derecha] = lista[derecha], lista[i + 1]  # Coloca el pivote en su lugar
        p = i + 1                         # Índice final del pivote

        pila.append((izquierda, p - 1))  # Agrega subarreglo izquierdo a la pila
        pila.append((p + 1, derecha))    # Agrega subarreglo derecho a la pila
    return lista


def ordenamiento_rapido_recursivo(lista):
    """
    Ordena una lista usando el algoritmo QuickSort de forma recursiva, seleccionando un pivote, particionando la lista en menores y mayores, y ordenando cada parte independientemente.
    Entradas: lista de elementos comparables.
    Salidas: nueva lista ordenada de menor a mayor.
    Restricciones: todos los elementos deben ser del mismo tipo y comparables.
    """
    if len(lista) <= 1:                   # Caso base: lista vacía o de un elemento
        return lista

    pivote = lista[len(lista) // 2]       # Elige el elemento del centro como pivote
    menores = [x for x in lista if x < pivote]   # Elementos menores al pivote
    iguales = [x for x in lista if x == pivote]  # Elementos iguales al pivote
    mayores = [x for x in lista if x > pivote]   # Elementos mayores al pivote

    # Combina recursivamente las tres partes
    return ordenamiento_rapido_recursivo(menores) + iguales + ordenamiento_rapido_recursivo(mayores)


# ============================================================
# ANÁLISIS DE TIEMPO COMPUTACIONAL
# ============================================================

def medir_tiempo(func, *args):
    """
    Mide el tiempo de ejecución de una función dada usando time.perf_counter() para máxima precisión.
    Entradas: func (callable) - función a ejecutar.
    Salidas: tiempo en segundos que tardó la función.
    Restricciones: la función recibida debe ser invocable (callable).
    """
    inicio = time.perf_counter()          # Marca el inicio del cronómetro
    func(*args)                           # Ejecuta la función con sus argumentos
    fin = time.perf_counter()             # Marca el fin del cronómetro
    return fin - inicio                   # Retorna el tiempo transcurrido


def generar_listas(n):
    """
    Genera tres variantes de lista de tamaño n: ordenada, desordenada (aleatoria) e invertida.
    Entradas: cantidad de elementos en cada lista.
    Salidas:  tupla (list, list, list) con lista ordenada, desordenada e invertida.
    Restricciones: n debe ser un entero positivo mayor que 0.
    """
    ordenada = list(range(1, n + 1))               # Lista de 1 a n en orden ascendente
    desordenada = random.sample(range(1, n + 1), n)  # Lista aleatoria sin repetición
    invertida = list(range(n, 0, -1))              # Lista de n a 1 en orden descendente
    return ordenada, desordenada, invertida


def ejecutar_analisis():
    """
    Ejecuta el análisis completo de tiempos para todos los algoritmos de búsqueda y ordenamiento con tamaños de lista de 10, 100, 1000 y 10000 elementos, imprimiendo los resultados en consola.
    Entradas: ninguna.
    Salidas:  imprime en consola una tabla de tiempos por algoritmo y tamaño.
    Restricciones: puede tardar varios segundos con n=10000 en algoritmos de complejidad O(n²) como burbuja y selección.
    """
    tamanios = [10, 100, 1000, 10000]    # Tamaños de prueba solicitados
    objetivo_factor = 0.5                 # El objetivo de búsqueda será el elemento del medio

    print("=" * 70)
    print("ANÁLISIS DE TIEMPO COMPUTACIONAL - CE1101 TAREA 02")
    print("=" * 70)

    # ---- Búsqueda lineal ----
    print("\n--- BÚSQUEDA LINEAL ---")
    print(f"{'Tamaño':<10} {'Ord-Iter(s)':<18} {'Ord-Rec(s)':<18} {'Desor-Iter(s)':<18} {'Desor-Rec(s)'}")
    for n in tamanios:
        ordenada, desordenada, _ = generar_listas(n)
        objetivo = ordenada[n // 2]      # Busca el elemento del medio

        t1 = medir_tiempo(busqueda_lineal_iterativa, ordenada, objetivo)
        t2 = medir_tiempo(busqueda_lineal_recursiva, ordenada, objetivo)
        t3 = medir_tiempo(busqueda_lineal_iterativa, desordenada, objetivo)
        t4 = medir_tiempo(busqueda_lineal_recursiva, desordenada, objetivo)
        print(f"{n:<10} {t1:<18.8f} {t2:<18.8f} {t3:<18.8f} {t4:.8f}")

    # ---- Búsqueda binaria ----
    print("\n--- BÚSQUEDA BINARIA (solo lista ordenada) ---")
    print(f"{'Tamaño':<10} {'Iterativa(s)':<18} {'Recursiva(s)'}")
    for n in tamanios:
        ordenada, _, _ = generar_listas(n)
        objetivo = ordenada[n // 2]

        t1 = medir_tiempo(busqueda_binaria_iterativa, ordenada, objetivo)
        t2 = medir_tiempo(busqueda_binaria_recursiva, ordenada, objetivo)
        print(f"{n:<10} {t1:<18.8f} {t2:.8f}")

    # ---- Ordenamiento burbuja ----
    print("\n--- ORDENAMIENTO BURBUJA ---")
    print(f"{'Tamaño':<10} {'Ord-Iter(s)':<18} {'Ord-Rec(s)':<18} {'Desor-Iter(s)':<18} {'Desor-Rec(s)':<18} {'Inv-Iter(s)':<18} {'Inv-Rec(s)'}")
    for n in tamanios:
        ordenada, desordenada, invertida = generar_listas(n)
        t1 = medir_tiempo(ordenamiento_burbuja_iterativo, ordenada)
        t2 = medir_tiempo(ordenamiento_burbuja_recursivo, ordenada)
        t3 = medir_tiempo(ordenamiento_burbuja_iterativo, desordenada)
        t4 = medir_tiempo(ordenamiento_burbuja_recursivo, desordenada)
        t5 = medir_tiempo(ordenamiento_burbuja_iterativo, invertida)
        t6 = medir_tiempo(ordenamiento_burbuja_recursivo, invertida)
        print(f"{n:<10} {t1:<18.8f} {t2:<18.8f} {t3:<18.8f} {t4:<18.8f} {t5:<18.8f} {t6:.8f}")

    # ---- Ordenamiento selección ----
    print("\n--- ORDENAMIENTO SELECCIÓN ---")
    print(f"{'Tamaño':<10} {'Ord-Iter(s)':<18} {'Ord-Rec(s)':<18} {'Desor-Iter(s)':<18} {'Desor-Rec(s)':<18} {'Inv-Iter(s)':<18} {'Inv-Rec(s)'}")
    for n in tamanios:
        ordenada, desordenada, invertida = generar_listas(n)
        t1 = medir_tiempo(ordenamiento_seleccion_iterativo, ordenada)
        t2 = medir_tiempo(ordenamiento_seleccion_recursivo, ordenada)
        t3 = medir_tiempo(ordenamiento_seleccion_iterativo, desordenada)
        t4 = medir_tiempo(ordenamiento_seleccion_recursivo, desordenada)
        t5 = medir_tiempo(ordenamiento_seleccion_iterativo, invertida)
        t6 = medir_tiempo(ordenamiento_seleccion_recursivo, invertida)
        print(f"{n:<10} {t1:<18.8f} {t2:<18.8f} {t3:<18.8f} {t4:<18.8f} {t5:<18.8f} {t6:.8f}")

    # ---- Ordenamiento rápido ----
    print("\n--- ORDENAMIENTO RÁPIDO ---")
    print(f"{'Tamaño':<10} {'Ord-Iter(s)':<18} {'Ord-Rec(s)':<18} {'Desor-Iter(s)':<18} {'Desor-Rec(s)':<18} {'Inv-Iter(s)':<18} {'Inv-Rec(s)'}")
    for n in tamanios:
        ordenada, desordenada, invertida = generar_listas(n)
        t1 = medir_tiempo(ordenamiento_rapido_iterativo, ordenada)
        t2 = medir_tiempo(ordenamiento_rapido_recursivo, ordenada)
        t3 = medir_tiempo(ordenamiento_rapido_iterativo, desordenada)
        t4 = medir_tiempo(ordenamiento_rapido_recursivo, desordenada)
        t5 = medir_tiempo(ordenamiento_rapido_iterativo, invertida)
        t6 = medir_tiempo(ordenamiento_rapido_recursivo, invertida)
        print(f"{n:<10} {t1:<18.8f} {t2:<18.8f} {t3:<18.8f} {t4:<18.8f} {t5:<18.8f} {t6:.8f}")

    print("\n" + "=" * 70)
    print("Análisis completado.")
    print("=" * 70)


# ============================================================
# PUNTO DE ENTRADA
# ============================================================

if __name__ == "__main__":
    # Ejecuta el análisis completo al correr el script directamente
    ejecutar_analisis()
