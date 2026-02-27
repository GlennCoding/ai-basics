# Random search

We have open_list, which saves states that we've searched and checked, if they are the goal state.

Each step, we pick a random state and do state transitions of every state, one by one in isolation, appending all of the new states to open_list, checking if one of them is the goal.

Then we repeat, taking a random state, etc. until we find the goal state.

# BFS

- frontier -> stores nodes to be checked from the beginning
- Then for each step, it pops the first node
  - Goes through all actions and checks wether one of the states is the goal state
  - Add each of these states to the frontier
  - It saves checked node to visited set
  - Repeat loop

# Shortest Toast Time Search (via Dijkstra's Algorithm)

Description of how algo works:
- It's like BFS, but not picking the locally nearest neighbour, but instead picking the node that has the shortest total distance from the start node -> till we find our goal node
- We check already explored neighboring nodes for shorter paths, long paths get de-prioritised
- We don't go over nodes again, if the current path is longer than the already known shortest path to that node
- For this process we use min-heaps, which help us sort from min to max distance

- We start from start state and initialise our min heap
- We pop the nearest distanced node from heap
- We check if that node has goal state -> if yes, we found the shortest path
  - If it's popped from minheap, it means there can't be any other path that is shorter.
- If not, we get the neighboring states via state_transition of each action
  - We check if any of the neighboring states have a smaller distance than the already documented ones for themselves
    - If yes, add them to heap and save their distance and prev node
  -> Like this we always add new neighboring states to the minheap or we updated their distance and prev node, if we've found a shorter distance in the graph

Naming:

- u -> current node (state)
- v -> neighboring node
- w -> weight of edges (wait time)
- d -> distance / total weight from start to current node (total wait time)

------
## Implementation

Input:

- start_state

Initialise:

- dist { state: distance }
- prev (state & action) ->
  - Example: For node {toaster_has_power: true, ...} prev node is ({toaster_has_power: false, ...}, action)
- minHeap (distance, state) -> saves the nodes we have to check next 

Implementation plan:

- initialise distances -> dist = {start: 0}
- initialise prev -> prev= {start: None}
- initialise minHeap -> minHeap = [(0, start)]

- start at start_state 
  - add start_state to heap
  
- pop heap head -> distance (d) & current node (u)
  - if current d is outdated, continue (dist[u] contains the nearest distance)
  - if u == goal -> stop
  - loop through adjacent states / neighbouring nodes (v)
    - get new distance (nd = d + w)
    - if nd smaller than dist.get(v, float(inf))
      - for dist v add nd
      - for prev v add u
      - push (nd, v) to minHeap

- repeat loop till minHeap is empty (while heap)

Reconstruct paths (recursive):

-> input: prev, end_state_key, start_key

def getPath(prev, u_key, path, start_key):
    if (u_key == start_key)
      return path
    
    prev_state_key, prev_action = prev[u_key]

    updated_path = [prev_action] + path

    getPath(prev, prev_state_key, path, start_key)
    
Reconstruct paths (iterative):

-> input: prev, end_state_key, start_key

path = []
next_u_key = end_state_key

while True:
  if (next_u_key == start_key):
    return path
  
  prev_state_key, prev_action = prev[next_u_key]
  
  path = [prev_action] + path
  next_u_key = prev_state_key
