import networkx as nx
import matplotlib.pyplot as plt


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

pos = nx.spring_layout(metro_graph)
nx.draw(
    metro_graph,
    pos,
    with_labels=True,
    font_size=8,
    node_size=700,
    node_color="skyblue",
    font_color="black",
    font_weight="bold",
    arrowsize=10,
)
plt.title("Київське метро")
plt.show()

num_nodes = metro_graph.number_of_nodes()
num_edges = metro_graph.number_of_edges()

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")

degree_dict = dict(metro_graph.degree())
print("\nСтупінь кожної вершини:")
for station, degree in degree_dict.items():
    print(f"{station}: {degree}")
