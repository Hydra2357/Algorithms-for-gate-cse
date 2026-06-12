def z_algorithm(s):
    """Z-algorithm for pattern matching.
    Computes Z-array where Z[i] is the length of longest substring
    starting from s[i] which is also prefix of s.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    
    n = len(s)
    z = [0] * n
    z[0] = n
    l, r = 0, 0
    
    for i in range(1, n):
        if i > r:
            l, r = i, i
            while r < n and s[r - l] == s[r]:
                r += 1
            z[i] = r - l
            r -= 1
        else:
            k = i - l
            if z[k] < r - i + 1:
                z[i] = z[k]
            else:
                l = i
                while r < n and s[r - l] == s[r]:
                    r += 1
                z[i] = r - l
                r -= 1
    
    return z

def z_algorithm_search(text, pattern):
    """Use Z-algorithm to find all occurrences of pattern in text."""
    
    combined = pattern + "$" + text
    z = z_algorithm(combined)
    matches = []
    
    for i in range(len(pattern) + 1, len(combined)):
        if z[i] == len(pattern):
            matches.append(i - len(pattern) - 1)
    
    return matches

if __name__ == "__main__":
    s = "aabaab"
    z = z_algorithm(s)
    print(f"Z-array: {z}")
    
    text = "ababdababcabab"
    pattern = "ababcabab"
    matches = z_algorithm_search(text, pattern)
    print(f"Pattern found at indices: {matches}")
