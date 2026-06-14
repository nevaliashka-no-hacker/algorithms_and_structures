class Graph:
    def __init__(self):
        self.vertexs = {}

    def add_top(self, top):
        if top not in self.vertexs:
            self.vertexs[top] = set()
            print("add vertex")

    def add_edge(self, edge, top):
        if top not in self.vertexs:
            self.add_top(top)
        if edge not in self.vertexs:
            self.add_top(edge)

        if edge in self.vertexs[top]:
            print("edge already exists")
            return

        self.vertexs[top].add(edge)
        self.vertexs[edge].add(top)
        print("add edge")

    def remove_top(self, top):
        if not self.search_top(top):
            print("no this top in graph")
            return 

        for edge in list(self.vertexs[top]):
            self.vertexs[edge].discard(top)

        del self.vertexs[top]
        print("remove top")

    def search_top(self, top):
        if top in self.vertexs:
            return True
        return False

    def neighbors(self, top):
        if not self.search_top(top):
            print("no this top in graph")
            return []

        return list(self.vertexs[top])

    def has_edge(self, edge, top):
        if not self.search_top(top):
            return False
        return edge in self.vertexs[top]

    def show_top(self):
        print(list(self.vertexs.keys()))

    def show(self):
        for top, edges in self.vertexs.items():
            print(f"{top} -> {list(edges)}")

    def degree(self, top):
        if not self.search_top(top):
            return 0
        return len(self.vertexs[top])


graph = Graph()
graph.add_top("B")
graph.add_top("A")
graph.add_top("C")
graph.add_top("D")
graph.add_top("E")

graph.show()

graph.add_edge("A", "B")
graph.add_edge("E", "B")
graph.add_edge("A", "C")
graph.add_edge("A", "E")
graph.add_edge("D", "B")
graph.add_edge("D", "C")

graph.show()

print("A:", graph.degree("A"))
print("D:", graph.degree("D"))

graph.show_top()

print("neighbors:", graph.neighbors("A"))

graph.show()

print("A-B:", graph.has_edge("A", "B")) 
print("C-E:", graph.has_edge("C", "E")) 

graph.remove_top("D")
graph.show()
print("neighbors B after remove D:", graph.neighbors("B"))
