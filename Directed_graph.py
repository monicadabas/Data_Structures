# Directed graph implementation using Adjacency linked list
# An array of size equal to number of vertices. Each elemet in the array will be a node with vertix value and
# a pointer to a linked list which will store the neighbors of that vertex
# each node of the linked list with have a weight and the neighbor vertex along with a point to the next
# neighbor of the vertex in array

# A = [1, 2, 3], A[0] = Node(val = 1, neighbors = LL().head), LL = neighbor1 -> neighbor2 -> None
# LL node = Node(val = neighbor vextex, weight = cost of edge, next = other neighbor of the vertex in array or None)

class GraphLLNode:
    def __init__(self, neighbor, weight, next=None):
        self.vertex = neighbor
        self.weight = weight
        self.next = next


class AdjacencyList:
    def __init__(self):
        self.head = None

    def add_node(self, n): # n is a GraphLLNode
        if self.head is None:
            self.head = n

        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = n

    def delete_node(self, vertex):
        if self.head is not None:
            if self.head.vertex == vertex:
                self.head = self.head.next
            else:
                current = self.head
                while current.next is not None and current.next.vertex != vertex:
                    current = current.next
                if current.next is not None:
                    current.next = current.next.next
                #else:
                #   print("Vertex {} is not the neighbor".format(vertex))

    def print_neighbors(self):
        if self.head is None:
            print("No Neighbors")
        else:
            current = self.head
            while current is not None:
                print("[{}, {}] -->".format(current.vertex, current.weight), end=" ")
                current = current.next
            print(current)


class GraphNode:
    def __init__(self, vertex):
        self.vertex = vertex
        self.neighbors = AdjacencyList()


class Graph:
    def __init__(self):
        self.vertices = []
        self.count = 0
        self.dict_of_vertices = {}

    def add_vertex(self, v):
        if v not in self.dict_of_vertices:
            self.vertices.append(GraphNode(v))
            self.dict_of_vertices[v] = self.count
            self.count += 1
        else:
            print("Vertex {} already in Graph".format(v))

    def get_number_of_vertices(self):
        return self.count

    def get_vertices(self):
        return list(self.dict_of_vertices.keys())

    def add_edge(self, start, end, weight=1):
        if self.count < 2 or start not in self.dict_of_vertices or end not in self.dict_of_vertices:
            print("Vertex {} or {} not in graph".format(start, end))

        else:
            start_index = self.dict_of_vertices[start]
            self.vertices[start_index].neighbors.add_node(GraphLLNode(end, weight))

    def delete_edge(self, start, end):
        if self.count < 2 or start not in self.dict_of_vertices or end not in self.dict_of_vertices:
            print("Vertex {} or {} not in graph".format(start, end))
        else:
            start_index = self.dict_of_vertices[start]
            self.vertices[start_index].neighbors.delete_node(end)

    def delete_vertex(self, vertex):
        if vertex not in self.dict_of_vertices:
            print("Vertex {} not in graph".format(vertex))

        else:
            # delete all the edges from other vertices to this vertex
            for index in range(self.count):
                self.delete_edge(self.vertices[index].vertex, vertex)

            # delete this vertex node from the array of vertices

            # we can either just delete the vertex node using del but that will be O(n) time operation
            # del self.vertices[self.dict_of_vertices[vertex]]
            # also delete the vertex from dictionary of vertices
            # del self.dict_of_vertices[vertex]

            # so instead we can swap the vertices at the index of vertex and the last index
            # and pop the last element from array since the order of vertices in array does not matter

            vertex_at_last_index = self.vertices[self.count-1].vertex
            index_of_vertex_to_be_deleted = self.dict_of_vertices[vertex]
            self.vertices[index_of_vertex_to_be_deleted], self.vertices[self.count-1] = \
                self.vertices[self.count-1], self.vertices[index_of_vertex_to_be_deleted]

            # make corresponding changes in dictionary to store the correct index of the vertices

            self.dict_of_vertices[vertex_at_last_index] = index_of_vertex_to_be_deleted

            del self.dict_of_vertices[vertex]
            self.count -= 1

    def print_graph(self):
        for i in range(self.count):
            print("{}: ".format(self.vertices[i].vertex),end='')
            self.vertices[i].neighbors.print_neighbors()


g = Graph()
a = ['A', 'B', 'C', 'D', 'E']
for v in a:
    g.add_vertex(v)

g.add_edge('A', 'B', 5)
g.add_edge('A', 'C', 10)
g.add_edge('B', 'C', 5)
g.add_edge('C', 'D', 5)
g.add_edge('D', 'E', 5)

g.delete_vertex('E')

g.print_graph()

