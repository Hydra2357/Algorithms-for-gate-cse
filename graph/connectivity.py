from collections import defaultdict

class UnionFind:
    """Union-Find (Disjoint Set Union) data structure.
    Time Complexity: O(α(n)) amortized per operation
    Space Complexity: O(n)
    """
    
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n
    
    def find(self, x):
        """Find the root of the set containing x with path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        """Union two sets containing x and y using union by rank."""
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
        
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        
        self.components -= 1
        return True
    
    def connected(self, x, y):
        """Check if x and y are in the same set."""
        return self.find(x) == self.find(y)

def find_bridges(adj_list, num_vertices):
    """Find all bridges in an undirected graph using DFS.
    Bridge: An edge whose removal disconnects the graph.
    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    
    visited = [False] * num_vertices
    disc = [0] * num_vertices
    low = [0] * num_vertices
    parent = [-1] * num_vertices
    time = [0]
    bridges = []
    
    def dfs(u):
        visited[u] = True
        disc[u] = low[u] = time[0]
        time[0] += 1
        
        for v in adj_list.get(u, []):
            if not visited[v]:
                parent[v] = u
                dfs(v)
                low[u] = min(low[u], low[v])
                
                if low[v] > disc[u]:
                    bridges.append((u, v))
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])
    
    for i in range(num_vertices):
        if not visited[i]:
            dfs(i)
    
    return bridges

def find_articulation_points(adj_list, num_vertices):
    """Find all articulation points in an undirected graph using DFS.
    Articulation Point: A vertex whose removal disconnects the graph.
    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    
    visited = [False] * num_vertices
    disc = [0] * num_vertices
    low = [0] * num_vertices
    parent = [-1] * num_vertices
    time = [0]
    articulation_points = set()
    
    def dfs(u):
        children = 0
        visited[u] = True
        disc[u] = low[u] = time[0]
        time[0] += 1
        
        for v in adj_list.get(u, []):
            if not visited[v]:
                children += 1
                parent[v] = u
                dfs(v)
                low[u] = min(low[u], low[v])
                
                if parent[u] == -1 and children > 1:
                    articulation_points.add(u)
                elif parent[u] != -1 and low[v] >= disc[u]:
                    articulation_points.add(u)
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])
    
    for i in range(num_vertices):
        if not visited[i]:
            dfs(i)
    
    return articulation_points

if __name__ == "__main__":
    # Union-Find example
    uf = UnionFind(5)
    uf.union(0, 1)
    uf.union(1, 2)
    print(f"Connected 0 and 2: {uf.connected(0, 2)}")
    print(f"Connected 0 and 3: {uf.connected(0, 3)}")
    
    # Bridges example
    adj_list = defaultdict(list)
    edges = [(0, 1), (1, 2), (2, 0), (1, 3), (3, 4)]
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    bridges = find_bridges(adj_list, 5)
    print(f"Bridges: {bridges}")
    
    articulation_points = find_articulation_points(adj_list, 5)
    print(f"Articulation points: {articulation_points}")
