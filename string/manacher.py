def manacher_algorithm(s):
    """Manacher's algorithm for finding longest palindromic substring.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    
    if not s:
        return ""
    
    # Preprocess string
    processed = "#".join("^{}$".format(s))
    n = len(processed)
    p = [0] * n
    center = right = 0
    max_len = 0
    center_index = 0
    
    for i in range(1, n - 1):
        mirror = 2 * center - i
        
        if i < right:
            p[i] = min(right - i, p[mirror])
        
        try:
            while processed[i + p[i] + 1] == processed[i - p[i] - 1]:
                p[i] += 1
        except IndexError:
            pass
        
        if i + p[i] > right:
            center, right = i, i + p[i]
        
        if p[i] > max_len:
            max_len = p[i]
            center_index = i
    
    start = (center_index - max_len) // 2
    return s[start:start + max_len]

if __name__ == "__main__":
    s = "babad"
    print(f"Longest palindromic substring: {manacher_algorithm(s)}")
    
    s = "cbbd"
    print(f"Longest palindromic substring: {manacher_algorithm(s)}")
