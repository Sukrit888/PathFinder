class Graph:
    def __init__(self):
        self.adjacency = {}

    def add_node(self, node):
        if node not in self.adjacency:
            self.adjacency[node] = []

    def add_edge(self, node1, node2, weight=1):
        self.add_node(node1)
        self.add_node(node2)
        self.adjacency[node1].append((node2, weight))
        self.adjacency[node2].append((node1, weight))  # For undirected graph

    def get_nodes(self):
        return list(self.adjacency.keys())

    def get_edges(self):
        edge_set = set()
        for node in self.adjacency:
            for neighbor, weight in self.adjacency[node]:
                edge = tuple(sorted((node, neighbor)))
                edge_set.add((edge[0], edge[1], weight))
        return list(edge_set)

    def dijkstra(self, start, end):
        import heapq
        queue = [(0, start, [])]
        seen = set()

        while queue:
            (cost, node, path) = heapq.heappop(queue)
            if node in seen:
                continue
            seen.add(node)
            path = path + [node]

            if node == end:
                return path, cost

            for neighbor, weight in self.adjacency.get(node, []):
                if neighbor not in seen:
                    heapq.heappush(queue, (cost + weight, neighbor, path))
        return None, float('inf')
