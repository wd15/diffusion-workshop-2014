import pydot
import itertools

graph = pydot.Dot(graph_type='digraph', fontnames="gs", splines='curved', bgcolor='transparent')

style = 'filled, rounded, dotted'
color = '#99d8c9'
other_color = '#deebf7'
arrow_color = 'black'
other_arrow_color = 'black'

other_names = ("reformulate", "debug", "change\nparameters", "review")
other_nodes = [pydot.Node(n, style='filled', fillcolor=other_color, fontname="Bitstream-Vera Sans", shape='ellipse', penwidth=0) for n in other_names]



names = ("prototype", "develop", "simulate", "analyze", "disseminate")
nodes = [pydot.Node(n, style=style, fillcolor=color, fontname="Bitstream-Vera Sans", shape='box', penwidth=0) for n in names]

nodes[2] = pydot.Node('simulate', style=style, fillcolor='#fc9272', fontname="Bitstream-Vera Sans", shape='box', penwidth=0)
                      
for node in nodes + other_nodes:
    graph.add_node(node)

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return itertools.izip(a, b)

for x, y in pairwise(nodes):
    graph.add_edge(pydot.Edge(x, y, color=arrow_color))


for i, n in enumerate(other_nodes):
    graph.add_edge(pydot.Edge(nodes[i+1], n, color=other_arrow_color))
    graph.add_edge(pydot.Edge(n, nodes[i], color=other_arrow_color))

# cluster = pydot.Cluster('cluster', label='simulation mangement')
# cluster.add_node(nodes[1])
# cluster.add_node(nodes[2])
# cluster.add_node(other_nodes[2])
# cluster.add_node(nodes[3])
# graph.add_subgraph(cluster)

    
graph.write_png('images/workflow.png')

