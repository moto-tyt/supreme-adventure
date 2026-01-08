class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
    
    def add_child(self, child_node):
        self.children.append(child_node)
    def display(self, level=0):
        print("  " * level + str(self.value))
        for child in self.children:
            child.display(level + 1)
        

def main():
    root = Node("Root")
    child1 = Node("Child 1")
    child2 = Node("Child 2")

    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node("Grandchild 1"))
    child1.add_child(Node("Grandchild 2"))

    root.display()

    print("this is children of root", root.children)
    print("this is children of child1", child1.children)
    print("this is children of child2", child2.children)

if __name__ == "__main__":
    main()