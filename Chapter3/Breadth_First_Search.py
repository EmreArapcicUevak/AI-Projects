from Chapter3.Search_Problem_Package.search_problem import *
from Chapter3.Search_Problem_Package.que import FIFO_Que
from Chapter3.Search_Problem_Package.node import Node
from Chapter3.Search_Problem_Package.expand import expand

def breadth_first_search(problem : Search_Problem):
  node = Node(problem.initial_state)
  if problem.IS_GOAL(node.state):
    return node
  
  frontier = FIFO_Que()
  frontier.push(node)

  reached = [problem.initial_state]
  
  while len(frontier) > 0:
    node = frontier.pop()

    for child in expand(problem=problem, node=node):
      if problem.IS_GOAL(child.state):
        return child
      elif child.state not in reached:
        reached.append(child.state)
        frontier.push(child)

  return SearchStatus.FAILURE