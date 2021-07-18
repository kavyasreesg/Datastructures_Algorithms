class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print(self.graph_dict)

    def get_path(self, start, end, path=[]):
        path = [start] + path
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []
        paths = []
        for node in self.graph_dict[start]:
            if node not in paths:
                new_paths = self.get_path(node, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths

    def shortest_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]
        if start not in self.graph_dict:
            return None
        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
        return shortest_path


if __name__ == '__main__':
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "New York"),
        ("Paris", "Dubai"),
        ("Dubai", "New York"),
        ("New York", "Toronto")
    ]
    graph = Graph(routes)
    print(graph.get_path("Mumbai", "New York"))
    print(graph.shortest_path("Mumbai", "New York"))