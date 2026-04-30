def print_transactions(transactions, prices):
    if not transactions:
        print("No profitable transactions")
        return

    for buy, sell in transactions:
        print(f"Buy on day {buy} at price {prices[buy]}, Sell on day {sell} at price {prices[sell]}")