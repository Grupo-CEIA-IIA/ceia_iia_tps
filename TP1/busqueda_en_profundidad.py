from aima_libs.hanoi_states import ProblemHanoi, StatesHanoi
from aima_libs.tree_hanoi import NodeHanoi


def breadth_first_search(number_disks=5):
    # Inicializamos el problema
    list_disks = [i for i in range(5, 0, -1)]
    initial_state = StatesHanoi(list_disks, [], [], max_disks=number_disks)
    goal_state = StatesHanoi([], [], list_disks, max_disks=number_disks)
    problem = ProblemHanoi(initial=initial_state, goal=goal_state)

    # Creamos una cola FIFO con el nodo inicial
    frontier = [NodeHanoi(problem.initial)]  

    # Creamos el set con estados ya visitados
    explored = set()
    
    node_explored = 0
    
    while len(frontier) != 0:
        node = frontier.pop()
        node_explored += 1
        
        # Agregamos el estado del nodo al set. Esto evita guardar duplicados, porque set nunca tiene elementos repetidos
        explored.add(node.state)
        
        if problem.goal_test(node.state):  # Comprobamos si hemos alcanzado el estado objetivo
            metrics = {
                "solution_found": True,
                "nodes_explored": node_explored,
                "states_visited": len(explored),
                "nodes_in_frontier": len(frontier),
                "max_depth": node.depth,
                "cost_total": node.state.accumulated_cost,
            }
            return node, metrics
        
        # Agregamos a la cola todos los nodos sucesores del nodo actual
        for next_node in node.expand(problem):
            # Solo si el estado del nodo no fue explorado
            if next_node.state not in explored:
                frontier.append(next_node)

    # Si no se encontro la solución, devolvemos la métricas igual
    metrics = {
        "solution_found": False,
        "nodes_explored": node_explored,
        "states_visited": len(explored),
        "nodes_in_frontier": len(frontier),
        "max_depth": node.depth, # OBS: Si no se encontró la solución, este valor solo tiene sentido en breadth_first_search, en otros casos se debe ir llevando registro de cual fue la máxima profundidad
        "cost_total": None,
    }
    return None, metrics

if __name__ == "__main__":
    solution, metrics = breadth_first_search(number_disks=5)
    for key, value in metrics.items():
        print(f"{key}: {value}")
    for nodos in solution.path():
        print(nodos)
    solution.generate_solution_for_simulator()
