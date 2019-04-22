from graph import Graph

#Instanciate a new graph:
g = Graph(vertices=[1,2,3,4,5,6])
g.add_edge((1,2))
g.add_edge((2,3))
g.add_edge((3,4))
g.add_edge((4,4))
g.add_edge((4,0))


# Checking its adjacencies (edges)
for vertice,adjacencies in g.simple_represented().items():
  if adjacencies:
    print('Vertice {} has the following adjacencies: {}'.format(vertice,adjacencies))
  

vertice, degree = g.max_degree_vertice()
print('\nThe vertice with highest degree is {}, with degree {} '.format(vertice,degree))

print('\nNumber of loops in graph is:',g.n_loops())


edge = (4,4)
if g.has_edge((edge)): 
  print('\nTrue! this graph does have a '+str(edge)+' edge')
else:
  print('False!')


#Example of Eulerian grpah:
eulerian_graph = Graph([1,2,3,4])
eulerian_graph.add_edge((1,2))
eulerian_graph.add_edge((2,3))
eulerian_graph.add_edge((3,4))
eulerian_graph.add_edge((4,1))
if eulerian_graph.is_eulerian():
	print('\nThis is an eulerian graph!')





g = Graph()
g.add_edge((1,2))
g.add_edge((1,3))
g.add_edge((2,4))
g.add_edge((2,5))
g.add_edge((3,6))
g.add_edge((5,6))

# Present the simple represetation of a graph:
print('\nSimple presentation of this graph: ',g.simple_represented())

# Perform a dfs on the graph:
start = 1
visited_vertices = g.dfs_search(start)
print('Visited vertices were:'+str(visited_vertices))


#Perform Cormen DFS on the graph:
color, discovery_time, finish_time = g.cormen_dfs()
print('Final color of vertices: ',color)
print('Vertices discovery time:',discovery_time)
print('Vertice finish time: ',finish_time)
'''

Next tasks:

-add __str__ methods
-add tests
- verify if grpah has an open eulerian path
'''