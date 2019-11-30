graph = {'1': ['2', '3'],
         '2': ['1', '4', '5'],
         '3': ['1', '6'],
         '4': ['2'],
         '5': ['2', '6'],
         '6': ['3', '5'],
         '7': ['8'],
         '8': ['7'],
         '9': ['10', '7'],
         '10': ['9']}


def comp_count(graph):

    def dfs(graph, start):
        visited, stack = [], [start]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.append(vertex)
                stack.extend(set(graph[vertex]) - set(visited))
        return visited

    vis_list = []
    for i in range(1, len(graph)):
        vis_list.append(dfs(graph, str(i)))

    comp = 1
    for i in range(len(vis_list) - 1):
        for j in vis_list[i]:
            if j not in vis_list[i + 1]:
                comp += 1
                break

    print(comp)


comp_count(graph)
