# task 2
import requests

# Replace 'YOUR_API_KEY' with your actual Alpha Vantage API key
API_KEY = '9GG9RXEE1MJUURKG'

class StockPortfolioTracker:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, shares):
        if symbol in self.portfolio:
            self.portfolio[symbol]['shares'] += shares
        else:
            self.portfolio[symbol] = {'shares': shares, 'price': None}

    def remove_stock(self, symbol, shares):
        if symbol in self.portfolio:
            if shares >= self.portfolio[symbol]['shares']:
                del self.portfolio[symbol]
            else:
                self.portfolio[symbol]['shares'] -= shares

    def update_portfolio(self):
        for symbol in self.portfolio:
            stock_data = self.get_stock_data(symbol)
            if stock_data:
                self.portfolio[symbol]['price'] = stock_data['price']

    def get_stock_data(self, symbol):
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}'

        try:
            response = requests.get(url)
            data = response.json()['Global Quote']
            return {'symbol': symbol, 'price': float(data['05. price'])}
        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")
            return None

    def display_portfolio(self):
        print("Stock Portfolio:")
        for symbol, stock_info in self.portfolio.items():
            shares = stock_info['shares']
            price = stock_info['price']
            if price is not None:
                value = shares * price
                print(f"{symbol}: {shares} shares - ${price:.2f} per share - Total Value: ${value:.2f}")
            else:
                print(f"{symbol}: {shares} shares - Price: Not available")

if __name__ == "__main__":
    tracker = StockPortfolioTracker()

    # Example: Adding stocks to the portfolio
    tracker.add_stock('AAPL', 10)
    tracker.add_stock('GOOGL', 5)
    
    # Display the initial portfolio
    tracker.display_portfolio()

    # Example: Updating and displaying the portfolio
    tracker.update_portfolio()
    tracker.display_portfolio()

    # Example: Removing some shares from the portfolio
    tracker.remove_stock('AAPL', 3)
    tracker.remove_stock('GOOGL', 2)

    # Display the final portfolio
    tracker.update_portfolio()
    tracker.display_portfolio()
