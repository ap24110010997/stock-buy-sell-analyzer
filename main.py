from greedy import max_profit_greedy
from dp import max_profit_dp
from utils import print_transactions

prices = list(map(int, input("Enter stock prices (space separated): ").split()))

# Greedy
profit_greedy, transactions = max_profit_greedy(prices)

# DP
profit_dp = max_profit_dp(prices)

print("\n--- Results ---")
print(f"Greedy Profit: {profit_greedy}")
print_transactions(transactions, prices)

print(f"\nDP Profit: {profit_dp}")