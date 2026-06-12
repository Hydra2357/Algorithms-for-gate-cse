def edit_distance(s1, s2):
    """Levenshtein distance using dynamic programming.
    Minimum number of single-character edits (insert, delete, replace).
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)
    """
    
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    
    return dp[m][n]

def edit_distance_space_optimized(s1, s2):
    """Space-optimized version using only two arrays.
    Space Complexity: O(n)
    """
    
    m, n = len(s1), len(s2)
    if m < n:
        s1, s2 = s2, s1
        m, n = n, m
    
    prev = list(range(n + 1))
    curr = [0] * (n + 1)
    
    for i in range(1, m + 1):
        curr[0] = i
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                curr[j] = prev[j - 1]
            else:
                curr[j] = 1 + min(prev[j], curr[j - 1], prev[j - 1])
        prev, curr = curr, prev
    
    return prev[n]

if __name__ == "__main__":
    s1 = "kitten"
    s2 = "sitting"
    print(f"Edit distance: {edit_distance(s1, s2)}")
    print(f"Edit distance (space optimized): {edit_distance_space_optimized(s1, s2)}")
