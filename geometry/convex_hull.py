def graham_scan(points):
    """Graham scan algorithm for convex hull.
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    
    points = sorted(set(points))
    if len(points) <= 1:
        return points
    
    # Build lower hull
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    
    # Build upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    
    return lower[:-1] + upper[:-1]

def jarvis_march(points):
    """Jarvis march (gift wrapping) algorithm for convex hull.
    Time Complexity: O(n * h) where h is hull size
    Space Complexity: O(n)
    """
    
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    
    n = len(points)
    if n < 3:
        return sorted(points)
    
    hull = []
    l = 0
    
    for i in range(1, n):
        if points[i][0] < points[l][0]:
            l = i
    
    p = l
    while True:
        hull.append(points[p])
        q = (p + 1) % n
        
        for i in range(n):
            if cross(points[p], points[i], points[q]) > 0:
                q = i
        
        p = q
        if p == l:
            break
    
    return hull

if __name__ == "__main__":
    points = [(0, 0), (1, 1), (2, 2), (0, 2), (2, 0), (1, 0)]
    
    print(f"Convex hull (Graham scan): {graham_scan(points)}")
    print(f"Convex hull (Jarvis march): {jarvis_march(points)}")
