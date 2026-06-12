def rabin_karp(text, pattern, prime=101):
    """Rabin-Karp string matching algorithm.
    Time Complexity: O(n + m) average, O(nm) worst
    Space Complexity: O(1)
    """
    d = 256
    q = prime
    n = len(text)
    m = len(pattern)
    
    if m > n:
        return []
    
    pattern_hash = 0
    text_hash = 0
    h = 1
    matches = []
    
    for i in range(m - 1):
        h = (h * d) % q
    
    for i in range(m):
        pattern_hash = (d * pattern_hash + ord(pattern[i])) % q
        text_hash = (d * text_hash + ord(text[i])) % q
    
    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            if text[i:i + m] == pattern:
                matches.append(i)
        
        if i < n - m:
            text_hash = (d * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % q
            if text_hash < 0:
                text_hash += q
    
    return matches

if __name__ == "__main__":
    text = "ababdababcabab"
    pattern = "ababcabab"
    print(f"Pattern found at indices: {rabin_karp(text, pattern)}")
