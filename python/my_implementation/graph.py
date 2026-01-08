from math import inf
from collections import deque


class Graph:
    def __init__(self, directed=False, weighted=False):
        self.graph = {}
        self.directed = directed
        self.weighted = weighted
        
    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edges(self, node1, node2, weight=0):
        #create empty list if first time node is seen
        if node1 not in self.graph:
            self.graph[node1] = []
        #add edge if not already in list
        if node2 not in self.graph[node1]:
            if not self.weighted:
                self.graph[node1].append({node2, weight})
            else:
                self.graph[node1].append(node2)
            self.add_node(node2)
            if not self.directed:
                if not self.weighted:
                    self.graph[node2].append((node1, weight))
                else:
                    self.graph[node2].append([node1])
            

        
    

    def change_weight(self, node1, node2):
        pass

    def print_graph(self):
        for node in self.graph:
            print(node, "->", self.graph[node])
    
    def get_nodes(self):
        return list(self.graph.keys())

    def get_edges(self):
        edges = []
        for node in self.graph:
            for neighbor in self.graph[node]:
                edges.append((node, neighbor))
        return edges
    
    def bfs(self, start_node):
        if self.directed:
            print("only work for nondirected graph")
            return None

        dist = {}
        pred = {}

        for node in self.graph:
            dist[node] = inf
            pred[node] = None
        dist[start_node] = 0

        queue = deque()
        queue.append(start_node)

        while queue:
            searching_variable = queue.popleft()
            for z in self.graph[searching_variable]:
                if dist[z] == inf:
                    dist[z] = dist[searching_variable] + 1
                    pred[z] = searching_variable
                    queue.append(z)
        return dist, pred
    
    def dfs(self, start_node):
        visited = set()
        stack = [start_node]

        while stack:
            node = stack.pop()

            if node not in visited:
                visited.add(node)
                print(f"Visiting: {node}")

                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        stack.append(neighbor)
        return visited

            







        

def test_implementation():
    print("Testing implementation\n")
    print("check add edges")
    a = Graph(weighted=True)
    a.add_node(0)
    a.add_edges(0, 1)
    a.print_graph()
    print("--------------------------------")
    g = Graph(directed=False)
    print("Testing adding nodes")
    g.add_node(0)
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_node(6)
    print("--------------------------------")
    print("Testing adding two same edges to the same node")
    g.add_edges(0, 1)
    g.add_edges(0, 2)
    g.add_edges(1, 2)
    g.add_edges(0, 2)
    g.add_edges(2, 3)
    g.add_edges(7, 8)
    g.print_graph()
    print("--------------------------------")
    print("Testing getting nodes")
    print(g.get_nodes())
    print("--------------------------------")
    print("Testing getting edges")
    print(g.get_edges())
    print("--------------------------------")
    g_bfs = Graph(directed=False)
    g_bfs.add_edges(0, 1)
    g_bfs.add_edges(0, 2)
    g_bfs.add_edges(1, 2)
    g_bfs.add_edges(1, 3)
    g_bfs.add_edges(2, 4)
    g_bfs.add_edges(3, 4)
    ans1, ans2 = g_bfs.bfs(1)
    print("dist", ans1, "pred", ans2)
    print("--------------------------------")
    print(g.dfs(0))
    print("------------------------------")



def main():
    
    print("Graph Implementation in Python")
    test_implementation()






if __name__ == "__main__":
    main()