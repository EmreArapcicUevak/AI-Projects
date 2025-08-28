
from Chapter3.Search_Problem_Package.search_problem import *
from Chapter3.Search_Problem_Package.que import Stack
from Chapter3.Search_Problem_Package.node import Node
from Chapter3.Search_Problem_Package.expand import expand

def depth_first_search(problem : Search_Problem):
  node = Node(problem.initial_state)
  if problem.IS_GOAL(node.state):
    return node

  frontier = Stack()
  frontier.push(node)

  while len(frontier) > 0:
    node = frontier.pop()

    for child in expand(problem=problem, node=node):
      if problem.IS_GOAL(child.state):
        return child
      else:
        frontier.push(child)

  return SearchStatus.FAILURE