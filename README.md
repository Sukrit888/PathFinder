# 🧭 PathFinder – Smart Navigation System using Graph Algorithms

PathFinder is a Python-based navigation system that finds the shortest path between nodes using **Dijkstra's Algorithm** and **A* Search Algorithm**. It is built with a strong foundation in Data Structures and Algorithms (DSA), ideal for practicing graph theory concepts.

---

## 🚀 Features

- Add nodes and weighted edges to build custom graphs.
- Add (x, y) coordinates for each node to enable A* heuristics.
- Use **Dijkstra's Algorithm** for shortest path with edge weights.
- Use **A\*** for optimal navigation with heuristics (Euclidean distance).
- Clean and modular Python code.
- Unit tests using Python’s `unittest` module.

---

## 📁 File Structure

PathFinder/
├── my_pathfinder.py # Main Graph class with Dijkstra & A* implementation
├── test_pathfinder.py # Unit tests for the graph algorithms
└── README.md # Project documentation


---

## 🧠 Algorithms Used

### Dijkstra’s Algorithm
Finds the shortest path based only on edge weights.

### A* Search
Finds the shortest path using:
- `g(n)` = cost so far from start to node `n`
- `h(n)` = heuristic estimate to goal (Euclidean)

---

## 🧪 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/pathfinder.git
cd pathfinder
```

### 2. Run Unit Tests
``` bash
python test_pathfinder.py
```
### 3. 🧰 Dependencies
No external packages required! Only Python standard libraries:

heapq

math

unittest

### 4. Topics Covered

Graphs (adjacency list)

Priority queues

Greedy algorithms

Shortest path finding

Heuristics (A* search)

Python unittest framework
