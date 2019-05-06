from vertice import Vertice
from operator import itemgetter
from random import choice
class Graph:
  ''' Represents a graph through python's dictionaries'''
  def __init__(self,vertices=[]):
      ''' Creates a graph
        Arguments:
        vertices: A list of vertices to be added to the graph. Can be empty
      '''

      #Instance variable to represent a graph:
      self.vertices_dict = {}
      # If there are vertices to be added, add them:
      if vertices:
        for key in vertices:
          self.vertices_dict[key] = Vertice(key)


      self.n_vertices = len(vertices)
      self.n_edges = 0

  def add_vertice(self,vertice):
    ''' Adds a new vertice
        Arguements:
        key: name of vertice to be added
        TODO:
        -chck to see if there's already a vertice named key before adding it, and throw exeption if it happens
    '''
    #if vertice is not int
    if not isinstance(vertice,int):
      raise ValueError("Vertice must be an int")
      return
    #if vertice already exists:
    if vertice in self.vertices_dict.keys():
      raise ValueError('Vertice {} already exists in graph'.format(vertice))
      return

    self.vertices_dict[vertice] = Vertice(vertice)
    self.n_vertices = self.n_vertices + 1


  def add_edge(self,edge,cost=0):
    ''' Adds a edge to the graph
        Arguments:
        edge: a tuple containing the origin and destiation vertices of the edge
        TODO:
    '''
    if len(edge) != 2:
      raise ValueError('Edge must have exactly 2 vertices')
      return

    #unpack tuple:
    origin, destination = edge

    #If one of the vertices in edge is not in graph:
    if origin not in self.vertices_dict:
        self.add_vertice(origin)
    if destination not in self.vertices_dict:
        self.add_vertice(destination)


    if origin != destination:
      self.get_vertice(origin).new_adjacency(self.get_vertice(destination))

      self.get_vertice(destination).new_adjacency(self.get_vertice(origin))

    else:
      self.get_vertice(origin).new_adjacency(self.get_vertice(destination))

    self.n_edges += 1


  def get_vertice(self,n):
    ''' Retrieve a single vertice named 'n'
        Arguements:
        n: name of the vertice to be returned
        TODO:
        -validate that vertice is in graph
          and throw exeption if not
    '''
    if n in self.vertices_dict:
        return self.vertices_dict[n]
    else:
        raise ValueError('Graph has no vertice named {}'.format(n))


  def has_edge(self,edge):
    '''check if edge (origin,destination) exist '''
    origin, destination = edge
    if origin in self.get_vertices_list():
      vertice = self.get_vertice(origin)
      if destination in vertice.get_adjacencies_list():
        return True
    return False


  def get_vertices_list(self):
    ''' Return a list of all the graph's vertices  '''
    return list(self.vertices_dict.keys())

  def get_vertices_dict(self):
    ''' Return whole vertices dictionary '''
    return self.vertices_dict

  def n_edges(self):
    ''' Return all edges contained in the graph'''
    return self.n_edges


  def get_adjacent_vertices(self,v):
    ''' Returns a list of all vertices adjacent to vertice 'v' '''
    pass


  def __str__(self):
    pass


  def has(self,n):
    ''' Check if the graph contains a vertice named n
        Arguments:
        n: vertice to be found in graph
    '''
    return n in self.vertices_dict


  def get_degrees_list(self):
    ''' return a degrees list'''
    return [vertice.get_degree() for key,vertice in self.vertices_dict.items()]


  def get_degrees_dict(self):
    ''' Return a degree list containing tuples represeting (vertice_name, vertice_degree)'''
    return dict([(vertice.get_name() , vertice.get_degree()) for key, vertice in self.vertices_dict.items()])


  def max_degree_vertice(self):
    ''' Return tuple containing (vertice_name,degree_of_vertice)
        TODO: must check if therse 2 vertices with same max degree
    '''
    degrees_dict = self.get_degrees_dict()
    filter_ = lambda k: k[1]
    highest_degree = max(degrees_dict.items(), key=filter_)
    return highest_degree


  def n_loops(self):
    ''' return number of loops present in the graph'''
    n_loops = 0
    for v in self.get_vertices_list():
      #if there's a loop edge in this vertice:
      if self.has_edge((v,v)):
        n_loops += 1
    return n_loops


  def is_eulerian(self):
    ''' Verify if graph is eulerian (all vertices must have even degrees)'''
    return all([True if degree %2 == 0 else False for degree in self.get_degrees_list()])


  def has_open_eulerian_path(self):
    ''' Check if graph contains an open eulerian path'''
    pass


  def simple_represented(self):
    ''' Return a simple represetation of the graph'''
    simple_represented = {}
    for vertice in self.get_vertices_list():
      simple_represented[vertice] = set(self.get_vertice(vertice).get_adjacencies_list())
    return simple_represented


  def dfs_search(self,start):
    ''' Perform a deep first search on the graph '''
    graph = self.simple_represented()
    time = {}
    stack   = [start]      # Vertices to be visited
    visited = set()        # Vertices already visited

    while stack:
        vertice = stack.pop()
        time[vertice] = 0

        if vertice not in visited:
            visited.add(vertice)
            #print("Visited: "+str(visited))
            stack.extend(graph[vertice] - visited)
            #print('Stack: '+str(stack)+'\n')

    return visited

  def cormen_dfs(self):
    '''Perform a deeep first search on the graph
    based on Cormen algorithm for this task '''

    graph = self.simple_represented()
    color = {vertice: 'white' for vertice in self.get_vertices_list()}
    discovery_time = {vertice: None for vertice in self.get_vertices_list()}
    finish_time = {vertice: None for vertice in self.get_vertices_list()}
    previous_vertice = {vertice: None for vertice in self.get_vertices_list()}
    current_time = 0

    for vertice in graph.keys():
      if color[vertice] == 'white':
        self.visit(vertice,graph,color,discovery_time,finish_time,previous_vertice,current_time)

    return color,discovery_time,finish_time

  def visit(self,vertice,graph,color,discovery_time,finish_time,previous_vertice,current_time):
    ''' Cormen's DFS helper function for visiting a vertice'''
    color[vertice] = 'grey'
    current_time += 1
    discovery_time[vertice] = current_time
    for adjacency in graph[vertice]:
      if color[adjacency] == 'white':
        previous_vertice[adjacency] = vertice
        self.visit(adjacency,graph,color,discovery_time,finish_time,previous_vertice,current_time)
    color[vertice] = 'black'
    current_time += 1
    finish_time[vertice] = current_time


  def cormen_bfs(self,start=None):
    ''' Implements Cormen's BFS algorithm
        start (int): optional arguement
    '''
    #Data structures needed:
    graph = self.simple_represented()
    color = {vertice: 'white' for vertice in self.get_vertices_list()}
    distance_from_start = {vertice: 0 for vertice in self.get_vertices_list()} # must be changed to distance
    previous_vertice = {vertice: None for vertice in self.get_vertices_list()}
    queue = [] # only operations allowed are append (add to queue) and pop (remove form queue)


    #BFS starts from the first vertice present in the graph definiton:
    if not start:
        start = next(iter(graph))
    queue.append(start)

    while queue:
      vertice = queue.pop()
      for adjacency in graph[vertice]:
        if color[adjacency] == 'white':
          color[adjacency] == 'grey'
          distance_from_start[adjacency] = distance_from_start[vertice] + 1
          previous_vertice[adjacency] = vertice
          queue.append(adjacency)
      color[vertice] = 'black'
    return start, color, distance_from_start

  def connected_components(self):
    '''Finds all connected components of a graph, based on the DFS search algorithm'''
    graph = self.simple_represented()
    id = 0
    ids = {vertice: None for vertice in self.get_vertices_list()}
    for vertice in graph.keys():
      #faz uma busca começando pelo vértice:
      _, colors, _ = self.cormen_bfs(vertice)
      #verifica quais foram marcados como preto, adiciona eles como um id novo:
      for v in graph.keys():
        if colors[v] == 'black' and not ids[v]:
          ids[v] = id
          flag = True
      if flag:
          id += 1
          flag = False
    return ids
