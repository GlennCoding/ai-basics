import random
import math


class Frontier:
    """
    Data structure that stores a frontier of nodes.
    Provides functionality to select and remove nodes according to a search algorithm.
    """
    def __init__(self, goal, search_algorithm):
        self.moves = 0
        self.frontier = []
        self.goal = goal
        self.search_algorithm = search_algorithm

    def add(self, node):
        """
            Add a node to the frontier. 
            New nodes are added to the back.
        """
        self.frontier.append(node)

    def contains_state(self, state):
        """
            Checks whether a node is already in the frontier.
        """
        return any(node.state == state for node in self.frontier)

    def empty(self):
        """
            Checks whether the frontier is empty.
        """
        return len(self.frontier) == 0

    def pop(self):
        """
            Removes a node from the frontier and returns it.
            The returned node is selected by function select_node.
        """
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.select_node()
            self.frontier.remove(node)
            return node


    def select_node(self):
        self.moves += 1
        print(self.moves)
        """
            Selects the next node to extend
        """
        # random search
        if self.search_algorithm == "RS":
            # select a random node from the frontier
            return random.choice(self.frontier)

        # depth-first search
        if self.search_algorithm == "DFS":
            # Selects last node
            return self.frontier[-1]
        
        # breadth-first search
        if self.search_algorithm == "BFS":
            # Selects first node
            return self.frontier[0]
        
        # heuristic search
        if self.search_algorithm == "HS":
            closest_node = self.frontier[0]
            cloest_node_distance = abs(self.goal[0] - closest_node.state[0]) + abs(self.goal[1] - closest_node.state[1])

            for n in self.frontier[1:]:
                distance = abs(self.goal[0] - n.state[0]) + abs(self.goal[1] - n.state[1])
                if (distance < cloest_node_distance):
                    closest_node = n
                    cloest_node_distance = distance

                
            # Selects closest node to end goal
            return closest_node
            
