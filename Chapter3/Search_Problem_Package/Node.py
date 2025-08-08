class Node():
  def __init__(self, state, parent = None, path_cost = 0):
    self.state = state
    self.parent = parent
    self.path_cost = path_cost

  def __str__(self):
    return f"|Node|  State: {self.state} | Parent: {self.parent} | Path Cost: {self.path_cost}"