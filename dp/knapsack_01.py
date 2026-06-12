def knapsack_01(weights, values, capacity):
    """0/1 Knapsack problem using dynamic programming.
    Time Complexity: O(n * W)
    Space Complexity: O(n * W)
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]

def knapsack_01_space_optimized(weights, values, capacity):
    """0/1 Knapsack with space optimization.
    Space Complexity: O(W)
    """
    dp = [0] * (capacity + 1)
    
    for i in range(len(weights)):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])
    
    return dp[capacity]

if __name__ == "__main__":
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 8
    print(f"Max value (0/1 Knapsack): {knapsack_01(weights, values, capacity)}")
    print(f"Max value (space optimized): {knapsack_01_space_optimized(weights, values, capacity)}")
