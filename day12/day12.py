import copy


class Node:
    def __init__(self, name: str):
        self.name = name
        self.edges = []

    def add_edge(self, name):
        self.edges.append(name)

    def is_finished(self):
        return self.name == 'end'

    def small_cave(self):
        return self.name.lower() == self.name


def get_data(filename):
    nodes = {}
    with open(filename) as f:
        for line in f.readlines():
            start, end = line.rstrip().split('-')
            if start not in nodes:
                nodes[start] = Node(start)

            nodes[start].add_edge(end)

            if end not in nodes:
                nodes[end] = Node(end)

            nodes[end].add_edge(start)

    return nodes


def search(nodes, current_node, paths, path_index):
    if nodes[current_node].small_cave() and paths[path_index][0] and current_node in paths[path_index]:
        return

    if current_node == 'start' and len(paths[path_index]) > 2:
        return

    if nodes[current_node].small_cave() and paths[path_index].count(current_node) == 1:
        paths[path_index][0] = True

    paths[path_index].append(current_node)

    if current_node == 'end':
        return

    for edge in nodes[current_node].edges:
        new_path = copy.deepcopy(paths[path_index])
        paths.append(new_path)
        search(nodes, edge, paths, len(paths) - 1)


nodes = get_data('input.txt')
paths = [[False]]
search(nodes, 'start', paths, 0)

legit_paths = []
for path in paths:
    if len(path) > 2 and path[1] == 'start' and path[-1] == 'end':
        legit_paths.append(path)

print(len(legit_paths))
