# Hardcoded dictionary of stock prices
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 320,
    "GOOGL": 140,
    "AMZN": 130
}

def stock_tracker():
    print("📊 Welcome to Stock Portfolio Tracker")
    print("Available stocks:", ", ".join(STOCK_PRICES.keys()))

    portfolio = {}
    total_value = 0

    # Step 1: Take user input
    while True:
        stock = input("Enter stock symbol (or 'done' to finish): ").upper().strip()
        if stock == "DONE":
            break
        if stock not in STOCK_PRICES:
            print("❌ Stock not found. Try again.")
            continue

        try:
            qty = int(input(f"Enter quantity of {stock}: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        # Step 2: Store in portfolio dictionary
        portfolio[stock] = portfolio.get(stock, 0) + qty
        print(f"✅ Added {qty} shares of {stock}.")

    # Step 3: Calculate total investment
    print("\n===== Portfolio Summary =====")
    for stock, qty in portfolio.items():
        value = STOCK_PRICES[stock] * qty   # basic arithmetic
        total_value += value
        print(f"{stock}: {qty} shares × ${STOCK_PRICES[stock]} = ${value}")

    print(f"\n💰 Total Investment Value: ${total_value}")

    # Step 4: Optional file save
    save = input("Save portfolio to file? (y/n): ").lower().strip()
    if save == "y":
        choice = input("Save as TXT or CSV? (txt/csv): ").lower().strip()
        if choice == "txt":
            with open("portfolio.txt", "w") as f:
                f.write("Stock Portfolio Summary\n")
                for stock, qty in portfolio.items():
                    value = STOCK_PRICES[stock] * qty
                    f.write(f"{stock}: {qty} shares × ${STOCK_PRICES[stock]} = ${value}\n")
                f.write(f"\nTotal Investment Value: ${total_value}\n")
            print("📂 Portfolio saved to portfolio.txt")
        elif choice == "csv":
            with open("portfolio.csv", "w") as f:
                f.write("Stock,Quantity,Price,Value\n")
                for stock, qty in portfolio.items():
                    value = STOCK_PRICES[stock] * qty
                    f.write(f"{stock},{qty},{STOCK_PRICES[stock]},{value}\n")
                f.write(f"Total,,,{total_value}\n")
            print("📂 Portfolio saved to portfolio.csv")

if __name__ == "__main__":
    stock_tracker()
