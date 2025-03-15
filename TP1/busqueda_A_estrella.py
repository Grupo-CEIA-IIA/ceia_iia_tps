import heapq

class TorreDeHanoi:
    def __init__(self, num_discos):
        self.num_discos = num_discos
        self.estado_inicial = ((1, 2, 3, 4, 5), (), ())  # Representación de las torres
        self.estado_final = ((), (), (1, 2, 3, 4, 5))
        self.visitados = set()

    def heuristica(self, estado):
        """Heurística: Cantidad de discos fuera de la torre final"""
        return sum(1 for torre in estado[:2] for _ in torre)

    def generar_movimientos(self, estado):
        movimientos = []
        for i in range(3):
            if estado[i]:  # Si hay discos en la torre
                disco = estado[i][0]
                for j in range(3):
                    if i != j and (not estado[j] or estado[j][0] > disco):
                        nuevo_estado = list(map(tuple, estado))
                        nuevo_estado[i] = tuple(nuevo_estado[i][1:])
                        nuevo_estado[j] = (disco,) + nuevo_estado[j]
                        movimientos.append(tuple(nuevo_estado))
        return movimientos

    def resolver(self):
        frontera = []
        heapq.heappush(frontera, (self.heuristica(self.estado_inicial), 0, self.estado_inicial, []))
        
        while frontera:
            _, costo, estado, pasos = heapq.heappop(frontera)
            
            if estado == self.estado_final:
                return pasos
            
            if estado in self.visitados:
                continue
            
            self.visitados.add(estado)
            
            for nuevo_estado in self.generar_movimientos(estado):
                nuevo_costo = costo + 1
                heapq.heappush(frontera, (nuevo_costo + self.heuristica(nuevo_estado), nuevo_costo, nuevo_estado, pasos + [nuevo_estado]))
        
        return []

hanoi = TorreDeHanoi(5)
solucion = hanoi.resolver()
for paso in solucion:
    print(paso)