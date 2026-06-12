def fenwick_tree_build(arr):
    """Build Binary Indexed Tree (Fenwick Tree).
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    
    n = len(arr)
    tree = [0] * (n + 1)
    
    for i in range(n):
        update(tree, i + 1, arr[i])
    
    return tree

def update(tree, i, delta):
    """Update tree with delta at index i.
    Time Complexity: O(log n)
    """
    
    while i < len(tree):
        tree[i] += delta
        i += i & (-i)

def query(tree, i):
    """Query prefix sum up to index i.
    Time Complexity: O(log n)
    """
    
    s = 0
    while i > 0:
        s += tree[i]
        i -= i & (-i)
    return s

def range_query(tree, l, r):
    """Query sum in range [l, r]."""
    
    return query(tree, r + 1) - (query(tree, l) if l > 0 else 0)

if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11]
    tree = fenwick_tree_build(arr)
    
    print(f"Prefix sum up to index 3: {query(tree, 3)}")
    print(f"Range sum [1, 4]: {range_query(tree, 1, 4)}")
    
    update(tree, 2, 5)  # Add 5 to index 2
    print(f"After update - Prefix sum up to index 3: {query(tree, 3)}")
