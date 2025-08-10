from Chapter3.Search_Problem_Package.search_problem import Search_Problem
from Chapter3.Search_Problem_Package.expand import expand
from Chapter3.Search_Problem_Package.node import Node
from Chapter3.Search_Problem_Package.que import Priority_Que

def path_cost_evaluation(a : Node, b : Node): # Returns true if a has a bigger prio then b
  return a.path_cost < b.path_cost

def uniform_cost_search(problem : Search_Problem):
  node = Node(problem.initial_state)
  if problem.IS_GOAL(node.state):
    return node
  
  frontier = Priority_Que(path_cost_evaluation)
  frontier.push(node)

  reached = {problem.initial_state: node}
  
  while len(frontier) > 0:
    node = frontier.pop()

    if node.path_cost > reached[node.state].path_cost:
      continue
    elif problem.IS_GOAL(node.state):
      return node

    for child in expand(problem=problem, node=node):
      if child.state not in reached.keys() or child.path_cost < reached[child.state].path_cost:
        reached[child.state] = child
        frontier.push(child)

  return None

if __name__ == "__main__":
  from romania_search_problem import Romania_Search_Problem_Uniform_Cost, Romania_Search_Problem

  arad_to_giurgiu = Romania_Search_Problem(initial_state="Arad", goal_state="Giurgiu")
  sibiu_to_bucharest = Romania_Search_Problem(initial_state="Sibiu", goal_state="Bucharest")

  result = uniform_cost_search(problem=arad_to_giurgiu)

  if result == None:
      print("No solution found")
  else:
    while result != None:
      print(result)
      result = result.parent