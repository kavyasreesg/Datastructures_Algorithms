adj_list = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["B"],
    "D": [],
    "E": ["F"],
    "F": []
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
    dfs_out.append(u)
    trav_time[u][0] = time
    time += 1
    for v in adj_list[u]:
        if color[v] == "W":
            parent[v] = u
            dfs_util(v)
    color[u] = "B"
    trav_time[u][1] = time
    time += 1


dfs_util("A")
print(dfs_out)
print(parent)
print(trav_time)
