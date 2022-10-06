from utils import *
from search import *
from search_modified import *
import math

"""
-------------------------------------------------------------------------------------
---------------------------- MISSIONARY CANNIBAL PROBLEM ----------------------------
-------------------------------------------------------------------------------------

Missionaries and Cannibals are to be brought from left to the right side of the river.
Maintaining the constraint of number of cannibals not exceeding number of missionaries.

"""

"""
1. RBF 3M 3C boat = 2
"""
class MissionaryCannibalProblem(Problem):
    def __init__(self, initial, goal):
        Problem.__init__(self, initial, goal)
        self.state = initial

    def actions(self, state):
        """
        State : (M,C,B)
        1. Boat on the left side [Indicated by B=0]
            1. Number of missionaries on the left side (0,1,2,3) [Indicated by '3-M']
                1. Number of cannibals on the left side (0,1,2,3) [Indicated by '3-C']
        2. Boat on the right side [Indicated by B=1]
            1. Number of missionaries on the right side (0,1,2,3) [Indicated by 'M']
                1. Number of cannibals on the right side (0,1,2,3) [Indicated by 'C']

        Based on M, C, B each state has a set of legal and illegal actions available.
        We return the legal actions available for each state
        """
        if state[2] == 0:  # Boat on the left
            if state[0] == 0:  # 3 missionaries on the left
                if state[1] == 0:
                    return ['MC', 'C', 'CC']
                elif state[1] == 1:
                    return ['M', 'C', 'CC']
                elif state[1] == 2:
                    return ['MM', 'C']
                else:
                    return []
            elif state[0] == 1:  # 2 missionaries on the left
                if state[1] == 1:
                    return ['MC', 'MM']
                else:
                    return []
            elif state[0] == 2:  # 1 missionary on the left
                if state[1] == 2:
                    return ['MC', 'M']
                else:
                    return []
            else:  # 0 missionary on the left
                if state[1] <= 1:
                    return ['C', 'CC']
                elif state[1] == 2:
                    return ['C']
                else:
                    return []
        elif state[2] == 1:  # Boat on the right side
            if state[0] == 0:  # 3 missionaries on the left
                if state[1] == 0:
                    return []
                elif state[2] == 1:
                    return ['C']
                else:
                    return ['C', 'CC']
            elif state[0] == 1:  # 2 missionaries on the left
                if state[1] == 1:
                    return ['M', 'MC']
                else:
                    return []
            elif state[0] == 2:  # 1 missionary on the left
                if state[1] == 2:
                    return ['MM', 'MC']
                else:
                    return []
            else:  # No missionary on the left
                if state[1] == 1:
                    return ['MM', 'C']
                elif state[1] == 2:
                    return ['M', 'C', 'CC']
                else:
                    return []
        else:
            return []

    def result(self, state, action):
        state = list(state)
        if state[2] == 0:  # Boat on the left, (For actions we add them)
            if action == 'M':
                state[0] = state[0] + 1
                state[2] = 1
            elif action == 'MM':
                state[0] = state[0] + 2
                state[2] = 1
            elif action == 'MC':
                state[0] = state[0] + 1
                state[1] = state[1] + 1
                state[2] = 1
            elif action == 'C':
                state[1] = state[1] + 1
                state[2] = 1
            else:
                state[1] = state[1] + 2
                state[2] = 1
        elif state[2] == 1:  # Boat on the right, (For actions we subtract them)
            if action == 'M':
                state[0] = state[0] - 1
                state[2] = 0
            elif action == 'MM':
                state[0] = state[0] - 2
                state[2] = 0
            elif action == 'MC':
                state[0] = state[0] - 1
                state[1] = state[1] - 1
                state[2] = 0
            elif action == 'C':
                state[1] = state[1] - 1
                state[2] = 0
            else:
                state[1] = state[1] - 2
                state[2] = 0

        state = tuple(state)
        self.state = state
        return self.state

    def goal_test(self, state):
        if state == self.goal:
            return True
        else:
            return False

    def h(self, node):
        current_state = node.state
        return ((3-current_state[0]) + (3-current_state[1])/2)

initial = tuple([0, 0, 0])
goal = tuple([3, 3, 1])
missionary_cannibal_problem = MissionaryCannibalProblem(initial, goal)
# rbfs_tree_search_solution, nodes_expanded = recursive_best_first_search(missionary_cannibal_problem)
# for node in rbfs_tree_search_solution.path():
#     print(node.action, node.state)
# print("Optimal Path Length: ", len(rbfs_tree_search_solution.path()))
# print("Nodes Expanded: ", nodes_expanded)

# bfs_tree_solution, nodes_expanded = breadth_first_graph_search(missionary_cannibal_problem)
# for node in bfs_tree_solution.path():
#     print(node.action, node.state)
# print("Optimal Path Length: ", len(bfs_tree_solution.path()))
# print("Nodes Expanded: ", nodes_expanded)

"""
2. Uniform Cost Search 4M 4C boat = 3
"""
class MissionaryCannibalProblem_2(Problem):
    def __init__(self, initial, goal):
        Problem.__init__(self, initial, goal)
        self.state = initial

    def actions(self, state):
        if state[2] == 0:  # Boat on the left
            if state[0] == 0:  # 4 missionaries on the left
                if state[1] == 0:
                    return ['CCC', 'CC', 'MC', 'C']
                elif state[1] == 1:
                    return ['CCC', 'MMC', 'CC', 'M', 'C']
                elif state[1] == 2:
                    return ['MM', 'CC', 'MC']  
                elif state[1] == 3:
                    return ['MMM', 'C']  
                else:
                    return []
            elif state[0] == 1:  # 3 missionaries on the left
                if state[1] == 1:
                    return ['MMM', 'MC']
                else:
                    return []
            elif state[0] == 2:  # 2 missionary on the left
                if state[1] == 2:
                    return ['MMC', 'MM', 'MC']
                else:
                    return []
            elif state[0] == 3:  # 1 missionary on the left
                if state[1] == 3:
                    return ['MC', 'M']
                else:
                    return []
            else:  # 0 missionary on the left
                if state[1] <= 1:
                    return ['CCC', 'CC', 'C']
                elif state[1] == 2:
                    return ['CC', 'C']
                elif state[1] == 3:
                    return ['C']
                else:
                    return []
        elif state[2] == 1:  # Boat on the right side
            if state[0] == 0:  # 4 missionaries on the left
                if state[1] == 0:
                    return []
                elif state[1] == 1:
                    return ['C']
                elif state[1] == 2:
                    return ['CC','C']
                else:
                    return ['CCC','C', 'CC']
            elif state[0] == 1:  # 3 missionaries on the left
                if state[1] == 1:
                    return ['M']
                else:
                    return []
            elif state[0] == 2:  # 2 missionaries on the left
                if state[1] == 2:
                    return ['MM', 'MC']
                else:
                    return []
            elif state[0] == 3:  # 1 missionary on the left
                if state[1] == 3:
                    return ['MMM', 'MM', 'MC']
                else:
                    return []
            else:  # No missionary on the left
                if state[1] == 1:
                    return ['MMM', 'C']
                elif state[1] == 2:
                    return ['MM', 'CC', 'C']
                elif state[1] == 3:
                    return ['CCC','CC', 'M', 'C']
                else:
                    return []
        else:
            return []

    def result(self, state, action):
        state = list(state)
        if state[2] == 0:  # Boat on the left, (For actions we add them)
            if action == 'MMM':
                state[0] = state[0] + 3
                state[2] = 1
            elif action == 'CCC':
                state[1] = state[1] + 3
                state[2] = 1
            elif action == 'MMC':
                state[0] = state[0] + 2
                state[1] = state[1] + 1
                state[2] = 1
            elif action == 'MM':
                state[0] = state[0] + 2
                state[2] = 1
            elif action == 'CC':
                state[1] = state[1] + 2
                state[2] = 1
            elif action == 'MC':
                state[0] = state[0] + 1
                state[1] = state[1] + 1
                state[2] = 1
            elif action == 'M':
                state[0] = state[0] + 1
                state[2] = 1
            else:
                state[1] = state[1] + 1
                state[2] = 1
        elif state[2] == 1:  # Boat on the right, (For actions we subtract them)
            if action == 'MMM':
                state[0] = state[0] - 3
                state[2] = 0
            elif action == 'CCC':
                state[1] = state[1] - 3
                state[2] = 0
            elif action == 'MMC':
                state[0] = state[0] - 2
                state[1] = state[1] - 1
                state[2] = 0
            elif action == 'MM':
                state[0] = state[0] - 2
                state[2] = 0
            elif action == 'CC':
                state[1] = state[1] - 2
                state[2] = 0
            elif action == 'MC':
                state[0] = state[0] - 1
                state[1] = state[1] - 1
                state[2] = 0
            elif action == 'M':
                state[0] = state[0] - 1
                state[2] = 0
            else:
                state[1] = state[1] - 1
                state[2] = 0

        state = tuple(state)
        self.state = state
        return self.state

    def goal_test(self, state):
        if state == self.goal:
            return True
        else:
            return False

    def h(self, node):
        """
        Here we define the following heuristic function:
        h(M,C,B) = ceil([M + C]/B)
        [This is a consistent heuristic (Optimal for graph search strategies)]
        """
        current_state = node.state
        return ((4-current_state[0]) + (4-current_state[1])/3)

# initial = tuple([0, 0, 0])
# goal = tuple([4, 4, 1])

# missionary_cannibal_problem_3 = MissionaryCannibalProblem_3(initial, goal)
# uniform_cost_search_solution = uniform_cost_search(missionary_cannibal_problem_3)
# for node in uniform_cost_search_solution.path():
#     print(node.action, node.state)
# print(len(uniform_cost_search_solution.path()))


"""
3. Greedy Best First Search 5M 5C boat = 3
"""   
class MissionaryCannibalProblem_3(Problem):
    def __init__(self, initial, goal):
        Problem.__init__(self, initial, goal)
        self.state = initial

    def actions(self, state):
        if state[2] == 0:           # Boat on the left
            if state[0] == 0:       # 5 missionaries on the left
                if state[1] == 0:
                    return ['CCC', 'CC', 'MC', 'C']
                elif state[1] == 1:
                    return ['MMM','CCC', 'MMC', 'CC','M','C']
                elif state[1] == 2:
                    return ['MMM','CCC','MM','CC','C']  
                elif state[1] == 3:
                    return ['MMM','CC','C']  
                elif state[1] == 4:
                    return ['C'] 
                else:
                    return []
            elif state[0] == 1:     # 4 missionaries on the left
                if state[1] == 1:
                    return ['MC']
                else:
                    return []
            elif state[0] == 2:     # 3 missionaries on the left
                if state[1] == 2:
                    return ['MMM','MC']
                else:
                    return []
            elif state[0] == 3:     # 2 missionary on the left
                if state[1] == 3:
                    return ['MM','MC']
                else:
                    return []
            elif state[0] == 4  :   # 1 missionary on the left
                if state[1] == 4:
                    return ['M']
                else:
                    return []
            else:                   # 0 missionary on the left
                if state[1] <= 2:
                    return ['CCC', 'CC', 'C']
                elif state[1] == 3:
                    return ['CC', 'C']
                elif state[1] == 4:
                    return ['C']
                else:
                    return []
        elif state[2] == 1:         # Boat on the right side
            if state[0] == 0:       # 5 missionaries on the left
                if state[1] == 0:
                    return []
                elif state[1] == 1:
                    return ['C']
                elif state[1] == 2:
                    return ['CC','C']
                else:
                    return ['CCC','C', 'CC']
            elif state[0] == 1:     # 4 missionaries on the left
                if state[1] == 1:
                    return ['M']
                else:
                    return []
            elif state[0] == 2:     # 3 missionaries on the left
                if state[1] == 2:
                    return ['MM', 'MC']
                else:
                    return []
            elif state[0] == 3:     # 2 missionary on the left
                if state[1] == 3:
                    return ['MMM', 'MC']
                else:
                    return []
            elif state[0] == 4:     # 1 missionary on the left
                if state[1] == 4:
                    return ['MC']
                else:
                    return []
            else:                   # No missionary on the left
                if state[1] == 1:
                    return ['C']
                elif state[1] == 2:
                    return ['CC', 'C']
                elif state[1] == 3:
                    return ['CCC','CC','MM', 'C']
                elif state[1] == 4:
                    return ['CCC','MMC','CC', 'M','C']
                else:
                    return []
        else:
            return []

    def result(self, state, action):
        state = list(state)
        if state[2] == 0:  # Boat on the left, (For actions we add them)
            if action == 'MMM':
                state[0] = state[0] + 3
                state[2] = 1
            elif action == 'CCC':
                state[1] = state[1] + 3
                state[2] = 1
            elif action == 'MMC':
                state[0] = state[0] + 2
                state[1] = state[1] + 1
                state[2] = 1
            elif action == 'MM':
                state[0] = state[0] + 2
                state[2] = 1
            elif action == 'CC':
                state[1] = state[1] + 2
                state[2] = 1
            elif action == 'MC':
                state[0] = state[0] + 1
                state[1] = state[1] + 1
                state[2] = 1
            elif action == 'M':
                state[0] = state[0] + 1
                state[2] = 1
            else:
                state[1] = state[1] + 1
                state[2] = 1
        elif state[2] == 1:  # Boat on the right, (For actions we subtract them)
            if action == 'MMM':
                state[0] = state[0] - 3
                state[2] = 0
            elif action == 'CCC':
                state[1] = state[1] - 3
                state[2] = 0
            elif action == 'MMC':
                state[0] = state[0] - 2
                state[1] = state[1] - 1
                state[2] = 0
            elif action == 'MM':
                state[0] = state[0] - 2
                state[2] = 0
            elif action == 'CC':
                state[1] = state[1] - 2
                state[2] = 0
            elif action == 'MC':
                state[0] = state[0] - 1
                state[1] = state[1] - 1
                state[2] = 0
            elif action == 'M':
                state[0] = state[0] - 1
                state[2] = 0
            else:
                state[1] = state[1] - 1
                state[2] = 0

        state = tuple(state)
        self.state = state
        return self.state

    def goal_test(self, state):
        if state == self.goal:
            return True
        else:
            return False

    def h(self, node):
        current_state = node.state
        return ((5-current_state[0]) + (5-current_state[1])/3)

initial = tuple([0, 0, 0])
goal = tuple([5, 5, 1])

# missionary_cannibal_problem_3 = MissionaryCannibalProblem_3(initial, goal)
# gbfs_solution = best_first_search_modified('GBFS',missionary_cannibal_problem_3, missionary_cannibal_problem_3.h)
# for node in gbfs_solution.path():
#     print(node.action, node.state)
# print("Optimal Path Length: ", len(gbfs_solution.path()))
# #print("Nodes Expanded: ", nodes_expanded)

"""
4. A* 6M 6C boat = 4
"""   
class MissionaryCannibalProblem_4(Problem):
    def __init__(self, initial, goal):
        Problem.__init__(self, initial, goal)
        self.state = initial

    def actions(self, state):
        if state[2] == 0:           # Boat on the left
            if state[0] == 0:       # 6 missionaries on the left
                if state[1] == 0:
                    return ['CCCC','MMCC','CCC','CC','MC','C']
                elif state[1] == 1:
                    return ['CCCC','CCC','MMC','CC','M','C']
                elif state[1] == 2:
                    return ['CCCC','MMMC','CCC','MM','CC','C']  
                elif state[1] == 3:
                    return ['MMM','CCC','CC','C']   
                elif state[1] == 4:
                    return ['MMMM','CC','C']   
                elif state[1] == 5:
                    return ['C']                
                else:
                    return []
            elif state[0] == 1:     # 5 missionaries on the left
                if state[1] == 1:
                    return ['MMCC','MC']
                else:
                    return []
            elif state[0] == 2:     # 4 missionaries on the left
                if state[1] == 2:
                    return ['MMMM','MMCC','MC']
                else:
                    return []
            elif state[0] == 3:     # 3 missionary on the left
                if state[1] == 3:
                    return ['MMMC','MMCC','MMM','MC']
                else:
                    return []
            elif state[0] == 4  :   # 2 missionary on the left
                if state[1] == 4:
                    return ['MMCC','MMC','MM','MC']
                else:
                    return []
            elif state[0] == 5  :   # 1 missionary on the left
                if state[1] == 5:
                    return ['MC','M']
                else:
                    return []
            else:                   # 0 missionary on the left
                if state[1] <= 2:
                    return ['CCCC','CCC','CC','C']
                elif state[1] == 3:
                    return ['CCC','CC','C']
                elif state[1] == 4:
                    return ['CC','C']
                elif state[1] == 5:
                    return ['C']
                else:
                    return []
        elif state[2] == 1:         # Boat on the right side
            if state[0] == 0:       # 6 missionaries on the left
                if state[1] == 0:
                    return []
                elif state[1] == 1:
                    return ['C']
                elif state[1] == 2:
                    return ['CC','C']
                elif state[1] == 3:
                    return ['CCC','CC','C']
                else:
                    return ['CCCC','CCC','CC','C']
            elif state[0] == 1:     # 5 missionaries on the left
                if state[1] == 1:
                    return ['MC','M']
                else:
                    return []
            elif state[0] == 2:     # 4 missionaries on the left
                if state[1] == 2:
                    return ['MMCC','MM','CC','MC']
                else:
                    return []
            elif state[0] == 3:     # 3 missionary on the left
                if state[1] == 3:
                    return ['MMMC','MMCC','MMM','MC']
                else:
                    return []
            elif state[0] == 4:     # 2 missionary on the left
                if state[1] == 4:
                    return ['MMMM','MMCC',  'MC']
                else:
                    return []
            elif state[0] == 5:     # 1 missionary on the left
                if state[1] == 5:
                    return ['MMCC','MC']
                else:
                    return []
            else:                   # No missionary on the left
                if state[1] == 1:
                    return ['C']
                elif state[1] == 2:
                    return ['CCCC','CC','C']
                elif state[1] == 3:
                    return ['MMM','CCC','CC','C']
                elif state[1] == 4:
                    return ['CCCC','MMMC','CCC','MM','CC','C']
                elif state[1] == 5:
                    return ['CCCC','CCC','MMC','CC','M','C']
                else:
                    return []
        else:
            return []

    def result(self, state, action):
        state = list(state)
        if state[2] == 0:  # Boat on the left, (For actions we add them)
            if action == 'MMMM':
                state[0] = state[0] + 4
                state[2] = 1
            elif action == 'CCCC':
                state[1] = state[1] + 4
                state[2] = 1       
            elif action == 'MMMC':
                state[0] = state[0] + 3
                state[1] = state[1] + 1
                state[2] = 1  
            elif action == 'MMCC':
                state[0] = state[0] + 2
                state[1] = state[1] + 2
                state[2] = 1  
            elif action == 'MMM':
                state[0] = state[0] + 3
                state[2] = 1
            elif action == 'CCC':
                state[1] = state[1] + 3
                state[2] = 1
            elif action == 'MMC':
                state[0] = state[0] + 2
                state[1] = state[1] + 1
                state[2] = 1
            elif action == 'MM':
                state[0] = state[0] + 2
                state[2] = 1
            elif action == 'CC':
                state[1] = state[1] + 2
                state[2] = 1
            elif action == 'MC':
                state[0] = state[0] + 1
                state[1] = state[1] + 1
                state[2] = 1
            elif action == 'M':
                state[0] = state[0] + 1
                state[2] = 1
            else:
                state[1] = state[1] + 1
                state[2] = 1
        elif state[2] == 1:  # Boat on the right, (For actions we subtract them)
             if action == 'MMMM':
                state[0] = state[0] - 4
                state[2] = 1
             elif action == 'CCCC':
                state[1] = state[1] - 4
                state[2] = 1       
             elif action == 'MMMC':
                state[0] = state[0] - 3
                state[1] = state[1] - 1
                state[2] = 1  
             elif action == 'MMCC':
                state[0] = state[0] - 2
                state[1] = state[1] - 2
                state[2] = 1            
             elif action == 'MMM':
                 state[0] = state[0] - 3
                 state[2] = 0
             elif action == 'CCC':
                 state[1] = state[1] - 3
                 state[2] = 0
             elif action == 'MMC':
                 state[0] = state[0] - 2
                 state[1] = state[1] - 1
                 state[2] = 0
             elif action == 'MM':
                 state[0] = state[0] - 2
                 state[2] = 0
             elif action == 'CC':
                 state[1] = state[1] - 2
                 state[2] = 0
             elif action == 'MC':
                 state[0] = state[0] - 1
                 state[1] = state[1] - 1
                 state[2] = 0
             elif action == 'M':
                 state[0] = state[0] - 1
                 state[2] = 0
             else:
                 state[1] = state[1] - 1
                 state[2] = 0

        state = tuple(state)
        self.state = state
        return self.state

    def goal_test(self, state):
        if state == self.goal:
            return True
        else:
            return False

    def h(self, node):
        current_state = node.state
        return ((6-current_state[0]) + (6-current_state[1])/4)

initial = tuple([0, 0, 0])
goal = tuple([6, 6, 1])

missionary_cannibal_problem_4 = MissionaryCannibalProblem_4(initial, goal)
astar_solution, nodes_expanded = astar_search(missionary_cannibal_problem_4, None, False)
for node in astar_solution.path():
    print(node.action, node.state)
print("Optimal Path Length: ", len(astar_solution.path()))
print("Nodes Expanded: ", nodes_expanded)