import heapq
import time

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def add_node(self, value):
        self.nodes.add(value)
        if value not in self.edges:
            self.edges[value] = []

    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node].append((to_node, weight))

def slowSP(graph, start):
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0
    queue = list(graph.nodes)

    while queue:
        min_node = None
        for node in queue:
            if min_node is None or distances[node] < distances[min_node]:
                min_node = node

        queue.remove(min_node)

        for neighbor, weight in graph.edges.get(min_node, []):
            new_distance = distances[min_node] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

    return distances

def fastSP(graph, start):
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_dist, min_node = heapq.heappop(queue)

        for neighbor, weight in graph.edges.get(min_node, []):
            new_distance = current_dist + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(queue, (new_distance, neighbor))

    return distances

def measure_performance(graph):
    slow_times = []
    fast_times = []

    for node in graph.nodes:
        start_time = time.perf_counter()
        slowSP(graph, node)
        slow_times.append(time.perf_counter() - start_time)

        start_time = time.perf_counter()
        fastSP(graph, node)
        fast_times.append(time.perf_counter() - start_time)

    return slow_times, fast_times

def plot_histogram(times, title):
    import matplotlib.pyplot as plt

    plt.hist(times, bins=20)
    plt.title(title)
    plt.xlabel('Execution Time (s)')
    plt.ylabel('Frequency')
    plt.show()

if __name__ == "__main__":
    # Example usage
    g = Graph()
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_edge(1, 2, 1)
    g.add_edge(2, 3, 2)
    g.add_edge(1, 3, 4)

    slow_times, fast_times = measure_performance(g)

    print("Slow algorithm:")
    print("Average time: {:.5f}".format(sum(slow_times) / len(slow_times)))
    print("Max time: {:.5f}".format(max(slow_times)))
    print("Min time: {:.5f}".format(min(slow_times)))

    print("\nFast algorithm:")
    print("Average time: {:.5f}".format(sum(fast_times) / len(fast_times)))
    print("Max time: {:.5f}".format(max(fast_times)))
    print("Min time: {:.5f}".format(min(fast_times)))

    plot_histogram(slow_times, "Slow Algorithm Execution Times")
    plot_histogram(fast_times, "Fast Algorithm Execution Times")
    
# Q4 results:
# the histogram shows 3 bars indicating 3 different times: 0.2 x e^-5s, 0.6 x e^-5s, and 
# and 1.3 x e^-5s. All times have a frequency of 1.