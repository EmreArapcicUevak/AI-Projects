class Node():
  def __init__(self, state, parent = None, cost = 0):
    self.state = state
    self.parent = parent
    self.cost = cost

  def __str__(self):
    return f"|Node|  State: {self.state} | Parent: {self.parent} | Cost: {self.cost}"