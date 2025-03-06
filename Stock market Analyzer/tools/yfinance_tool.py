import yfinance as yf
from langchain.tools import tool

def compute_rsi(data, window=14):
    delta = data['Close'].diff(1)
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

class YFinTool:
    @tool("Gather info from yfinance")
    def gatherInfoTool(stock_symbol: str):
        """
        Useful to generate financial data of a company from yahoo Finance.
        """
        try:
            data = yf.download(stock_symbol, period="1y", interval="1d")
            data = data.reset_index()
            data.columns = data.columns.droplevel(1)

            ## Calculate  Moving Averages
            data['50_MA'] = data['Close'].rolling(window=50).mean()
            data['100_MA'] = data['Close'].rolling(window=100).mean()
            data['200_MA'] = data['Close'].rolling(window=200).mean()

            # RSI Calculation
            data['RSI'] = compute_rsi(data)

            # MACD Calculation
            data['EMA_12'] = data['Close'].ewm(span=12, adjust=False).mean()
            data['EMA_26'] = data['Close'].ewm(span=26, adjust=False).mean()
            data['MACD'] = data['EMA_12'] - data['EMA_26']
            data['Signal_Line'] = data['MACD'].ewm(span=9, adjust=False).mean()

            # Bollinger Bands
            data['20_MA'] = data['Close'].rolling(window=20).mean()

            # Compute rolling standard deviation as a Series
            rolling_std = data['Close'].rolling(window=20).std(ddof=0)
            data['Upper_Band'] = data['20_MA'] + 2 * rolling_std[1]
            data['Lower_Band'] = data['20_MA'] - 2 * rolling_std[1]

            # Volume Analysis
            data['Volume_MA'] = data['Volume'].rolling(window=20).mean()

            # Breakout Detection (Bollinger Band Squeeze)
            data['Band_Width'] = (data['Upper_Band'] - data['Lower_Band']) / data['20_MA']
            squeeze = data['Band_Width'] < data['Band_Width'].quantile(0.1)  # 10% narrowest bands

            return data.to_string()
        except Exception as e:
            print(f"Error Occured: {e}")
            return None
        

    @tool("Gather Stock Price from Yfinance")
    def getStockPrice(stock_symbol: str):
        """
        Useful to generate financial data of a company from yahoo Finance.
        """
        try:
            stock = yf.Ticker(stock_symbol)
            info = stock.info
            return_str = f"""Company: {info.get('longName', 'N/A')}
Sector: {info.get('sector', 'N/A')}
Industry: {info.get('industry', 'N/A')}
Market Cap: {info.get('marketCap', 'N/A'):,}
Current Price: {info.get('currentPrice', 'N/A')}
52-Week High: {info.get('fiftyTwoWeekHigh', 'N/A')}
52-Week Low: {info.get('fiftyTwoWeekLow', 'N/A')}
"""
            return return_str
        except Exception as e:
            print(f"Error fetching company info: {e}")
