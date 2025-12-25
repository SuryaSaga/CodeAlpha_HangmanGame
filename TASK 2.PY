# Stock Portfolio Tracker
# Internship Task Project

STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 130
}

def stock_tracker():
    portfolio = {}
    total_investment = 0

    print("=== Stock Portfolio Tracker ===")
    print("Available stocks:", ", ".join(STOCK_PRICES.keys()))

    while True:
        stock_name = input("\nEnter stock symbol (or 'done' to finish): ").upper()

        if stock_name == "DONE":
            break

        if stock_name not in STOCK_PRICES:
            print("❌ Stock not available.")
            continue

        try:
            quantity = int(input("Enter quantity: "))
            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

    print("\n=== Portfolio Summary ===")
    for stock, qty in portfolio.items():
        price = STOCK_PRICES[stock]
        investment = price * qty
        total_investment += investment
        print(f"{stock} - Quantity: {qty}, Price: ${price}, Value: ${investment}")

    print("\nTotal Investment Value: $", total_investment)

    save_to_file(portfolio, total_investment)


def save_to_file(portfolio, total):
    choice = input("\nDo you want to save the result to a file? (yes/no): ").lower()

    if choice == "yes":
        with open("portfolio_summary.txt", "w") as file:
            file.write("Stock Portfolio Summary\n")
            file.write("------------------------\n")
            for stock, qty in portfolio.items():
                file.write(f"{stock} - Quantity: {qty}, Price: ${STOCK_PRICES[stock]}\n")
            file.write(f"\nTotal Investment: ${total}\n")

        print("✅Portfolio saved to portfolio_summary.txt")


stock_tracker()
