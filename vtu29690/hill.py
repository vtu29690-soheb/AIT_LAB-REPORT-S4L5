graph={
    'A':{'B':2, 'D':4},
    'B':{'C':3, 'A':2},
    'C':{'B':3, 'D':1},
    'D':{'A':4, 'C':1}
    }
print(f"Cost from A to B is: {graph['A']['B']}")
print(f"Cost from B to C is: {graph['B']['C']}")
print(f"Cost from C to D is: {graph['C']['D']}")
print(f"Cost from D to A is: {graph['D']['A']}")

total_cost = 0
edges_visited = set()

for start_node, edges in graph.items():
    for end_node, cost in edges.items():
        edge=tuple(sorted([start_node, end_node]))
        if edge not in edges_visited:
            total_cost += cost
            edges_visited.add(edge)

print(f"Total cost of the Graph is: {total_cost}")
