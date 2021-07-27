"""Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed
edge u v, vertex u comes before v in the ordering. Topological Sorting for a graph is not possible if the graph is
not a DAG.
Perform DFS and try to append the nodes once it's adjacent nodes are completely visited.4
Time complexity is O(V+E) Space is O(V) Graph should be Cyclic
"""
adj_list = {
    "0": [],
    "1": [],
    "2": ["3"],
    "3":["1"],
    "4": ["0", "1"],
    "5": ["2", "0"]
}
color = {}
parent = {}
trav_time = {}
dfs_out = []

for node in adj_list.keys():
    color[node] = "W"
    parent[node] = None
    trav_time[node] = [-1, -1]

time = 0


def dfs_util(u):
    global time
    color[u] = "G"
    trav_time[u][0] = time
    time += 1
    for v in adj_list[u]:
        if color[v] == "W":
            parent[v] = u
            dfs_util(v)
    color[u] = "B"
    trav_time[u][1] = time
    time += 1
    dfs_out.append(u)


for node in adj_list.keys():
    if color[node] == "W":
        dfs_util(node)

print(dfs_out)
print(parent)
print(trav_time)
