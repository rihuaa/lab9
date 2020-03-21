"""Vertex and Edge class data definitions for my_graph
For:
    CPE202
    Section 5
    Winter 2020
Author:
    Richard Hua
"""
from linked_list import Node

class Vertex:
    """class for Vertex
    Attributes:
        key (int) : key
        val (int) : value
        edges (list) : a list of Vertices
        num_edges (int) : the number of edges
        status (str) : None or 'discovered' or 'done'
        start_time (int) : the process start time
        end_time (int) : the process end time
        predecessor (Vertex) : the predecessor
        color (str) : 'RED' or 'GREEN'
    """
    def __init__(self, key):
        """reads in the specification of a graph and creates a graph using an adjacency list representation. You may assume the graph is not empty and is a correct specification. E.g. each edge is represented by a pair of vertices between 1 and n. Note that the graph is not directed so each edge specified in the input file should appear on the adjacency list of each vertex of the two vertices associated with the edge.
        """
        self.key = key
        self.edges = [] # holds list of 2nd connected vertex
        self.num_edges = 0
        self.discovered = False
        self.color = None

    def __repr__(self):
        return 'Vertex(key=%s, num_edges=%s, edges=%s)'\
        % (self.key, self.num_edges, self.edges)
        
    def add_edge(self, dest):
        self.edges.append(v)
        self.num_edges += 1
