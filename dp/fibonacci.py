def fibonacci_recursive(n):
    """Fibonacci using recursion (inefficient).
    Time Complexity: O(2^n)
    """
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_dp(n):
    """Fibonacci using dynamic programming.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

def fibonacci_space_optimized(n):
    """Fibonacci with space optimization.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if n <= 1:
        return n
    
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    
    return curr

if __name__ == "__main__":
    n = 10
    print(f"Fibonacci({n}) using DP:", fibonacci_dp(n))
    print(f"Fibonacci({n}) space optimized:", fibonacci_space_optimized(n))
