def build_graph(edges,courses):
    graph = {}
    for course in range(courses):
        graph[course] = []
    for edge in edges:
        a,b = edge
        graph[a].append(b)
    return graph

prereqs = [
  (1, 2),
  (2, 4),
  (3, 5),
  (0, 5),
]

print(build_graph(prereqs,6))