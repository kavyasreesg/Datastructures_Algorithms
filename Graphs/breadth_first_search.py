from queue import Queue

adj_list = {
    "A": ["B", "D"],
    "B": ["A", "C"],
    "C": ["B"],
    "D": ["A", "E", "F"],
    "E": ["D", "F", "G"],
    "F": ["D", "E", "H"],
    "G": ["E", "H"],
    "H": ["G", "F"]
}
visited = {}
level = {}
parent = {}
bfs_traversal_output = []
queue = Queue()

for node in adj_list.keys():
    visited[node] = False
    level[node] = -1
    parent[node] = None

s = "A"
visited[s] = True
level[s] = 0
queue.put(s)

while not queue.empty():
    u = queue.get()
    bfs_traversal_output.append(u)
    for v in adj_list[u]:
        if not visited[v]:
            visited[v] = True
            level[v] = level[u] + 1
            parent[v] = u
            queue.put(v)
print(bfs_traversal_output)

# Level of each node from source node
print(level["G"])

# Shortest path from source to node "G"

v = "G"
path = []
while v is not None:
    path.append(v)
    v = parent[v]
path.reverse()
print(path)


