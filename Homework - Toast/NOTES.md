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

# Shortest Toast Time Search (via Dijkstra's Algorithm)

Naming:
- u -> current node
- v -> neighboring node
- w -> weight
- d -> distance

Components:

- nodes -> states
  - distance -> compounded time to reach each state
- edges -> actions
- edge weights -> time consumed for action

- adjacency list -> neighboring states
- previous state ->
  - Example: {toaster_has_power: true, ...}, previous state was {toaster_has_power: false, ...}
- shortest path -> saves the shortest path to each state

- minHeap -> saves the nodes we have to check next

Implementation plan:

- initialise distances -> dist = {start: 0}
- initialise prev -> prev= {start: None}
- initialise minHeap -> minHeap = [(0, start)]

- start at start_state 
  - add start_state to heap
  
- pop heap head -> distance (d) & current node (u)
  - if node == goal, then stop
  <!-- - get adjacent states (v, w)
    - how: loop through actions
      - save them to adjacency list -> adj = { state1: [(sate2, time), (state3, time), ...], state2: ... } -->
  - loop through adjacent states / neighbouring nodes (v)
    - get new distance (nd = d + w)
    - if nd smaller than dist.get(v, float(inf))
      - add nd to distances
      - for prev v add u
      - push (nd, v) to minHeap

- repeat loop till minHeap is empty (while heap)