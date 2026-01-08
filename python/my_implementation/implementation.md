**Graph Implementation in Python**
**Graph methods:**
`add_node(self, node)`
- add node to the graph class if the given node is not already in there.
- same node will not be created
***
`add_edges(self, node1, node2)`
- if its directed graph, calling add_edges once will only add one edges from node1 to node2
- if its undirected graph, calling add_edges will add both node1 to node2 and node2 to node1 edges
***
`print_graph(self)`
- print node -> which other node is connected  to that node.
***
`get_nodes(self)`
- return list of all the nodes in the graph
***
`get_edges(self)`
- return list of all the edges in the graph