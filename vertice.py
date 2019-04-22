class Vertice:
  def __init__(self,name):
      self.name = name
      self.adjacencies = {}
      self.n_adjacencies = 0

  def new_adjacency(self,destination, weight=0):
      # Repeated edge with same weight
      if destination in self.adjacencies.keys():
        if weight == self.adjacencies[destination]: 
          raise ValueError("Warning! Repeated edge. Vertice {} already has connection with weigth {} to vertice {}".format(self.name, weight, destination))
          return
      # Repeated loop with same weight:
      if self.name == destination:
        if weight == self.adjacencies[destination]:
          raise ValueError('Warning! Vertice {} already has a loop with weight'.format(destination)) 
          return
      # If it's a loop (the first one)
      if self.name == destination:
        if destination not in self.adjacencies.keys():
          self.adjacencies[destination] = weight
          self.n_adjacencies += 2
          return
      # If it's just an normal edge
      if destination not in self.adjacencies.keys():
        self.adjacencies[destination] = weight
        self.n_adjacencies += 1 
        return

  def get_degree(self):
    ''' Vertices's degree (number of adjacencies)'''
    return self.n_adjacencies

  def get_adjacencies_list(self):
    ''' A list of all this vertice adjacencies '''  
    return list(vertice.get_name() for vertice, weight in self.adjacencies.items())

  def get_name(self):
    ''' Name of vertice '''
    return self.name

  def get_weight(self,destination):
    ''' Weight in a edge between this and 'destination' vertices '''
    return self.adjacencies[destination]

  
  def __str__(self):
    return str(self.name)