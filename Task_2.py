from collections import deque
import networkx as nx
import matplotlib.pyplot as plt


def visualize_graph(graph, title="Graph"):
    pos = nx.spring_layout(graph)
    nx.draw(
        graph,
        pos,
        with_labels=True,
        font_size=8,
        node_size=700,
        node_color="skyblue",
        font_color="black",
        font_weight="bold",
        arrowsize=10,
    )
    plt.title(title)
    plt.show()


def dfs_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for neighbor in graph.neighbors(start):
        if neighbor not in path:
            new_paths = dfs_paths(graph, neighbor, end, path)
            for p in new_paths:
                paths.append(p)
    return paths


def bfs_paths(graph, start, end):
    queue = [(start, [start])]
    paths = []
    while queue:
        current, path = queue.pop(0)
        for neighbor in graph.neighbors(current):
            if neighbor not in path:
                new_path = path + [neighbor]
                queue.append((neighbor, new_path))
                if neighbor == end:
                    paths.append(new_path)
    return paths


metro_graph = nx.Graph()
metro_graph.add_edges_from(
    [
        ("Shuliavska", "Vokzalna"),
        ("Vokzalna", "Universytet"),
        ("Universytet", "Teatralna"),
        ("Teatralna", "Khreshchatyk"),
        ("Khreshchatyk", "Arsenalna"),
        ("Arsenalna", "Hidropark"),
        ("Khreshchatyk", "Maidan Nezalezhnosti"),
        ("Maidan Nezalezhnosti", "Poshtova Ploscha"),
        ("Poshtova Ploscha", "Kontraktova Ploscha"),
        ("Kontraktova Ploscha", "Plosha Tarasa Shevchenka"),
        ("Lva Tolstogo", "Maidan Nezalezhnosti"),
        ("Olimpiyska", "Lva Tolstogo"),
        ("Palats Ukraina", "Olimpiyska"),
        ("Lybidska", "Palats Ukraina"),
        ("Osokorky", "Slavutych"),
        ("Slavutych", "Vydubichy"),
        ("Vydubichy", "Druzhby Narodiv"),
        ("Druzhby Narodiv", "Pecherska"),
        ("Pecherska", "Klovska"),
        ("Klovska", "Palats Sportu"),
        ("Palats Sportu", "Lva Tolstogo"),
        ("Palats Sportu", "Zoloti Vorota"),
        ("Zoloti Vorota", "Teatralna"),
        ("Zoloti Vorota", "Lukiyanivska"),
        ("Lukiyanivska", "Dorogozhychy"),
    ]
)

visualize_graph(metro_graph, "Київське метро")

start_station = "Dorogozhychy"
end_station = "Vokzalna"

dfs_tree = dfs_paths(metro_graph, start_station, end_station)
bfs_tree = bfs_paths(metro_graph, start_station, end_station)
