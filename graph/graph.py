
class Graph:
    def __init__(self):
        self.vertices = None

    def add_vertex(self, data):
        # create a new vertex
        v = Vertex(data)
        # make next of new vertex point where vertices is pointing to
        v.next = self.vertices
        # make vertices point to the new vertex
        self.vertices = v

    def connect(self, vfrom, vto, weight):
        # find vfrom and vto
        vf = self.find(vfrom)
        if vf is not None:
            vt = self.find(vto)
            # if found connect them
            if vt is not None:
                vf.connect(vt, weight)
                return True
        # reach this point? Some vertex not found
        return False

    def find(self, data):
        current = self.vertices
        while current is not None:
            if current.get_data() == data:
                return current
            current = current.get_next()
        return None

    def display(self):
        # start from where vertices points to
        current = self.vertices
        # loop as long as current points to an object and print each object
        while current is not None:
            print(current)
            current = current.get_next()

    def find_second_level_conn(self, d):
        current = self.find(d)
        con = current.edges
        while con is not None:
            edge = con.connection.edges
            while edge is not None:
                if edge.connection.data != current.data:
                    print(edge.connection.data)
                edge = edge.next
            con = con.next


class Vertex:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.edges = None

    def get_next(self):
        return self.next

    def get_data(self):
        return self.data

    def connect(self, v, w):
        edge = Edge(v, w)
        edge.next = self.edges
        self.edges = edge

    def __str__(self):
        text = self.data
        current = self.edges
        while current is not None:
            text += " [" + current.get_connection().get_data() + "," + str(current.get_weight()) + "]"
            current = current.get_next()
        return text


class Edge:
    def __init__(self, conn, w):
        self.connection = conn
        self.weight = w
        self.next = None

    def get_connection(self):
        return self.connection

    def get_weight(self):
        return self.weight

    def get_next(self):
        return self.next


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

    social.find_second_level_conn('B')
    social.find_second_level_conn('G')