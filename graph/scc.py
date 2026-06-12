from collections import defaultdict

def tarjan_scc(adj_list, num_vertices):
    """Tarjan's algorithm for finding strongly connected components.
    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    
    index_counter = [0]
    stack = []
    lowlinks = [0] * num_vertices
    index = [0] * num_vertices
    on_stack = [False] * num_vertices
    index_initialized = [False] * num_vertices
    sccs = []
    
    def strongconnect(vertex):
        index[vertex] = index_counter[0]
        lowlinks[vertex] = index_counter[0]
        index_counter[0] += 1
        index_initialized[vertex] = True
        stack.append(vertex)
        on_stack[vertex] = True
        
        for neighbor in adj_list.get(vertex, []):
            if not index_initialized[neighbor]:
                strongconnect(neighbor)
                lowlinks[vertex] = min(lowlinks[vertex], lowlinks[neighbor])
            elif on_stack[neighbor]:
                lowlinks[vertex] = min(lowlinks[vertex], index[neighbor])
        
        if lowlinks[vertex] == index[vertex]:
            scc = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                scc.append(w)
                if w == vertex:
                    break
            sccs.append(scc)
    
    for v in range(num_vertices):
        if not index_initialized[v]:
            strongconnect(v)
    
    return sccs

def kosaraju_scc(adj_list, num_vertices):
    """Kosaraju's algorithm for finding strongly connected components.
    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    
    visited = [False] * num_vertices
    stack = []
    
    def dfs1(vertex):
        visited[vertex] = True
        for neighbor in adj_list.get(vertex, []):
            if not visited[neighbor]:
                dfs1(neighbor)
        stack.append(vertex)
    
    for i in range(num_vertices):
        if not visited[i]:
            dfs1(i)
    
    # Create transpose graph
    transpose = defaultdict(list)
    for u in adj_list:
        for v in adj_list[u]:
            transpose[v].append(u)
    
    visited = [False] * num_vertices
    sccs = []
    
    def dfs2(vertex, scc):
        visited[vertex] = True
        scc.append(vertex)
        for neighbor in transpose.get(vertex, []):
            if not visited[neighbor]:
                dfs2(neighbor, scc)
    
    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            scc = []
            dfs2(vertex, scc)
            sccs.append(scc)
    
    return sccs

if __name__ == "__main__":
    adj_list = defaultdict(list)
    edges = [(0, 1), (1, 2), (2, 0), (1, 3), (3, 4), (4, 5), (5, 3)]
    
    for u, v in edges:
        adj_list[u].append(v)
    
    print("Tarjan's SCCs:", tarjan_scc(adj_list, 6))
    print("Kosaraju's SCCs:", kosaraju_scc(adj_list, 6))
