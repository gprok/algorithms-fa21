
class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vname):
        v = Vertex(vname)
        self.vertices[vname] = v

    def connect(self, vfrom, vto, w):
        if vfrom in self.vertices and vto in self.vertices:
            self.vertices[vfrom].connect(self.vertices[vto], w)

    def display(self):
        for vertex in self.vertices:
            print(vertex, end=": ")
            for edge in self.vertices[vertex].edges:
                print(edge, end=" ")
            print()


class Vertex:
    def __init__(self, name):
        self.name = name
        self.edges = []

    def connect(self, v, w):
        e = Edge(v, w)
        self.edges.append(e)

    def __str__(self):
        return self.name


class Edge:
    def __init__(self, vto, w):
        self.vertex_to = vto
        self.weight = w

    def __str__(self):
        return self.vertex_to.name


if __name__ == '__main__':
    social = Graph()
    social.add_vertex("A")
    social.add_vertex("B")
    social.add_vertex("C")
    social.add_vertex("D")
    social.add_vertex("E")
    social.add_vertex("F")
    social.add_vertex("G")
    social.connect("A", "F", 45)
    social.connect("A", "B", 34)
    social.connect("B", "A", 90)
    social.connect("G", "D", 58)
    social.connect("D", "C", 27)
    social.display()
