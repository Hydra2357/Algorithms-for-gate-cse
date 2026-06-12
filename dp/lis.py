def lis_length(arr):
    """Longest Increasing Subsequence length using DP.
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    n = len(arr)
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp) if dp else 0

def lis_binary_search(arr):
    """Longest Increasing Subsequence using binary search.
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    import bisect
    
    tails = []
    for num in arr:
        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num
    
    return len(tails)

if __name__ == "__main__":
    arr = [10, 9, 2, 5, 3, 7, 101, 18]
    print(f"LIS length (DP): {lis_length(arr)}")
    print(f"LIS length (Binary Search): {lis_binary_search(arr)}")
