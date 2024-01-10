import networkx as nx
import matplotlib.pyplot as plt


def dijkstra(graph, start):
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.nodes)

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float("infinity"):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight["weight"]

            if distance < distances[neighbor]:
                distances[neighbor] = distance

        unvisited.remove(current_vertex)

    return distances


metro_graph = nx.Graph()
metro_graph.add_edges_from(
    [
        ("Shuliavska", "Vokzalna", {"weight": 3}),
        ("Vokzalna", "Universytet", {"weight": 2}),
        ("Universytet", "Teatralna", {"weight": 2}),
        ("Teatralna", "Khreshchatyk", {"weight": 2}),
        ("Khreshchatyk", "Arsenalna", {"weight": 2}),
        ("Arsenalna", "Hidropark", {"weight": 3}),
        ("Khreshchatyk", "Maidan Nezalezhnosti", {"weight": 1}),
        ("Maidan Nezalezhnosti", "Poshtova Ploscha", {"weight": 2}),
        ("Poshtova Ploscha", "Kontraktova Ploscha", {"weight": 2}),
        ("Kontraktova Ploscha", "Plosha Tarasa Shevchenka", {"weight": 2}),
        ("Lva Tolstogo", "Maidan Nezalezhnosti", {"weight": 2}),
        ("Olimpiyska", "Lva Tolstogo", {"weight": 2}),
        ("Palats Ukraina", "Olimpiyska", {"weight": 2}),
        ("Lybidska", "Palats Ukraina", {"weight": 2}),
        ("Osokorky", "Slavutych", {"weight": 3}),
        ("Slavutych", "Vydubichy", {"weight": 4}),
        ("Vydubichy", "Druzhby Narodiv", {"weight": 4}),
        ("Druzhby Narodiv", "Pecherska", {"weight": 3}),
        ("Pecherska", "Klovska", {"weight": 2}),
        ("Klovska", "Palats Sportu", {"weight": 2}),
        ("Palats Sportu", "Lva Tolstogo", {"weight": 1}),
        ("Palats Sportu", "Zoloti Vorota", {"weight": 2}),
        ("Zoloti Vorota", "Teatralna", {"weight": 1}),
        ("Zoloti Vorota", "Lukiyanivska", {"weight": 4}),
        ("Lukiyanivska", "Dorogozhychy", {"weight": 3}),
    ]
)

for start_station in metro_graph.nodes:
    shortest_paths = dijkstra(metro_graph, start_station)
    print(f"Найкоротші шляхи від `{start_station}`: {shortest_paths}<br>")
