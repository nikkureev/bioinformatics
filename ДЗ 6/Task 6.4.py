graph = {'1': ['2', '3'],
         '2': ['1', '4', '5'],
         '3': ['1', '6'],
         '4': ['2'],
         '5': ['2', '6'],
         '6': ['3', '5']}


def dfs(graph, start):
    visited, stack = [], [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack.extend(set(graph[vertex]) - set(visited))
    return visited
