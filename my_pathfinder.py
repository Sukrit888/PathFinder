import heapq

class Graph:
    def __init__(self):
        self.edges = {}
        self.heuristics = {}

    def add_node(self, value):
        if value not in self.edges:
            self.edges[value] = {}

    def add_edge(self, from_node, to_node, weight):
        self.add_node(from_node)
        self.add_node(to_node)
        self.edges[from_node][to_node] = weight
        self.edges[to_node][from_node] = weight  # Undirected

    def set_heuristic(self, node, h_value):
        self.heuristics[node] = h_value

    def get_nodes(self):
        return list(self.edges.keys())

    def bfs(self, start, goal):
        visited = set()
        queue = [(start, [start])]

        while queue:
            current, path = queue.pop(0)
            if current == goal:
                return path, len(path) - 1

            visited.add(current)

            for neighbor in self.edges[current]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
                    visited.add(neighbor)
        return None, float("inf")

    def dfs(self, start, goal):
        visited = set()
        stack = [(start, [start])]

        while stack:
            current, path = stack.pop()
            if current == goal:
                return path, len(path) - 1

            if current not in visited:
                visited.add(current)
                for neighbor in self.edges[current]:
                    stack.append((neighbor, path + [neighbor]))

        return None, float("inf")

    def dijkstra(self, start, goal):
        queue = [(0, start, [])]
        visited = set()

        while queue:
            (cost, current, path) = heapq.heappop(queue)
            if current in visited:
                continue
            visited.add(current)
            path = path + [current]

            if current == goal:
                return path, cost

            for neighbor, weight in self.edges[current].items():
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + weight, neighbor, path))

        return None, float("inf")

    def a_star(self, start, goal):
        open_set = [(self.heuristics.get(start, 0), 0, start, [])]
        visited = set()

        while open_set:
            est_total, cost_so_far, current, path = heapq.heappop(open_set)
            if current in visited:
                continue
            visited.add(current)
            path = path + [current]

            if current == goal:
                return path, cost_so_far

            for neighbor, weight in self.edges[current].items():
                if neighbor not in visited:
                    new_cost = cost_so_far + weight
                    est = new_cost + self.heuristics.get(neighbor, 0)
                    heapq.heappush(open_set, (est, new_cost, neighbor, path))

        return None, float("inf")
