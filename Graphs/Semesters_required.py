def semesters_required(num_courses, prereqs):
    graph = build_graph(num_courses, prereqs)
    distance = {}
    for course in graph:
        if len(graph[course]) == 0:
            distance[course] = 1
    for node in graph:
        traverse_distance(graph, node, distance)
    return max(distance.values())


def traverse_distance(graph, node, distance):
    if node in distance:
        return distance[node]
    max_distance = 0
    for neighbor in graph[node]:
        neighbor_distance = traverse_distance(graph, neighbor, distance)
        if neighbor_distance > max_distance:
            max_distance = neighbor_distance
    distance[node] = 1 + max_distance
    return distance[node]


def build_graph(num_courses, prereqs):
    graph = {}
    for course in range(num_courses):
        graph[course] = []
    for prereq in prereqs:
        a, b = prereq
        graph[a].append(b)
    return graph


num_courses = 6
prereqs = [
    (1, 2),
    (2, 4),
    (3, 5),
    (0, 5),
]
print(semesters_required(num_courses, prereqs))
