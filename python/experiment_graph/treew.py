class Node:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.connections = []
    
    def add_edge(self, neighbor_node, bidirectional=True):
        """Add an edge to another node. If bidirectional, also add edge back."""
        if neighbor_node not in self.connections:
            self.connections.append(neighbor_node)
        if bidirectional and self not in neighbor_node.connections:
            neighbor_node.connections.append(self)

    def add_weight(self, weight):
        self.weight = weight

    def get_weight(self):
        return self.weight

    def get_value(self):
        return self.value

    def get_connections(self):
        return self.connections

    def display(self, level=0):
        print("  " * level + str(self.value))
        for child in self.connections:
            child.display(level + 1)
    
    def dijikstra(self):
        # Initialize distances dictionary for all reachable nodes
        distances = {}
        visited = set()
        queue = [self]
        distances[self] = 0
        
        while queue:
            current_node = queue.pop(0)
            if current_node in visited:
                continue
            visited.add(current_node)
            
            for neighbor in current_node.connections:
                # Cost to reach neighbor = current distance + neighbor's weight
                distance = distances[current_node] + neighbor.weight
                
                # Update if we found a shorter path
                if neighbor not in distances or distance < distances[neighbor]:
                    distances[neighbor] = distance
                    queue.append(neighbor)
        
        return distances
    def display_dijikstra(self):
        distances = self.dijikstra()
        for node, distance in distances.items():
            print(f"{node.get_value()}: {distance}")

def main():
    # Create nodes (name, weight)
    # Weight = cost to traverse through this node
    A = Node("A", 0)
    B = Node("B", 1)
    C = Node("C", 4)
    D = Node("D", 2)
    E = Node("E", 3)
    F = Node("F", 1)
    
    # Build a graph (not a tree!) - nodes are peers connected by edges
    A.add_edge(B)  # A <--> B
    A.add_edge(C)  # A <--> C
    A.add_edge(D)  # A <--> D
    B.add_edge(E)  # B <--> E
    C.add_edge(F)  # C <--> F
    D.add_edge(E)  # D <--> E
    D.add_edge(F)  # D <--> F
    
    print("Graph structure (bidirectional edges):")
    print("A(0) connects to: B(1), C(4), D(2)")
    print("B(1) connects to: A(0), E(3)")
    print("C(4) connects to: A(0), F(1)")
    print("D(2) connects to: A(0), E(3), F(1)")
    print("E(3) connects to: B(1), D(2)")
    print("F(1) connects to: C(4), D(2)")
    print("\nShortest distances from node A:")
    A.display_dijikstra() 

if __name__ == "__main__":
    main()