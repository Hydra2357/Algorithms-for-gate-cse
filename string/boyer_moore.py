def boyer_moore(text, pattern):
    """Boyer-Moore string matching algorithm.
    Time Complexity: O(n + m) best, O(nm) worst
    Space Complexity: O(k) where k is alphabet size
    """
    
    if len(pattern) == 0:
        return []
    
    # Build bad character table
    bad_char = {}
    for i in range(len(pattern)):
        bad_char[pattern[i]] = len(pattern) - 1 - i
    
    matches = []
    i = len(pattern) - 1
    
    while i < len(text):
        j = len(pattern) - 1
        
        while j >= 0 and pattern[j] == text[i]:
            i -= 1
            j -= 1
        
        if j < 0:
            matches.append(i + 1)
            i += 1 + len(pattern)
        else:
            i += max(bad_char.get(text[i], 0), 1)
    
    return matches

if __name__ == "__main__":
    text = "ababdababcabab"
    pattern = "ababcabab"
    print(f"Pattern found at indices: {boyer_moore(text, pattern)}")
