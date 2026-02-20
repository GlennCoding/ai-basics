# Random search

We have open_list, which saves states that we've searched and checked, if they are the goal state.

Each step, we pick a random state and do state transitions of every state, one by one in isolation, appending all of the new states to open_list, checking if one of them is the goal.

Then we repeat, taking a random state, etc. until we find the goal state.

# BFS

- frontier -> stores nodes to be checked from the beginning
- Then for each step, it picks the first node
  - Goes through all actions and checks wether one of the states is the goal state
  - Add each of these states to the frontier
  - After all 4 actions are checked, it removes the first node
  - It saves checked node to visited set

# Heuristic search

- For each action checked, put the closest node to the front (meaning which has used the least amount of time)
- Take the front node and search

How I would do it logically:
- 