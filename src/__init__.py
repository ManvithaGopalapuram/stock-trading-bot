def login_to_robinhood():
    print("Mock login successful.")
    return {"access_token": "mock_token"}

def get_account_info():
    return {
        "buying_power": 10000.0,
        "url": "https://mock.robinhood.com/account/",
        "other_info": "mocked"
    }

def get_portfolio_stocks():
    return {
        "AAPL": {"quantity": 10, "price": 150.0, "average_buy_price": 140.0},
        "TSLA": {"quantity": 5, "price": 700.0, "average_buy_price": 650.0}
    }

def buy_stock(symbol, quantity):
    return {"id": "mock", "symbol": symbol, "quantity": quantity, "status": "filled"}

def sell_stock(symbol, quantity):
    return {"id": "mock", "symbol": symbol, "quantity": quantity, "status": "filled"}

def get_watchlist_stocks(name):
    return [
        {"symbol": "AAPL", "price": 150.0},
        {"symbol": "TSLA", "price": 700.0}
    ]

def get_ratings(symbol):
    return {"symbol": symbol, "ratings": [{"type": "buy", "published_at": "2024-01-01", "text": "Strong buy"}]}

def get_historical_data(symbol, interval="day", span="year"):
    return [{"close_price": 150.0, "high_price": 155.0, "low_price": 145.0, "volume": 1000000} for _ in range(30)]
