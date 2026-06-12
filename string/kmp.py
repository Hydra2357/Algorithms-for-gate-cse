def kmp_search(text, pattern):
    """Knuth-Morris-Pratt string matching algorithm.
    Time Complexity: O(n + m)
    Space Complexity: O(m)
    """
    lps = build_lps(pattern)
    matches = []
    i = j = 0
    
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        if j == len(pattern):
            matches.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return matches

def build_lps(pattern):
    """Build Longest Proper Prefix which is also Suffix array."""
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1
    
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    
    return lps

if __name__ == "__main__":
    text = "ababdababcabab"
    pattern = "ababcabab"
    print(f"Pattern found at indices: {kmp_search(text, pattern)}")
