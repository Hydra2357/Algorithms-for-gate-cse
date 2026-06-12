def line_segment_intersection(p1, p2, p3, p4):
    """Check if line segment p1p2 intersects with p3p4.
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    
    def ccw(A, B, C):
        return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])
    
    return ccw(p1, p3, p4) != ccw(p2, p3, p4) and ccw(p1, p2, p3) != ccw(p1, p2, p4)

def point_in_polygon_ray_casting(point, polygon):
    """Check if point is inside polygon using ray casting algorithm.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    
    x, y = point
    n = len(polygon)
    inside = False
    
    p1x, p1y = polygon[0]
    for i in range(1, n + 1):
        p2x, p2y = polygon[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    
    return inside

if __name__ == "__main__":
    # Line segment intersection
    p1, p2 = (0, 0), (2, 2)
    p3, p4 = (0, 2), (2, 0)
    print(f"Segments intersect: {line_segment_intersection(p1, p2, p3, p4)}")
    
    # Point in polygon
    point = (1, 1)
    polygon = [(0, 0), (3, 0), (3, 3), (0, 3)]
    print(f"Point in polygon: {point_in_polygon_ray_casting(point, polygon)}")
