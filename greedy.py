def max_profit_greedy(prices):
    profit = 0
    transactions = []

    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
            transactions.append((i-1, i))

    return profit, transactions
