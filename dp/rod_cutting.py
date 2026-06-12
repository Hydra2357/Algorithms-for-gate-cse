def rod_cutting(prices):
    """Rod cutting problem - maximize profit.
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    
    n = len(prices)
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        max_profit = -1
        for j in range(1, i + 1):
            max_profit = max(max_profit, prices[j - 1] + dp[i - j])
        dp[i] = max_profit
    
    return dp[n]

def rod_cutting_with_cut_info(prices):
    """Rod cutting with information about which cuts to make."""
    
    n = len(prices)
    dp = [0] * (n + 1)
    cuts = [0] * (n + 1)
    
    for i in range(1, n + 1):
        max_profit = -1
        for j in range(1, i + 1):
            profit = prices[j - 1] + dp[i - j]
            if profit > max_profit:
                max_profit = profit
                cuts[i] = j
        dp[i] = max_profit
    
    return dp[n], cuts

if __name__ == "__main__":
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    max_profit = rod_cutting(prices)
    print(f"Maximum profit: {max_profit}")
    
    max_profit, cuts = rod_cutting_with_cut_info(prices)
    print(f"Maximum profit with cuts: {max_profit}")
