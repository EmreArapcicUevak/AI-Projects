from romania_search_problem import Romania_Search_Problem_Uniform_Cost
from Search_Problem_Package.search_problem import Search_Problem
from Search_Problem_Package.que import FIFO_Que
from Search_Problem_Package.node import Node
from Search_Problem_Package.expand import expand

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

  return None


if __name__ == "__main__":
  arad_to_giurgiu = Romania_Search_Problem_Uniform_Cost(initial_state="Arad", goal_state="Giurgiu")
  result = breadth_first_search(problem=arad_to_giurgiu)

  if result == None:
      print("No solution found")
  else:
    while result != None:
      print(result)
      result = result.parent

    

