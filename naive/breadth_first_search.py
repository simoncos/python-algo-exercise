graph = {1:[2,3,4,5], 3:[6], 4:[5], 6:[1,2,7]}

def has_path_bfs(graph, in_node, out_node):
    from collections import deque
    search_queue = deque()
    search_queue += graph.get(in_node, []) 
    searched = []
    while search_queue:
        n = search_queue.popleft()
        if n not in searched:
            if n == out_node:
                return True
            else:
                search_queue += graph.get(n, [])
            searched.append(n)
    return False

print('graph:', graph)
print('1 to 7:', has_path_bfs(graph, 1, 7))
print('4 to 7:', has_path_bfs(graph, 4, 7))
print('2 to 5:', has_path_bfs(graph, 2, 5))
