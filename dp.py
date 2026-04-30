def max_profit_dp(prices):
    n = len(prices)
    if n == 0:
        return 0

    dp = [0] * n

    for i in range(1, n):
        max_profit = dp[i-1]
        for j in range(i):
            if prices[i] > prices[j]:
                max_profit = max(max_profit, prices[i] - prices[j] + (dp[j-1] if j >= 1 else 0))
        dp[i] = max_profit

    return dp[-1]