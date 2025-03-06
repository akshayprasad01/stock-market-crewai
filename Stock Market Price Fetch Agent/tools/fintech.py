import yfinance as yf
from logger import logger

class StockData:
    def __init__(self, ticker_symbol):
        """Initialize with the ticker symbol."""
        self.ticker_symbol = ticker_symbol
        self.stock = yf.Ticker(ticker_symbol)
        self.info = self.stock.info

    def get_company_info(self):
        """Fetch and display company information."""
        try:
            logger.info(f"Company: {self.info.get('longName', 'N/A')}")
            logger.info(f"Sector: {self.info.get('sector', 'N/A')}")
            logger.info(f"Industry: {self.info.get('industry', 'N/A')}")
            logger.info(f"Market Cap: ₹{self.info.get('marketCap', 'N/A'):,}")
            logger.info(f"Current Price: ₹{self.info.get('currentPrice', 'N/A')}")
            logger.info(f"52-Week High: ₹{self.info.get('fiftyTwoWeekHigh', 'N/A')}")
            logger.info(f"52-Week Low: ₹{self.info.get('fiftyTwoWeekLow', 'N/A')}")
            return_str = f"""Company: {self.info.get('longName', 'N/A')}
Sector: {self.info.get('sector', 'N/A')}
Industry: {self.info.get('industry', 'N/A')}
Market Cap: ₹{self.info.get('marketCap', 'N/A'):,}
Current Price: ₹{self.info.get('currentPrice', 'N/A')}
52-Week High: ₹{self.info.get('fiftyTwoWeekHigh', 'N/A')}
52-Week Low: ₹{self.info.get('fiftyTwoWeekLow', 'N/A')}
"""
            return return_str
        except Exception as e:
            logger.error(f"Error fetching company info: {e}")

    def get_historical_data(self, period="1mo", interval="1d"):
        """Fetch and display historical data.
        Allows fetching data for different periods (1d, 5d, 1mo, 6mo, 1y) and intervals (1m, 5m, 1d, 1wk).
        """
        try:
            history = self.stock.history(period=period, interval=interval)
            if not history.empty:
                logger.info(f"Historical Data (Last {period}):")
                logger.info(history[['Open', 'Close', 'Volume']].tail(5))  # Last 5 rows
            else:
                logger.info(f"No historical data available for {self.ticker_symbol}.")
        except Exception as e:
            logger.error(f"Error fetching historical data: {e}")

    def get_dividends(self):
        """Fetch and display dividend information."""
        try:
            dividends = self.stock.dividends.tail(5)  # Last 5 dividends
            if not dividends.empty:
                logger.info("\nDividends:")
                logger.info(dividends)
            else:
                logger.info("\nNo recent dividends.")
        except Exception as e:
            logger.error(f"Error fetching dividends: {e}")
