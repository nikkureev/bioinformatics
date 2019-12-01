import matplotlib.pyplot as plt
from networkx import nx

a, b, c, d, e, f = ('a', 'b', 'c', 'd', 'e', 'f')
G = nx.Graph()
G.add_edge(a, b)
G.add_edge(b, c)
G.add_edge(c, b)
G.add_edge(c, a)
G.add_edge(c, d)
G.add_edge(d, e)
G.add_edge(e, f)
G.add_edge(f, d)

for line in nx.generate_adjlist(G):
    print(line)

nx.draw(G, with_labels=True)
plt.show()
