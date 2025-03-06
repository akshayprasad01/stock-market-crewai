from pydantic import BaseModel, Field
from crewai.tools import BaseTool
from typing import Type
import yfinance as yf

class MyYahooFinToolInput(BaseModel):
    """Input Schema for my yfinance Tool"""
    stock_ticker: str = Field(... , description="Company stock ticker in string")

class MyYahooFinTool(BaseTool):
    name: str = "Name of my tool"
    description: str = "What this tool does. It's vital for effective utilization."
    args_schema: Type[BaseModel] = MyYahooFinToolInput

    def _run(self, stock_ticker: str) -> str:
        try:
            stock_data = yf.Ticker(ticker=stock_ticker)
            stock_info = stock_data.info
            dividends = stock_data.dividends.tail(5)
            data = yf.download(tickers=stock_ticker, period="1y", interval="1d")
            return_str = f"""Company: {stock_info.get('longName', 'N/A')}
Sector: {stock_info.get('sector', 'N/A')}
Industry: {stock_info.get('industry', 'N/A')}
Market Cap: {stock_info.get('marketCap', 'N/A'):,}
Current Price: {stock_info.get('currentPrice', 'N/A')}
52-Week High: {stock_info.get('fiftyTwoWeekHigh', 'N/A')}
52-Week Low: {stock_info.get('fiftyTwoWeekLow', 'N/A')}
"""
            return return_str
        except Exception as e:
            return "Stock data not found"