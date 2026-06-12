class SegmentTree:
    """Segment Tree for range queries and point updates.
    Time Complexity: O(log n) for query and update
    Space Complexity: O(n)
    """
    
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.arr = arr
        if self.n > 0:
            self.build(1, 0, self.n - 1)
    
    def build(self, node, start, end):
        """Build segment tree."""
        if start == end:
            self.tree[node] = self.arr[start]
        else:
            mid = (start + end) // 2
            self.build(2 * node, start, mid)
            self.build(2 * node + 1, mid + 1, end)
            self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]
    
    def update(self, node, start, end, idx, val):
        """Update value at index idx to val."""
        if start == end:
            self.arr[idx] = val
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            if idx <= mid:
                self.update(2 * node, start, mid, idx, val)
            else:
                self.update(2 * node + 1, mid + 1, end, idx, val)
            self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]
    
    def query(self, node, start, end, l, r):
        """Query sum in range [l, r]."""
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        
        mid = (start + end) // 2
        p1 = self.query(2 * node, start, mid, l, r)
        p2 = self.query(2 * node + 1, mid + 1, end, l, r)
        return p1 + p2
    
    def range_query(self, l, r):
        """Public method for range query."""
        return self.query(1, 0, self.n - 1, l, r)
    
    def point_update(self, idx, val):
        """Public method for point update."""
        self.update(1, 0, self.n - 1, idx, val)

if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11]
    st = SegmentTree(arr)
    
    print(f"Sum [1, 4]: {st.range_query(1, 4)}")
    st.point_update(2, 10)
    print(f"After update - Sum [1, 4]: {st.range_query(1, 4)}")
