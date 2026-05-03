# SE_14 Artificial Intelligence Basics — Assessment Submission

This repository contains my solutions to the practical exercises for the module **SE_14 Artificial Intelligence Basics**. Each subproject covers one area of AI and is accompanied by a short algorithm description.

---

## Repository Structure

```
.
├── README.md                       # This file
├── toast-planning/                 # Problem 1 — Planning
│   └── planning/
│       ├── planner.py              # Contains Planner.shortest_toast_time_search
│       └── planning_problem.py              # Provided utility function
└── toast-optimisation/             # Problem 2 — Optimization
    └── optimization/
        ├── optimization_algorithms.py   # Contains Optimization_Algorithms.gradient_ascent
        └── optimization_problem.py      # Provided utility function
```

Each subproject is self-contained and can be run independently.

---

## Setup

Both projects use only the Python standard library — no additional dependencies are required.

- **Python version:** 3.10 or later recommended

---

## How to Run

### Problem 1 — Shortest Toast Time Search (Planning)

```bash
cd toast-planning
python main.py
```

### Problem 2 — Gradient Ascent for Toast Optimization (Optimization)

```bash
cd toast-optimisation
python main.py
```

---

## Solved Problems

### Shortest Toast Time Search (Homework-Toast)

**Problem Description:** The goal of this planning problem is to find the shortest possible path, measured in time in the toasting world. The number rof states the algorithm visits should also be minimized.

**Area of AI:** Planning

**Applied Algorithms:** I used Dijkstra's Algorithm to solve this problem. The algorithm finds finds the shortest paths from a single source node to all other nodes in a weighted graph with non-negative edge weights. It uses a greedy approach, iteratively selecting the unvisited node with the smallest tentative distance, updating its neighbors' distances, and marking it visited

**Results:** Dijkstra's Algorithm was the best algorithm to find the shortest path to toast a toast, as expected. The algortihm did have a longer execution time than BFS, which makes sense, given that it's considering weights and sometimes goes over the same nodes again, when it found quicker overall paths. 

<div align="center"><img src="assets/toast-planning-results.png" /></div>

**Location [(Link)](toast-planning/planning/planner.py):** Homework-Toast folder: `Planner.shortest_toast_time_search` in `planner/planner.py`, with helper methods `Planner.get_path_iterative` and `Planner.get_path_recursion` for path reconstruction.

---

### Gradient Ascent for Toast Optimization

**Problem Description:** The goal of this optimisation problem was to maximise an utility value based on the parameters *toast_duration*,  *wait_duration* and *power* by implementing gradient ascent. 

**Area of AI:** Optimization

**Applied Algorithms:** I implemented gradient ascent by looking up the slope of each isolated variable (going a small step to the front and the back) and then walking up the slope for each value. I then calculated the utility value for the three updated params. I repeated this procedure for a number of times that I defined in my program. 

**Results:** The algorithm was able to maximise the utility value to a high precision. Small steps were crucial with gradient ascent and higher number of iterations meant a better result, although with diminishing effects at some point.

<div align="center"><img src="assets/toast-optimisation-results.png" /></div>

**Location [(Link)](toast-optimisation/optimization/optimization_algorithms.py):** `Optimization_Algorithms.gradient_ascent` in `optimization/optimization_algorithms.py`, with the helper method `Optimization_Algorithms.numerical_gradient` for central-difference gradient estimation.
