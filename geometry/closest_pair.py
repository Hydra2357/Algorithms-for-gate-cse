def closest_pair_bruteforce(points):
    """Find closest pair of points - brute force approach.
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    
    def distance(p1, p2):
        return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5
    
    min_dist = float('inf')
    closest_pair = None
    
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = distance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                closest_pair = (points[i], points[j])
    
    return closest_pair, min_dist

def closest_pair_divide_conquer(points):
    """Find closest pair using divide and conquer.
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    
    def distance(p1, p2):
        return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5
    
    def closest_pair_recursive(px, py):
        n = len(px)
        
        if n <= 3:
            min_dist = float('inf')
            closest = None
            for i in range(n):
                for j in range(i + 1, n):
                    d = distance(px[i], px[j])
                    if d < min_dist:
                        min_dist = d
                        closest = (px[i], px[j])
            return closest, min_dist
        
        mid = n // 2
        midpoint = px[mid]
        
        pyl = [p for p in py if p[0] <= midpoint[0]]
        pyr = [p for p in py if p[0] > midpoint[0]]
        
        pair1, dist1 = closest_pair_recursive(px[:mid], pyl)
        pair2, dist2 = closest_pair_recursive(px[mid:], pyr)
        
        min_dist = min(dist1, dist2)
        closest_pair = pair1 if dist1 < dist2 else pair2
        
        strip = [p for p in py if abs(p[0] - midpoint[0]) < min_dist]
        
        for i in range(len(strip)):
            j = i + 1
            while j < len(strip) and strip[j][1] - strip[i][1] < min_dist:
                d = distance(strip[i], strip[j])
                if d < min_dist:
                    min_dist = d
                    closest_pair = (strip[i], strip[j])
                j += 1
        
        return closest_pair, min_dist
    
    px = sorted(points, key=lambda p: p[0])
    py = sorted(points, key=lambda p: p[1])
    
    return closest_pair_recursive(px, py)

if __name__ == "__main__":
    points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10)]
    
    pair, dist = closest_pair_bruteforce(points)
    print(f"Closest pair (brute force): {pair}, distance: {dist:.2f}")
    
    pair, dist = closest_pair_divide_conquer(points)
    print(f"Closest pair (D&C): {pair}, distance: {dist:.2f}")
