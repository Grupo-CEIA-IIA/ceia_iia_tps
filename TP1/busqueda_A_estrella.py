import heapq

class TorreDeHanoi:
    def __init__(self, num_discos):
        """Inicializa el problema con el número de discos y los estados inicial y final."""
        self.num_discos = num_discos
        self.estado_inicial = ((1, 2, 3, 4, 5), (), ())  # Representación de las torres
        self.estado_final = ((), (), (1, 2, 3, 4, 5))  # Estado objetivo donde todos los discos están en la tercera torre
        self.visitados = set()  # Conjunto para almacenar los estados visitados y evitar ciclos

    def heuristica(self, estado):
        """Heurística: Cantidad de discos que aún no están en la torre final."""
        return sum(1 for torre in estado[:2] for _ in torre)

    def generar_movimientos(self, estado):
        """Genera todos los movimientos posibles desde el estado actual."""
        movimientos = []
        for i in range(3):  # Itera sobre cada torre
            if estado[i]:  # Si la torre tiene discos
                disco = estado[i][0]  # Toma el disco superior
                for j in range(3):  # Intenta moverlo a otra torre
                    if i != j and (not estado[j] or estado[j][0] > disco):  # Regla de movimiento válido
                        nuevo_estado = list(map(tuple, estado))  # Copia del estado actual
                        nuevo_estado[i] = tuple(nuevo_estado[i][1:])  # Remueve el disco de la torre de origen
                        nuevo_estado[j] = (disco,) + nuevo_estado[j]  # Agrega el disco a la torre destino
                        movimientos.append(tuple(nuevo_estado))  # Agrega el nuevo estado a la lista de movimientos
        return movimientos

    def resolver(self):
        """Resuelve la Torre de Hanoi usando el algoritmo A*."""
        frontera = []  # Cola de prioridad para A*
        heapq.heappush(frontera, (self.heuristica(self.estado_inicial), 0, self.estado_inicial, []))  # (costo estimado, costo real, estado, camino)
        
        while frontera:
            _, costo, estado, pasos = heapq.heappop(frontera)  # Extrae el estado con menor costo estimado
            
            if estado == self.estado_final:
                return pasos  # Retorna la secuencia de movimientos si se alcanza el estado objetivo
            
            if estado in self.visitados:
                continue  # Si el estado ya fue visitado, lo ignora
            
            self.visitados.add(estado)  # Marca el estado como visitado
            
            for nuevo_estado in self.generar_movimientos(estado):
                nuevo_costo = costo + 1  # Cada movimiento tiene un costo de 1
                heapq.heappush(frontera, (nuevo_costo + self.heuristica(nuevo_estado), nuevo_costo, nuevo_estado, pasos + [nuevo_estado]))  # Agrega el nuevo estado a la cola de prioridad
        
        return []  # Retorna una lista vacía si no encuentra solución

# Ejecución del algoritmo
hanoi = TorreDeHanoi(5)
solucion = hanoi.resolver()
for paso in solucion:
    print(paso)  # Imprime cada estado intermedio de la solución