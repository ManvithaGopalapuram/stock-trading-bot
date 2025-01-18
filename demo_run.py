from src.api import robinhood

def main():
    print("Logging in...")
    robinhood.login_to_robinhood()
    print("Account Info:", robinhood.get_account_info())
    print("Portfolio:", robinhood.get_portfolio_stocks())
    print("Buying AAPL:", robinhood.buy_stock("AAPL", 1))
    print("Selling TSLA:", robinhood.sell_stock("TSLA", 1))
    print("Watchlist:", robinhood.get_watchlist_stocks("My Watchlist"))
    print("Ratings:", robinhood.get_ratings("AAPL"))
    print("Historical Data:", robinhood.get_historical_data("AAPL"))

if __name__ == "__main__":
    main()