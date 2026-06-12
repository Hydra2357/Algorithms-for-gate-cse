def coin_change_min_coins(coins, amount):
    """Find minimum number of coins to make amount.
    Time Complexity: O(amount * len(coins))
    Space Complexity: O(amount)
    """
    
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

def coin_change_combinations(coins, amount):
    """Find number of ways to make amount with coins.
    Time Complexity: O(amount * len(coins))
    Space Complexity: O(amount)
    """
    
    dp = [0] * (amount + 1)
    dp[0] = 1
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    
    return dp[amount]

def coin_change_coins_used(coins, amount):
    """Find which coins to use for minimum coins."""
    
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    parent = [-1] * (amount + 1)
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                parent[i] = coin
    
    if dp[amount] == float('inf'):
        return -1, []
    
    coins_used = []
    current = amount
    while current > 0:
        coin = parent[current]
        coins_used.append(coin)
        current -= coin
    
    return dp[amount], coins_used

if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 5
    
    print(f"Min coins: {coin_change_min_coins(coins, amount)}")
    print(f"Combinations: {coin_change_combinations(coins, amount)}")
    
    min_count, coins_used = coin_change_coins_used(coins, amount)
    print(f"Min coins with selection: {min_count}, Coins: {coins_used}")
