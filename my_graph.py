"""Connected Graphs
For:
    CPE202
    Section 5
    Winter 2020
Author:
    Richard Hua
"""
from my_vertex import Vertex

class MyGraph:
    """Connected Graph
    Contains algorithms using Breadth First Search and Depth First Search
    to find connected components (vertices and edges) of an undirected graph. Determines if graph is bipartite/bicolorable.

    RESTRICTIONS: NO BUILTIN LIST POP() OR DICTIONARY
    SUGGESTIONS: USE QUEUE FROM LAB3 AS QUEUE.

    Attributes:

        capacity (int): the capacity of the queue. The default capacity is 2,
                        but will be increased automatically.
        num_items (int): the number of items in the queue.
        arr (list): an array which contains the items in the queue.
    """
    def __init__(self, filename):
        """reads in the specification of a graph and creates a graph using an adjacency list representation. You may assume the graph is not empty and is a correct specification. E.g. each edge is represented by a pair of vertices between 1 and n. Note that the graph is not directed so each edge specified in the input file should appear on the adjacency list of each vertex of the two vertices associated with the edge.
        """
        self.is_bicolor = True
        with open(filename) as infile:
            for idx, line in enumerate(infile):
                line = line.split()
                if idx == 0:
                    self.num_vertices = int(line[0])
                    print('num vertices', self.num_vertices)
                    self.vertices = [None] * (self.num_vertices + 1) #empty 0 idx
                    for key in range(1, self.num_vertices + 1):
                        self.vertices[key] = Vertex(key)
                    # print(self.vertices)
                if idx > 1: # connected vertices
                    src = int(line[0])
                    dest = int(line[1])
                    print('src', src)
                    print('dest', dest)
                    if dest not in self.vertices[src].edges:
                        self.vertices[src].edges.append(dest)
                        self.vertices[src].num_edges += 1
                    if src not in self.vertices[dest].edges:
                        self.vertices[dest].edges.append(src)
                        self.vertices[dest].num_edges += 1

        # self.init_vertices(self.vertices)
        # num_vertices, adj = self.init_vertices(filename)
        # self.adj = adj

    def __eq__(self, other):
        return isinstance(other, MyGraph)\
        and (self.arr == other.arr)\
        and (self.capacity == other.capacity)\
        and (self.num_items == other.num_items)

    def __repr__(self):
        return 'MyGraph(num_verts=%s, Vertices=%s)'\
        % (self.num_vertices, self.vertices)

    def get_conn_components(self, is_dfs=True):
        """returns a list of lists. For example, if there are three connected components then you will return a list of three lists. The order of the sub-lists is not important. However each sub-list will contain the vertices (in ascending order) in the connected component represented by that list. Each vertex is represented by an integer from 1 to n. If a vertex has no edges it will be in a connected component containing only itself. This function shall call either dfs or bfs method depending on the value of the argument is_dfs: i.e. do DFS if is_dfs=True, otherwise do BFS.
        """
        self.init_vertices(self.vertices)

    def init_vertices(self):
        """set vertices attributes
        """
        # for vertex in self.vertices:

        # line = file.readlines() # returns list containing all lines
        # num_vertices = int(line[0])
        # num_edges = int(line[1])
        # line = line[2:]
        # self.vlist = [None] * self.num_vertices
        # # self.bicolorable = bool(num_vertices - num_edges == 1)
        # for i,pair in enumerate(line): # i.e. (3, 7) : pair of connected vertices
        #     pair = pair.split()
        #     print(pair)
        #     src = int(pair[0])
        #     dest = int(pair[1])
        #     if src not in self.vlist:
        #         self.vlist[i] = self.init_vertices(src)
        #     if dest not in self.vlist[src].edges:
        #         self.vlist[src].edges.append(dest)
        # vert = Vertex(vertex)
        # # vert.add_edge(dest)
        # return vert

    def dfs(self, vertex, component):
        """does dfs, finds connected components, and determines if the graph is bicolorable or not. If it is bicolorable, it is going to set the is_bicolor member variable to True, otherwise False. Takes two arguments, vertex (Vertex) and component (list). Returns a connected component as a list of vertex keys.
        """
        pass

    def bfs(self, vertex, component):
        """does bfs, finds connected components, and determines if the graph is bicolorable or not. If it is bicolorable, it is going to set the is_bicolor member variable to True, otherwise False. Takes two arguments, vertex (Vertex) and component (list). Returns a connected component as a list of vertex keys.
        """


    def bicolor(self):
        """returns True if the graph is bicolorable and false otherwise. i.e. It returns the value of is_bicolor.
        """
        return self.bicolorable
